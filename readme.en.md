# GraphQL FastAPI

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/luiisp/graphql-fastapi/blob/main/readme.en.md)
> Speak in English? [Access Readme.md in English](https://github.com/luiisp/graphql-fastapi/blob/main/readme.en.md)

Tag this project with a star 🌟  
![grapqlv](https://github.com/luiisp/graphql-fastapi/assets/115284250/3750ddf5-cae0-4224-9ce2-12410c44272d)

![gpl+fastapi](https://miro.medium.com/v2/resize:fit:720/format:webp/1*yvwpVOnyE5PB60ot-hCCSw.png)

This project is a GraphQL API implemented with FastAPI.

## What is GraphQL and what advantage does it have over REST?

GraphQL is a query and manipulation language for APIs created by Facebook. GraphQL makes it easier for clients to use the API because it gives clients the power to ask for exactly what they need and nothing more, which facilitates scalability and performance.

### What are the problems with REST?

One of the fundamental problems with REST is the flexibility of the data being transmitted. When different clients with different needs start consuming your API, you may encounter a phenomenon known as over-fetching and under-fetching:

- **over-fetching**: It's when you're getting too much data, not necessary for your purpose, and wasting bandwidth on your request.

  > Example: You only need the name and email of a user, but the API returns all the user's data, such as address, phone number, etc.

- **under-fetching**: The opposite. When you don't get enough data and need to make other calls to fulfill your purpose.

  > Example: You need data from a user, but the API only returns the name, and you need to make another request to get the email.

### How does GraphQL solve these problems?

GraphQL solves this by allowing the client to specify exactly what they need. The client can ask for exactly what they need, and the API will return exactly what was requested.

### Advantages of using GraphQL

- **Efficient data retrieval**: GraphQL allows clients to retrieve only the data they need, eliminating over-fetching and under-fetching, reducing bandwidth usage.

- **Flexible queries**: Clients can specify the exact data requirements in their queries, allowing them to retrieve related data in a single request.

  > **Example**: Imagine that at different times, the client needs different data, in a REST pattern it would be necessary to create two different endpoints to handle each of these requests. With GraphQL, only one route would be necessary, and the client could request **ONLY** the data they need.

- **Strongly typed**: GraphQL is strongly typed, clients already know what to expect from the API response.

- **Versionless API**: With GraphQL, API changes can be introduced without disrupting existing clients. Clients can request specific fields and easily handle schema changes, ensuring compatibility with previous versions.

## Features

- [✅] User registration
- [✅] Update requested user fields
- [✅] Delete user
- [✅] Query user fields or all users

## Technologies

- FastApi
- Bcrypt (Encryption)
- SQLAlchemy (ORM)
- Strawberry (GraphQL)
- Uvicorn

## Running

1. Clone the repository `git clone https://github.com/luiisp/graphql-fastapi`
2. Install dependencies `pip install -r requirements.txt`
3. Run the server `uvicorn main:app --reload`
4. Access the GraphQL playground at `http://localhost:8000/graphql`

## Examples


### Mutation

#### Creating a User

> Creates a user with the fields name, username, password, and email

```graphql
mutation {
  createUser(name: "pedroluis",
  username: "luiisp",
  password: "password@123", 
  email: "luisp.diias@gmail.com") {
    id
    name
    username
    email
  }
}
```

#### Updating User Data

> Updates the email of the user with id 1

```graphql
mutation {
  updateUser(id:1,
  email: "newemail@gmail.com") {
    id
    email
  }
}
```

#### Deleting User

> Deletes the user with id 1

```graphql
mutation {
  deleteUser(id:1) {
    id
    name
    username
    email
  }
}
```

### Query

#### Querying All Users

> Queries the fields name and email of all registered users

```graphql
query {
  users {
    id
    name
    email
  }
}
```

#### Querying User by ID

> Queries the fields name and username of the user with id 1

```graphql
query {
  user(id: 1) {
    id
    name
    username
  }
}
```

### Author

- [Pedro Luis](https://github.com/luiisp)

### References

- [GraphQL](https://graphql.org/)
- [Kinsta.com](https://kinsta.com/pt/blog/graphql-vs-rest/)

## Screenshots

![image](https://github.com/luiisp/graphql-fastapi/assets/115284250/ece8f006-657d-48b5-a44c-4e36aeaa5627)
![image](https://github.com/luiisp/graphql-fastapi/assets/115284250/62693a98-d058-4f62-9810-7dde251589fb)
