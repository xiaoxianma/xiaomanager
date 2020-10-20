import enum
from sqlalchemy.sql.schema import CheckConstraint, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Enum, DateTime, Text

from app.db.session import Base


class Institution(Base):
    __tablename__ = 'institution'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    def __str__(self) -> str:
        return self.name


class AccountOwner(Base):
    __tablename__ = 'accountowner'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    def __str__(self) -> str:
        return self.name


class AccountType(enum.Enum):
    credit_card = 'CRED'
    debit_card = 'DEBT'
    cash = 'CASH'
    checking = 'CHCK'
    saving = 'SAVE'


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, index=True)
    institution_id = Column(Integer, ForeignKey("institution.id", ondelete="SET NULL"))
    account_owner_id = Column(Integer, ForeignKey("accountowner.id", ondelete="SET NULL"))
    account_type = Column(Enum(AccountType))
    number = Column(String)
    alias = Column(String)

    def __str__(self) -> str:
        ret = f'{self.owner}|{self.institution}|{self.account_type}'
        if self.alias:
            ret = f'{ret}|{self.alias}'
        return ret


class RewardType(Base):
    __tablename__ = 'rewardtype'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    def __str__(self) -> str:
        return self.name


class Reward(Base):
    __tablename__ = 'reward'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("account.id", ondelete="SET NULL"))
    reward_type_id = Column(Integer, ForeignKey("rewardtype.id", ondelete="SET NULL"))
    xpoints = Column(Integer)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=True)
    description = Column(Text)

    __table_args__ = (
        CheckConstraint(xpoints > 0, name='check_xponits_positive'),
    )

    def __str__(self) -> str:
        if self.end_time:
            active_period = f'{self.end_time.year}-{self.end_time.month:02d}-{self.end_time.day:02d}'
        else:
            active_period = "4ever"
        return f"{self.account}|{active_period}|{self.reward_type}"
