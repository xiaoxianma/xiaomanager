import enum

from app.db.session import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import CheckConstraint, Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Enum, Integer, String, Text
from sqlalchemy_utils import generic_repr


@generic_repr
class Institution(Base):
    __tablename__ = "institution"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


@generic_repr
class AccountOwner(Base):
    __tablename__ = "accountowner"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class AccountType(enum.Enum):
    credit_card = "CRED"
    debit_card = "DEBT"
    cash = "CASH"
    checking = "CHCK"
    saving = "SAVE"


@generic_repr
class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    institution_id = Column(Integer, ForeignKey("institution.id", ondelete="SET NULL"))
    account_owner_id = Column(
        Integer, ForeignKey("accountowner.id", ondelete="SET NULL")
    )
    account_type = Column(Enum(AccountType))
    number = Column(String)
    alias = Column(String)

    institution = relationship(Institution, backref="account")
    account_owner = relationship(AccountOwner, backref="account")


@generic_repr
class RewardType(Base):
    __tablename__ = "rewardtype"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


@generic_repr
class Reward(Base):
    __tablename__ = "reward"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("account.id", ondelete="SET NULL"))
    reward_type_id = Column(Integer, ForeignKey("rewardtype.id", ondelete="SET NULL"))
    xpoints = Column(Integer)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=True)
    description = Column(Text)

    __table_args__ = (CheckConstraint(xpoints > 0, name="check_xponits_positive"),)
