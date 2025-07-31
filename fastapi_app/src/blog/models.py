from sqlalchemy import String, Text, Table, Column, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.base_class import Base


article_tag = Table("article_tags",
                          Base.metadata,
                    Column('article_id', ForeignKey("articlemodel.id"), primary_key=True),
                          Column('tag_id', ForeignKey("tagmodel.id"), primary_key=True))

class ArticleModel(Base):
    __tablename__ = "articlemodel"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(255),nullable=False,default="Статья без названия")
    text: Mapped[str] = mapped_column(Text(),nullable=False)
    author = relationship("UserModel",back_populates="articles",lazy="selectin")
    author_id: Mapped[int] = mapped_column(ForeignKey("usermodel.id"))
    tags = relationship("TagModel",secondary=article_tag,back_populates="articles",lazy="selectin")

class TagModel(Base):
    __tablename__ = "tagmodel"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(255),nullable=False,default="Без названия")
    articles = relationship("ArticleModel",secondary=article_tag,back_populates="tags")
