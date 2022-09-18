"""
Frequency-driven keyword extraction starter
"""
import json
from pathlib import Path


if __name__ == "__main__":

    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH = ASSETS_PATH / 'Дюймовочка.txt'
    with open(TARGET_TEXT_PATH, 'r', encoding='utf-8') as file:
        target_text = file.read()

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as file:
        stop_words = file.read().split('\n')

    # reading IDF scores for all tokens in the corpus of H.C. Andersen tales
    IDF_PATH = ASSETS_PATH / 'IDF.json'
    with open(IDF_PATH, 'r', encoding='utf-8') as file:
        idf = json.load(file)

    # reading frequencies for all tokens in the corpus of H.C. Andersen tales
    CORPUS_FREQ_PATH = ASSETS_PATH / 'corpus_frequencies.json'
    with open(CORPUS_FREQ_PATH, 'r', encoding='utf-8') as file:
        corpus_freqs = json.load(file)


    def clean_and_tokenize(text: str) -> Optional[list[str]]:
        clean1 = text.lower().replace(':', '').replace('!', '').replace('...', '').replace('!..', '').replace('?..', '').replace('.', '').replace(',', '').replace('?', '').replace(';', '').replace('-', '')
        clean2 = clean1.split()


        return clean2

    clean_list = clean_and_tokenize(target_text)
    print(clean_list)


    def remove_stop_words(tokens: list[str], stop_words: list[str]) -> Optional[list[str]]:
        for word in stop_words:
            while word in tokens:
                tokens.remove(word)

        return tokens


    delet_list = remove_stop_words(clean_list, stop_words)
    print(delet_list)

    RESULT = None
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Keywords are not extracted'
