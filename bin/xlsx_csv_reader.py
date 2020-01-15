from config import *

import openpyxl
from openpyxl.utils import get_column_letter
import os


def __verify_header(wl):
    header = "en	cn	cn2en	WorS	comment".split("\t")
    if [wl['A1'].value, wl['B1'].value, wl['C1'].value, wl['D1'].value, wl['E1'].value] == header:
        return True
    else:
        return False


def handle_xlsx(file_name="Jan10th.xlsx", path=ADVANCED_INTERPRETATION_WORDS_PATH):
    if not os.path.exists(os.path.join(ADVANCED_INTERPRETATION_WORDS_PATH, file_name)):
        raise FileNotFoundError
    wb = openpyxl.load_workbook(os.path.join(ADVANCED_INTERPRETATION_WORDS_PATH, file_name))
    wl = wb['word']
    if not __verify_header(wl):
        raise XLSXHeaderError(file_name)
    return __read_words(wl)


def __read_words(wl):
    i = 2
    WL = WordList()
    while wl['A{}'.format(i)].value is not None:
        WL.append(
            Word(wl['A{}'.format(i)].value, wl['B{}'.format(i)].value,
                 int(wl['C{}'.format(i)].value) if wl['C{}'.format(i)].value is not None else 1,
                 int(wl['D{}'.format(i)].value) if wl['D{}'.format(i)].value is not None else 1)
        )
        i += 1
    return WL

# 打开excel文件,获取工作簿对象
