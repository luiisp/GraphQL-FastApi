from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    _password = Column('password', String) 
    email = Column(String, unique=True, index=True)
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_password):
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        self._password = hashed_password.decode('utf-8')
