from sqlalchemy.orm import Session


class BaseCRUDService:
    def __init__(self, model):
        self.model = model

    def get(self,db: Session, id: int):
        return db.query(self.model).filter(self.model.id==id).first()

