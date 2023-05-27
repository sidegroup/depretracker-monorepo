# Scripts

## O que é?

Consiste em uma série de scripts que automatizam tarefas repetitivas e/ou complexas.

## Scripts disponíveis

### [**`translate_csv.py`**](./translate_csv.py)
Traduz um arquivo csv, basta informar a coluna que deve ser traduzida e o idioma para qual deve ser traduzido.

```bash
make scripts-translate-csv FILE=example.csv COLUMN=1 LANG=pt
# OU
docker-compose run --rm scripts python3 translate_csv.py datasets/example.csv 2 p
# OU
python3 scripts/translate_csv.py datasets/example.csv 1 pt
```

#### Exemplos

```bash
make scripts-translate-csv FILE=datasets/spanish_tweets_suggesting_signs_of_depression_v1.csv COLUMN=2 LANG=pt
# OU
docker-compose run --rm scripts 

```
