from datetime import date, datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    display_name: str = Field(index=True, max_length=160)
    email: Optional[str] = Field(default=None, max_length=254)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: Optional[int] = Field(default=None, foreign_key="person.id", index=True)
    starts_at: datetime = Field(index=True)
    service: str = Field(max_length=160)
    status: str = Field(default="scheduled", max_length=32)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source_id: Optional[str] = Field(default=None, index=True, max_length=120)
    person_name: str = Field(max_length=160)
    service: str = Field(max_length=160)
    amount_minor: int = Field(gt=0)
    currency: str = Field(index=True, max_length=3)
    paid_on: date = Field(index=True)
    reference: Optional[str] = Field(default=None, max_length=240)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
