import hmac
import os
from collections import defaultdict
from contextlib import asynccontextmanager
from datetime import date

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session, select

from .database import create_db_and_tables, get_session
from .models import Payment
from .schemas import CashflowMonth, PaymentCreate, PaymentRead

load_dotenv()
API_TOKEN = os.getenv("ARIGATO_API_TOKEN", "")
if not API_TOKEN:
    raise RuntimeError("ARIGATO_API_TOKEN must be configured before starting the API")

origins = [item.strip() for item in os.getenv(
    "CORS_ORIGINS", "https://devmansworld.github.io"
).split(",") if item.strip()]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="ARIGATO Database API", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

bearer = HTTPBearer(auto_error=False)

def require_token(credentials: HTTPAuthorizationCredentials | None = Depends(bearer)) -> None:
    if credentials is None or not hmac.compare_digest(credentials.credentials, API_TOKEN):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/health")
def health():
    return {"status": "ok", "service": "arigato-db", "version": "0.1.0"}

@app.get("/api/payments", response_model=list[PaymentRead], dependencies=[Depends(require_token)])
def list_payments(session: Session = Depends(get_session)):
    return session.exec(select(Payment).order_by(Payment.paid_on.desc(), Payment.id.desc())).all()

@app.post(
    "/api/payments",
    response_model=PaymentRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_token)],
)
def create_payment(payload: PaymentCreate, session: Session = Depends(get_session)):
    if payload.source_id:
        existing = session.exec(
            select(Payment).where(Payment.source_id == payload.source_id)
        ).first()
        if existing:
            raise HTTPException(status_code=409, detail="source_id already exists")
    payment = Payment(**payload.model_dump())
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment

@app.get(
    "/api/cashflow",
    response_model=list[CashflowMonth],
    dependencies=[Depends(require_token)],
)
def cashflow(session: Session = Depends(get_session)):
    payments = session.exec(select(Payment)).all()
    totals: dict[tuple[str, str], dict[str, int]] = defaultdict(
        lambda: {"total_minor": 0, "transaction_count": 0}
    )
    for payment in payments:
        key = (payment.paid_on.strftime("%Y-%m"), payment.currency)
        totals[key]["total_minor"] += payment.amount_minor
        totals[key]["transaction_count"] += 1
    return [
        CashflowMonth(month=month, currency=currency, **values)
        for (month, currency), values in sorted(totals.items())
    ]
