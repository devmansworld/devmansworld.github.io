from datetime import date
from typing import Literal, Optional

from sqlmodel import SQLModel, Field


class PaymentCreate(SQLModel):
    source_id: Optional[str] = Field(default=None, max_length=120)
    person_name: str = Field(min_length=1, max_length=160)
    service: str = Field(min_length=1, max_length=160)
    amount_minor: int = Field(gt=0)
    currency: Literal["CLP", "USD"]
    paid_on: date
    reference: Optional[str] = Field(default=None, max_length=240)


class PaymentRead(PaymentCreate):
    id: int


class CashflowMonth(SQLModel):
    month: str
    currency: Literal["CLP", "USD"]
    total_minor: int
    transaction_count: int
