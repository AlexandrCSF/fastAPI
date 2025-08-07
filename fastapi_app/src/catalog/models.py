from datetime import datetime

from db.base_class import Base
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ProductModel(Base):
    __tablename__ = "productmodel"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[float]
    description: Mapped[str] = mapped_column(String(1000), nullable=True, default=None)
    comments = relationship("CommentModel", back_populates="product")

class CommentModel(Base):
    __tablename__ = "commentmodel"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text,default=None)
    rating: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    author = relationship("UserModel",back_populates="comments",lazy="selectin")
    author_id: Mapped[int] = mapped_column(ForeignKey("usermodel.id"))

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("commentmodel.id"), nullable=True)
    parent: Mapped["CommentModel"] = relationship(back_populates="replies")
    replies: Mapped[list["CommentModel"]] = relationship(
        back_populates="parent",
        remote_side=[id],
        cascade="all"
    )

    product = relationship("ProductModel",back_populates="comments",lazy="selectin")
    product_id: Mapped[int] = mapped_column(ForeignKey("productmodel.id"))
