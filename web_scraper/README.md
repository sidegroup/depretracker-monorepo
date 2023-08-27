# DepreTracker - Web Scraper

## Como executar
Considerando que você está dentro da pasta `web_scraper`:

```bash
make build # apenas na primeira vez, para instalar as dependências no docker
make run # executa o script
```

## Kibana
Para facilitar a visualização dos dados coletados, é possível utilizar o Kibana.
Para isso acesse http://localhost:5601/app/dev_tools#/console e execute o seguinte comando:

Dica: Basta copiar e colar o comando no console do Kibana e apertar `ctrl + enter` para executar.


### Para exemplos com o dataset deprimido
```bash
GET reddit_depressed_posts/_count

GET reddit_depressed_comments/_count

GET reddit_depressed_posts/_search

GET reddit_depressed_comments/_search
```

### Para exemplos com o dataset não deprimido
```bash
GET reddit_neutral_posts/_count

GET reddit_neutral_comments/_count

GET reddit_neutral_posts/_search

GET reddit_neutral_comments/_search
```