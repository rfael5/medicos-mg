import csv

with open("C:\\Users\\rfael\\medicos-mg\\mdmg\\medicos\\medicos-mg.csv", 'r') as arquivo:
        tabela = csv.reader(arquivo, delimiter=';')

        for linha in tabela:
            _, meds = Medicos.objects.get_or_create(
                num=linha[0],
                nome=linha[1],
                status=linha[2],
                especializacao=linha[3],
            )