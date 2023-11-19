# Side Web APP
O Side Web APP é uma aplicação web que fornece um conjunto de ferramentas para mineração de dados e pré-processamento de dados.

# Ferramentas
- Mineração de dados
  - [ ] Web Scraping (Em planejamento)
- Data preprocessing
  - [x] Tradução de arquivos

# Executando localmente
## Pré-requisitos
O projeto roda em Docker. O docker compose e o Makefile estão aqui para facilitar nossas vidas.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

## Iniciando o projeto
O Side Web APP depende do banco de dados e do tradutor, que é uma simples aplicação em 'python.
O comando abaixo irá iniciar todos os serviços necessários para o projeto.

```bash
make up
```

Acesse o projeto em [http://localhost:3000](http://localhost:3000)