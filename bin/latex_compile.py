import os
from datetime import datetime
import shutil
import config.latex_config as la
from config import TMP_LATEX_PATH, ADVANCED_INTERPRETATION_WORDS_PATH
from config import WordList, Word
from bin.xlsx_csv_reader import handle_xlsx


def dictation_paper_compiler(words, sentences, user="匿名", saving_file_name="words", quiet=True):
    latex = la.latex_header_gen(title="每日单词", user_name=user)
    if words.__len__() > 0:
        latex += la.word_part_start()
        for word_index in range(0, words.__len__(), 2):
            try:
                latex += la.word_part_double_column_with_underline(
                    index1=str(word_index + 1),
                    word1=words[word_index].cn if words[word_index].cn2en == 2 else words[word_index].en,
                    index2=str(word_index + 2),
                    word2=words[word_index + 1].cn if words[word_index + 1].cn2en == 2 else words[word_index + 1].en
                )
            except IndexError:
                latex += la.word_part_single_column_with_underline(
                    index=str(word_index + 1),
                    word=words[word_index].cn if words[word_index].cn2en == 2 else words[word_index].en,
                )
    if sentences.__len__() > 0:
        latex += la.sentence_part_start()
        for sentence_index in range(0, sentences.__len__()):
            latex += la.sentence_part_with_underline(
                index=str(sentence_index + 1),
                sentence=sentences[sentence_index].cn if sentences[sentence_index].cn2en == 2 else sentences[
                    sentence_index].en
            )
    latex += la.tail()

    open(TMP_LATEX_PATH + "\\tmp.tex", 'w', encoding="utf8").write(latex)
    os.system(la.compile_cmd(TMP_LATEX_PATH + '\\tmp.tex', quiet=quiet))
    os.remove('tmp.aux')
    os.remove('tmp.log')
    f_name = datetime.strftime(datetime.now(), '{}_dict_%m_%d'.format(saving_file_name.split(".")[0])) + ".pdf"
    shutil.move('tmp.pdf', "{}".format(ADVANCED_INTERPRETATION_WORDS_PATH + "\\" + f_name))
    return f_name


def answer_sheet_compiler(words, sentences, user="烧包", saving_file_name="answer", quiet=True):
    latex = la.latex_header_gen("每日单词答案", user_name=user)
    if words.__len__() > 0:
        latex += la.word_part_start()
        for word_index in range(0, words.__len__(), 2):
            try:
                latex += la.word_part_double_column_with_answer(
                    index1=str(word_index + 1),
                    word1=words[word_index].cn if words[word_index].cn2en == 2 else words[word_index].en,
                    answer1=words[word_index].cn if words[word_index].cn2en == 1 else words[word_index].en,
                    index2=str(word_index + 2),
                    word2=words[word_index + 1].cn if words[word_index + 1].cn2en == 2 else words[word_index + 1].en,
                    answer2=words[word_index + 1].cn if words[word_index + 1].cn2en == 1 else words[word_index + 1].en,
                )
            except IndexError:
                latex += la.word_part_single_column_with_answer(
                    index=str(word_index + 1),
                    word=words[word_index].cn if words[word_index].cn2en == 2 else words[word_index].en,
                    answer=words[word_index].cn if words[word_index].cn2en == 1 else words[word_index].en,
                )
    if sentences.__len__() > 0:
        latex += la.sentence_part_start()
        for sentence_index in range(0, sentences.__len__()):
            latex += la.sentence_part_with_answer(
                index=str(sentence_index + 1),
                sentence=sentences[sentence_index].cn if sentences[sentence_index].cn2en == 2 else sentences[
                    sentence_index].en,
                answer=sentences[sentence_index].cn if sentences[sentence_index].cn2en == 1 else sentences[
                    sentence_index].en
            )
    latex += la.tail()

    open(TMP_LATEX_PATH + "\\tmp.tex", 'w', encoding="utf8").write(latex)
    os.system(la.compile_cmd(TMP_LATEX_PATH + '\\tmp.tex', quiet=quiet))
    os.remove('tmp.aux')
    os.remove('tmp.log')
    f_name = datetime.strftime(datetime.now(), '{}_ans_%m_%d'.format(saving_file_name.split(".")[0])) + ".pdf"
    shutil.move('tmp.pdf', "{}".format(ADVANCED_INTERPRETATION_WORDS_PATH + "\\" + f_name))
    return f_name


def main(file_name, quiet):
    # print(file_name)
    wl = handle_xlsx(file_name)
    words, sentences = wl.split()
    dictation_paper_compiler(words.__list__(), sentences.__list__(), saving_file_name=file_name, quiet=quiet)
    print("dictation paper compiled !")
    answer_sheet_compiler(words.__list__(), sentences.__list__(), saving_file_name=file_name, quiet=quiet)
    print("answer sheet paper compiled !")
