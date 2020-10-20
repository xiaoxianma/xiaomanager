from sqlalchemy.sql.schema import CheckConstraint, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime, Text
from sqlalchemy_utils import CountryType

from app.db.session import Base


class ExpenseType(Base):
    __tablename__ = "expensetype"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    def __str__(self) -> str:
        return self.name


class Merchant(Base):
    __tablename__ = "merchant"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    country = Column(CountryType)

    def __str__(self) -> str:
        return f"{self.name}|{self.city}|{self.country}".replace('||', '|')


class Transaction(Base):
    __tablename__ = "transaction"


    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    account_id = Column(Integer, ForeignKey("account.id", ondelete="SET NULL"))
    merchant_id = Column(Integer, ForeignKey("merchant.id", ondelete="SET NULL"))
    expense_type_id = Column(Integer, ForeignKey("expensetype.id", ondelete="SET NULL"))
    transaction_date = Column(DateTime(timezone=True), nullable=False)
    coupon = Column(Integer)
    tags = Column(String)
    notes = Column(Text)
    created = Column(DateTime(timezone=True), nullable=False)

    __table_args__ = (
        CheckConstraint(coupon > 0, name='check_coupon_positive'),
    )