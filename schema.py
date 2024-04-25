import strawberry
from .models.models import UserModel

@strawberry.type
class PublicUser:
    id: int
    name: str
    username: str
    email: str
