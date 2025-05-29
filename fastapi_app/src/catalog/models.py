from db.base_class import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class ProductModel(Base):
    __tablename__ = "productmodel"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[float]
    description: Mapped[str] = mapped_column(String(1000), nullable=True, default=None)
