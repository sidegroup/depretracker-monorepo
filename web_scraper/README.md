# Wedex - Web Data Extractor

Wedex é uma aplicação completa de extração, visualização e download de dados de redes sociais, composta por backend em Python, frontend em Angular, e stack ELK (Elasticsearch + Kibana) para armazenamento.

**OBS: As pastas estão sendo referidas como web_scraper pois nas primeiras versões esta nomenclatura foi utilizada, porém, a ferramenta está em processo de remodelação e transferência para outro diretório, onde os mesmos serão nomedados corretamente.**

## 🧰 Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- `make` instalado na sua máquina

---

## 🚀 Como executar

Certifique-se de estar dentro da pasta `web_scraper`:

```bash
make build  # Apenas na primeira vez. Instala as dependências e constrói os containers
make run    # Inicia todos os serviços

---

## 🧱 Arquitetura dos Serviços

- **web_scraper_be**: API backend em Flask que utiliza a PRAW para se comunicar com a Reddit, extrai os dados e envia ao Elasticsearch.
- **web_scrapper_interface**: Interface web em Angular para interação com os dados extraídos.
- **Elasticsearch**: Armazena os dados extraídos da web.
- **Kibana**: Dashboard para visualização dos dados presentes no Elasticsearch.

---

## ✅ Healthchecks

Os containers possuem verificações de saúde para garantir a inicialização correta dos serviços:

- **Elasticsearch** só é considerado ativo quando estiver com status `green` ou `yellow`.
- **Kibana** só inicia após o Elasticsearch estar saudável.
- **Backend** espera Elasticsearch e Kibana.
- **Frontend** depende do backend.

---

## 📁 Estrutura de Pastas

├── web_scraper/ # Backend 
│ └── Dockerfile # Dockerfile do backend
├── web_scrapper_interface/
│ └── wedext/ # Código Angular do frontend
│ └── Dockerfile.angular # Dockerfile do frontend
├── docker-compose.yml # Orquestração dos serviços
├── Makefile # Comandos utilitários
└── README.md # Este arquivo
