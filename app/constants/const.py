BASE: str = './app/data/'
JSON_URL_I: str = BASE + 'langi.json'
TXT_URL_I: str = BASE + 'langi.txt'



TXT_URLS: list[str] = [
]

def process_txts(start_idx: int = 1, end_idx: int = 1) -> list[str]:
    ''' Function to process txt files. '''
    txt_urls: list[str] = []
    for idx in range(start_idx, end_idx + 1):
        file_url: str = f'lang{idx}.txt'
        txt_urls.append(BASE + file_url)
    return txt_urls

LAMBDA: str = 'λ'
LMD: str = '~'
REGEX = r'\b[A-Z]+[\'’]?|⟨[A-Z]+⟩'
UTF8: str = 'utf-8'
ARROW: str = '⟶'
PIPE: str = '|'
SPACE: str = ' '