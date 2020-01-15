from collections import OrderedDict
import os
import sys

ADVANCED_INTERPRETATION_WORDS_PATH = r"D:\forever wisedom\AdvancedInterpretation\words"  # 这个需要自己指定
TMP_LATEX_PATH = r"D:\python_box\EasyEnglishTerminal\compile"


class Word:
    def __init__(self, cn, en, cn2en=2, WorS=1):
        '''

        :param cn:
        :param en:
        :param cn2en: cn2en = 2 代表英到中，默认2
        :param WorS: WorS = 1 代表单词，默认1
        '''
        assert WorS == 1 or WorS == 2
        assert cn2en == 1 or cn2en == 2
        # en	cn	cn2en	WorS	comment
        self.cn = cn
        self.en = en
        self.cn2en = cn2en
        self.WorS = WorS

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(
            self.cn, self.en,
            "中翻英" if self.cn2en == 1 else "英译中",
            "单词" if self.WorS == 1 else "句子",
        )


class WordList:
    def __init__(self):
        self.words = []

    def append(self, X):
        self.words.append(X)

    def __add__(self, other):
        self.append(X=other)

    def __str__(self):
        return "".join(
            x.__str__() + "\n" for x in self.words
        )

    def split(self):
        A = WordList()
        B = WordList()
        [A.append(X) for X in self.words if X.WorS == 1]
        [B.append(X) for X in self.words if X.WorS == 2]
        return A, B

    def __len__(self):
        return self.words.__len__()

    def __list__(self):
        return self.words


class LatexCompileError(Exception):
    def __init__(self, numA, numB):
        self.numA = numA
        self.numB = numB

    def __str__(self):
        return f"Latex文档编译失败!"


class XLSXHeaderError(Exception):
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return "文件{} 头行参数错误，参考template.xlsx书写".format(self.filename)
