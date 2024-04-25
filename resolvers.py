import strawberry
from typing import List, Optional
from database import get_db
from schema import PublicUser
from models.models import UserModel

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[PublicUser]:
        db = next(get_db())
        users = db.query(UserModel).all()
        return [PublicUser(id=user.id,
                            name=user.name,
                            username=user.username, 
                            email=user.email) for user in users]

    @strawberry.field
    def user(self, id: int) -> PublicUser:
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.id == id).first()
        if user:
            return PublicUser(id=user.id, 
                              name=user.name, 
                              username=user.username, 
                              email=user.email)
        else:
            return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self,
                    name: str,
                    username: str,
                    password: str,
                    email: str) -> PublicUser:
        db = next(get_db())
        user = UserModel(name=name, 
                         username=username, 
                         password=password, 
                         email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return PublicUser(id=user.id,
                          name=user.name,
                          username=user.username, 
                          email=user.email)

    @strawberry.mutation
    def update_user(self, id: int, email: str, name: Optional[str] = None, username: Optional[str] = None, password: Optional[str] = None) -> PublicUser:
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.id == id).first()
        if user:
            if name is not None:
                user.name = name
            if username is not None:
                user.username = username
            if password is not None:
                user.password = password
            user.email = email
            db.commit()
            return PublicUser(id=user.id, name=user.name, username=user.username, email=user.email)
        else:
            return None


    @strawberry.mutation
    def delete_user(self, id: int) -> PublicUser:
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.id == id).first()
        if user:
            db.delete(user)
            db.commit()
            return PublicUser(id=user.id, 
                              name=user.name, 
                              username=user.username, 
                              email=user.email)
        else:
            return None