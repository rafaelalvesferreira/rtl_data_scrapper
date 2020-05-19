import os
import datetime
from func_timeout import FunctionTimedOut
from R3_16_1 import Relatorio3_16_1
from R3_16_2 import Relatorio3_16_2
from R_5_7_1 import Relatorio5_7_1
from R_5_7_1_GPS import Relatorio5_7_1_GPS
from R_5_12_2 import Relatorio5_12_2

day = str(datetime.datetime.now().date())

final_data_path = os.path.join('C:\\Users',
                               os.getlogin(),
                               'Downloads',
                               day)

with open('Usuario_Senha.txt', 'r') as f:
    for linha in f:
        if linha.split()[0] == 'Usuario:':
            lg = linha.split()[1]
        if linha.split()[0] == 'Senha:':
            pwd = linha.split()[1]

try:
    Relatorio3_16_1("1", "132000", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_1-132000.timeout'), 'w'):
        pass

try:
    Relatorio3_16_1("2", "61913", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_1-61913.timeout'), 'w'):
        pass

try:
    Relatorio3_16_1("4", "85789", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_1-85789.timeout'), 'w'):
        pass

try:
    Relatorio3_16_1("3", "63785", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_1-63785.timeout'), 'w'):
        pass

try:
    Relatorio3_16_2("1", "132000", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_2-132000.timeout'), 'w'):
        pass

try:
    Relatorio3_16_2("2", "61913", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_2-61913.timeout'), 'w'):
        pass

try:
    Relatorio3_16_2("4", "85789", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_2-85789.timeout'), 'w'):
        pass

try:
    Relatorio3_16_2("3", "63785", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'3_16_2-63785.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1("1", "132000", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1-132000.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1("2", "61913", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1-61913.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1("4", "85789", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1-85789.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1("3", "63785", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1-63785.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_GPS("1", "132000", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_GPS-132000.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_GPS("2", "61913", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_GPS-61913.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_GPS("4", "85789", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_GPS-85789.timeout'), 'w'):
        pass

try:
    Relatorio5_7_1_GPS("3", "63785", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_7_1_GPS-63785.timeout'), 'w'):
        pass

try:
    Relatorio5_12_2("1", "132000", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_12_2-132000.timeout'), 'w'):
        pass

try:
    Relatorio5_12_2("2", "61913", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_12_2-61913.timeout'), 'w'):
        pass

try:
    Relatorio5_12_2("4", "85789", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_12_2-85789.timeout'), 'w'):
        pass

try:
    Relatorio5_12_2("3", "63785", lg, pwd)
except FunctionTimedOut:
    with open(os.path.join(final_data_path,
                           f'5_12_2-63785.timeout'), 'w'):
        pass
