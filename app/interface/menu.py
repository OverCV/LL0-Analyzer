from constants.const import *
from models.language import Language
from services.reader import Reader
from lang.LL1 import LL1


class Menu:
    ''' Class Menu is used to view data. '''

    def __init__(self) -> None:
        self._lector: Reader = Reader()
        pass

    def display(self, ends: int = 1, starts: int = 1) -> None:
        ''' Display menu. '''
        files: list[str] = process_txts(starts, ends)

        for file in files:
            lang: Language = self._lector.txt_to_lang(file)
            analyzer: LL1 = LL1(lang)

            # print(lang)

            inits: dict = analyzer.inits_lang()

            print(f'\nINITS: ')
            for key, value in inits.items():
                print(f'prim({key}) = {value}')

            nexts: dict = analyzer.nexts_lang()

            print(f'\nNEXTS: ')
            for key, value in nexts.items():
                print(f'next({key}) = {value}')
            print(f'\n')
