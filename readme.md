# GraphQL FastAPI

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/luiisp/graphql-fastapi/blob/main/readme.en.md)
> Speak in English? [Access Readme.md in English](https://github.com/luiisp/graphql-fastapi/blob/main/readme.en.md)

Tag this project with a star 🌟  
![grapqlv](https://github.com/luiisp/graphql-fastapi/assets/115284250/3750ddf5-cae0-4224-9ce2-12410c44272d)

![gpl+fastapi](https://miro.medium.com/v2/resize:fit:720/format:webp/1*yvwpVOnyE5PB60ot-hCCSw.png)

Este projeto é uma API GraphQL implementada com FastApi.

## O que é o GraphQL e qual vantagem sobre o REST?

GraphQL é uma linguagem de consulta e manipulação de dados para API criado pelo Facebook. O GraphQL facilita o uso da API pelos clientes, pois dá aos clientes o poder de pedir exatamente o que precisam e nada mais, o que facilita na escalabilidade e desempenho.

### Quais são os problemas do REST?

Um dos problemas fundamentais do REST é a flexibilidade dos dados sendo transmitidos. Quando diferentes clientes, com diferentes necessidades, começam a consumir sua API, é possível que você enfrente um fenômeno conhecido por over-fetching e under-fetching:

- **over-fetching**: É quando você está recebendo dados demais, não necessários para o seu propósito, e utilizando mais banda atoa em sua requisição.

  > Exemplo: Você precisa apenas do nome e email de um usuário, mas a API retorna todos os dados do usuário, como endereço, telefone, etc.

- **under-fetching**: O oposto. Quando você não recebe dados o suficiente e precisa realizar outras chamadas para cumprir o seu propósito.

  > Exemplo: Você precisa de dados de um usuário, mas a API retorna apenas o nome, e você precisa fazer outra requisição para pegar o email.

### Como o GraphQL resolve esses problemas?

O GraphQL resolve isso permitindo que o cliente especifique exatamente o que ele precisa. O cliente pode pedir exatamente o que ele precisa, e a API retornará exatamente o que foi pedido.

### Vantagens do uso GraphQL

- **Recuperação eficiente de dados**: GraphQL permite que os clientes recuperem apenas os dados de que precisam, eliminando a busca excessiva e insuficiente, reduzindo o uso de banda.

- **Consultas flexíveis**: Os clientes podem especificar os requisitos exatos de dados em suas consultas, permitindo-lhes recuperar dados relacionados em uma única solicitação.

  > **Exemplo**: imaginando que em duas ocasiões diferentes o cliente precise de dados diferentes em tempos diferentes, em um padrão REST seria necessário criar dois endpoints diferentes para atender a cada uma dessas requisições. Já no GraphQL seria necessário apenas uma rota, e o cliente poderia pedir **APENAS** os dados que ele precisa.

- **Fortemente tipado**: o GraphQL é fortemente tipado, os clientes já sabem o que esperar da resposta da API.

- **API sem versão**: com GraphQL, alterações de API podem ser introduzidas sem interromper os clientes existentes. Os clientes podem solicitar campos específicos e lidar facilmente com alterações de esquema, garantindo compatibilidade com versões anteriores.

## Features

- [✅] Cadastro de usuário
- [✅] Atualização de campos requisitados do usuário
- [✅] Deletar usuário
- [✅] Consultar campos de usuário ou todos os usuários

## Tecnologias

- FastApi
- Bcrypt (Criptografia)
- SQLAlchemy (ORM)
- Strawberry (GraphQL)
- Uvicorn

## Rodando

1. Clone o repositório `git clone https://github.com/luiisp/graphql-fastapi`
2. Instale as dependências `pip install -r requirements.txt`
3. Rode o servidor `uvicorn main:app`
4. Acesse o playground do GraphQL em `http://localhost:8000/graphql`

## Examples


### Mutation 

#### Criando  usuario

> Cria um usuario com os campos name, username, password e email



```
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

#### Atualizando dados do usuario

> Atualiza o email do usuario com id 1

```
mutation {
  updateUser(id:1,
  email: "novoemail@gmail.com") {
    id
    email
  }
}
```

#### Deletando usuario
> Deleta o usuario com id 1

```
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

#### Consultando todos os usuarios

> Consulta os campos name e email de todos os usuarios cadastrados 

```

query {
  users {
    id
    name
    email
  }
}

```

#### Consultando usuario por id

> Consulta os campos name e username do usuario com id 1

```

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

### Referências

- [GraphQL](https://graphql.org/)
- [Kinsta.com](https://kinsta.com/pt/blog/graphql-vs-rest/)

## Screenshots

![image](https://github.com/luiisp/graphql-fastapi/assets/115284250/ece8f006-657d-48b5-a44c-4e36aeaa5627)
![image](https://github.com/luiisp/graphql-fastapi/assets/115284250/62693a98-d058-4f62-9810-7dde251589fb)
