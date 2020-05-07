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

lg = 'RAFAELFERRE'
pwd = 'Rafa001*el'

try:
    Relatorio3_16_1("1", "132000", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_1("2", "61913", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_1("4", "85789", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_1("3", "63785", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_2("1", "132000", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_2("2", "61913", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_2("4", "85789", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio3_16_2("3", "63785", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1("1", "132000", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1("2", "61913", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1("4", "85789", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1("3", "63785", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1_GPS("1", "132000", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1_GPS("2", "61913", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1_GPS("4", "85789", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_7_1_GPS("3", "63785", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_12_2("1", "132000", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_12_2("2", "61913", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_12_2("4", "85789", lg, pwd)
except FunctionTimedOut:
    pass

try:
    Relatorio5_12_2("3", "63785", lg, pwd)
except FunctionTimedOut:
    pass
