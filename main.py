from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from resolvers import Query, Mutation

app = FastAPI()

schema = strawberry.Schema(query=Query, mutation=Mutation)


app.mount("/graphql", GraphQL(schema, debug=True))
