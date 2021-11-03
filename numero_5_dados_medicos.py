'''5) Leia o arquivo MEDICOS.CSV (em anexo) e crie uma função DADOS_MEDICOS que receba
como parâmetro o caminho do arquivo e que imprima as seguintes informações:
- Número total de médicos
- Número de médico por status
- Número de médicos ativos com / sem especialização
- Número e porcentagem de médicos ativos por especializaçã'''

import csv

def dados_medicos(arquivo):
    total_medicos = 0
    medicos_ativos = 0
    medicos_falecidos = 0
    medicos_cancelados = 0
    medicos_transferidos = 0
    md_com_especializacao = 0
    md_sem_especializacao = 0

    total_especializacoes = []
    lista_md_especializados = []
    especializacoes_sepadadas = []
    with open('medicos-mg.csv', 'r') as medicosmg:
        tabela = csv.reader(medicosmg, delimiter=';')

        for linha in tabela:
            total_medicos += 1
            if linha[2] == 'ATIVO':
                medicos_ativos += 1
            elif linha[2] == 'FALECIDO':
                medicos_falecidos += 1
            elif linha[2] == 'CANCELADO':
                medicos_cancelados += 1
            elif linha[2] == 'TRANSFERIDO':
                medicos_transferidos += 1

            if linha[2] == 'ATIVO' and linha[3] != '':
                md_com_especializacao += 1
                lista_md_especializados.append(linha[3])
            if linha[2] == 'ATIVO' and linha[3] == '':
                md_sem_especializacao += 1

        print(f'Total de médicos: {total_medicos}')
        print(f'Médicos ativos: {medicos_ativos}')
        print(f'Médicos falecidos: {medicos_falecidos}')
        print(f'Médicos transferidos: {medicos_transferidos}')
        print(f'Registros cancelados: {medicos_cancelados}')
        print(f'Médicos com especialização: {md_com_especializacao}')
        print(f'Medicos sem especialização: {md_sem_especializacao}')


dados_medicos('medicos-mg.csv')




