import os
import datetime
from func_timeout import FunctionTimedOut
from R_5_7_1_IC import Relatorio5_7_1_IC


day = str(datetime.datetime.now().date())

final_data_path = os.path.join('C:\\Users',
                               os.getlogin(),
                               'Downloads',
                               day)

try:
    with open('Usuario_Senha.txt', 'r') as f:
        for linha in f:
            if linha.split()[0] == 'Usuario:':
                lg = linha.split()[1]
            if linha.split()[0] == 'Senha:':
                pwd = linha.split()[1]
except IndexError:
    pass

# ORDEM DAS LISTAS
# [IC, INDICADOR, Outro, Nome do Arquivo]
#
# Na função
#
#                Num Site, Cod Site, login , senha, dados, 'D' se for dia atual
#                                                     'D-1' se for dia anterior
# Relatorio5_7_1_IC("1", "132000", lg, pwd, dados, 'D')


dados = [
    [16, 8, 56, 'CV_TT'],
    [16, 8, 55, 'RGB_TT'],
    [16, 8, 130, 'PORT_TT'],
    [16, 8, 147, 'REFRIGENANC'],
    [16, 8, 86, 'HE_TT'],
    [7, 8, 0, 'GPS_TT'],
    [10, 8, 0, 'POSIT_TT']
        ]

try:
    Relatorio5_7_1_IC("1", "132000", lg, pwd, dados, 'D')
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_IC-CG.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_IC("2", "61913", lg, pwd, dados, 'D')
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_IC-AQ.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_IC("4", "85789", lg, pwd, dados, 'D')
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_IC-CB.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_IC("3", "63785", lg, pwd, dados, 'D')
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_IC-CX.timeout'), 'w'):
        pass
