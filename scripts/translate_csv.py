# Script para traduçao de arquivos csv
# Autor: Kelvin Romero
# O script agurda 3 parametros
# 1 - Arquivo csv a ser traduzido
# 2 - Idiomar origem
# 3 - Idioma destino

from deep_translator import GoogleTranslator
import sys
import csv


# Funcao para traduzir o arquivo csv
def translate_csv(file, column, target_language):
    try:
        file_name = file.split('/')[1]
        output_file = './outputs/' + file_name + 'translated.csv'
    except:
        output_file = './outputs/' + file + 'translated.csv'


    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(output_file, 'w') as csv_output:
            csv_writer = csv.writer(csv_output, delimiter=',')
            first_line = True

            print('\nTraduzindo...')
            for row in csv_reader:
                print('.', end='', flush=True)
                if first_line:
                    first_line = False
                    csv_writer.writerow(row)
                    continue

                column = int(column)

                translated = GoogleTranslator(source='auto', target=target_language).translate(row[column])
                row_translated = row
                row_translated[column] = translated

                csv_writer.writerow(row_translated)


# Funcao principal
def main():
    # Verifica se a quantidade de parametros esta correta
    if len(sys.argv) != 4:
        print("Como usar: python3 translate_csv.py <file> <column> <target_language>")
        print("Exemplo: python3 translate_csv.py file.csv 0 pt")
        sys.exit(1)
    # Traduz o arquivo csv
    translate_csv(sys.argv[1], sys.argv[2], sys.argv[3])


# Chama a funcao principal
if __name__ == "__main__":
    main()
