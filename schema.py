import strawberry


@strawberry.type
class PublicUser:
    id: int
    name: str
    username: str
    email: str
