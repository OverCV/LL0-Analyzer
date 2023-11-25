from models.language import Language
from models.token import Token
from models.production import Production


class LL1:
    ''' Class LL1 is used to analyze lexically a language. '''

    def __init__(self, language: Language = None) -> None:
        self._language: Language = language

        self._prims_dict: dict[str: set] = dict()
        self._nexts_dict: dict[str: set] = dict()

    def get_language(self) -> Language:
        ''' Get language. '''
        return self._language

    def set_prims_dict(self) -> bool:
        ''' Function to set the dict of initials '''
        self._prims_dict: dict[str: set] = dict()
        self._prims_dict: dict[str: set] = self.inits_lang()
        return True

    def set_nexts_dict(self) -> bool:
        ''' Function to set the dict of followings '''
        self._nexts_dict: dict[str: set] = dict()
        self._nexts_dict: dict[str: set] = self.next_lang()

    def inits_lang(self) -> dict[str:set]:
        ''' Function to get the first of a language. '''

        prim_dict: dict[str: set] = dict()
        productions: list[Production] = self._language.get_productions()

        for production in productions:
            main_token: Token = production.get_mtoken()
            prim_dict[main_token.get_lexema()]\
                = self.inits(production, set())

        return prim_dict

    def inits(self, production: Production, prim_set: set) -> set:
        ''' Function to get the first of one production. '''

        for pattern in production.get_patterns():
            first: Token = pattern.get_first()

            if first.is_terminal():
                # prim_set.add(first)
                # prim_set.add(
                #     (first.get_lexema(), first.is_terminal())
                # )
                prim_set.add(
                    first.get_lexema()
                )
            else:
                lexema: Token = first.get_lexema()
                wanted_production: Token = self._language\
                    .get_production(lexema)
                prim_set.union(self.inits(wanted_production, prim_set))
        return prim_set

    def nexts_lang(self) -> dict:
        ''' Function to get the following of a language. '''
        nexts_dict: dict = dict()

        prods: list[Production] = self.get_language().get_productions()
        mtokens: list[Token] = [
            prod.get_mtoken()for prod in prods
        ]

        for token in mtokens:
            nexts_dict[
                token.get_lexema()
            ] = self.nexts(token, set())

        return nexts_dict

    def nexts(self, token: Token, nexts_set: set) -> set:
        ''' Function to get the following of one Token. '''
        # print(f'TKN: {token.get_lexema()} NEXTS: {nexts_set}')
        self.set_prims_dict()

        is_initial: bool = self._language.is_initial_token(token)
        if is_initial:
            nexts_set.add("$")

        loc_prods: list[Production] | None\
            = self._language.get_prods_contains(token)
        if loc_prods == None:
            print(f'variable: {token.get_lexema()} has any prod.')
            return nexts_set

        # [
        #     print(f'PROD: {prod}') for prod in loc_prods
        # ]
        # print('\n')

        for prod in loc_prods:
            for pattern in prod.get_patterns():
                if not pattern.includes_token(token):
                    continue

                next_token: Token | None = pattern.next_token(token)

                if next_token == None:
                    if prod.eq_mtoken(token):
                        continue
                    nexts_set = nexts_set.union(
                        self.nexts(prod.get_mtoken(), nexts_set)
                    )
                elif next_token.is_terminal():
                    nexts_set.add((
                        next_token.get_lexema()
                    ))
                elif not next_token.is_terminal():
                    inits: set = self._prims_dict[
                        next_token.get_lexema()
                    ]
                    nexts_set = nexts_set.union(inits)
                    if not nexts_set.__contains__('λ'):
                        continue

                    nexts_set.remove('λ')
                    if prod.eq_mtoken(token):
                        continue
                    nexts_set = nexts_set.union(
                        self.nexts(prod.get_mtoken(), nexts_set)
                    )

        return nexts_set
