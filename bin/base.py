from bin.latex_compile import main
from config import ADVANCED_INTERPRETATION_WORDS_PATH, TMP_LATEX_PATH
import os

import optparse
from collections import OrderedDict


class EasyEnglishTerminal(object):
    def show_info(self):
        print(
            "ADVANCED_INTERPRETATION_WORDS_PATH : \n\t",
            ADVANCED_INTERPRETATION_WORDS_PATH,
            "\n"
            "TMP_LATEX_PATH :  \n\t",
            TMP_LATEX_PATH,
        )

    def show_listing_file(self):
        X = os.system('dir "{}"'.format(ADVANCED_INTERPRETATION_WORDS_PATH))

    def __init__(self):
        self.H_HEADER = '\033[95m'
        self.H_OK_BLUE = '\033[94m [i] '
        self.H_OK_GREEN = '\033[96m [+] '
        self.H_WARNING = '\033[93m [!] '
        self.H_FAIL = '\033[31m [X] '
        self.H_DEBUG = ' [D] '
        self.E_END = '\033[0m'
        self.E_BOLD = '\033[1m'
        self.E_UNDERLINE = '\033[4m'
        self.options = optparse.Values()
        self.task_list = OrderedDict()

    def run_shell(self):
        self.parser()
        self.handler()

    def parser(self):
        '''
        :return:
        '''
        usage = 'Usage: %prog [options] arg1 arg2 ...'
        parser = optparse.OptionParser(usage, version='%prog 1.0')
        parser.add_option("-i", "--info", dest="show_info",
                          action="store_true", default=False,
                          help="Show info.")
        parser.add_option("-d", "--dir", dest="show_files",
                          action="store_true", default=False,
                          help="Show files.")

        parser.add_option("-f", "--file", dest="file_name", type="string", default="",
                          action="store", help="The file name. The file is in the Word Path Dir"
                          )
        # parser.add_option("-p", "--clear-daily", action="store_true", default=False, dest="clear_daily",
        #                   help="Clear daily task if call this option")
        (self.options, _) = parser.parse_args()

    def handler(self):
        if self.options.show_info:
            self.show_info()
        if self.options.show_files:
            self.show_listing_file()
        if self.options.file_name == "":
            optparse.OptionParser().error(
                self.E_BOLD + "[!] Must input file name " + self.E_END
            )
        else:
            main(self.options.file_name)
