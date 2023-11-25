# from models.language import Language


# class Grammar:
#     ''' Class Grammar services is used to implement usefull Language methods. '''

#     def __init__(self, name: str) -> None:
#         self._name: str = name
#         self._languages: list[Language] = []

#     def get_languages(self) -> list[Language]:
#         ''' Get languages from grammar. '''
#         return self._languages

#     def get_language(self, name: str) -> Language:
#         ''' Get language from grammar. '''
#         for language in self._languages:
#             if language.get_name() == name:
#                 return language
#         return None

#     def add_language(self, language: Language) -> None:
#         ''' Add language to grammar. '''
#         self._languages.append(language)

#     def remove_language(self, name: str) -> None:
#         ''' Remove language from grammar. '''
#         for language in self._languages:
#             if language.get_name() == name:
#                 self._languages.remove(language)
#                 break

#     def __str__(self) -> str:
#         return {
#             'languages': self._languages
#         }.__str__()
