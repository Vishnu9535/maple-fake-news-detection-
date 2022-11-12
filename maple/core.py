import spacy

from GoogleNews import GoogleNews
from multi_rake import Rake


def find_words(text):
    rake = Rake()
    keywords = rake.apply(text.lower())
    return keywords


def get_search_results(keywords):
    googlenews = GoogleNews()
    search_words = ""
    for x in keywords:
        search_words = search_words+x[0]+" "
    googlenews.search(search_words)
    result = googlenews.result()
    return result


def paraphrase_wesite(result):
    compare = list()
    compare = []
    for x in result:
        compare.append(str(x['title']))
    return compare


nlp = spacy.load("en_core_web_lg")


def news_prediction(compare, text):
    count = len(compare)

    if count > 10:
        count = 10

    sentence1 = nlp(text)
    for i in range(count):
        sentence2 = nlp(compare[i])
        x = float(sentence1.similarity(sentence2)*100)
        if (x > 82):
            return 1
    return 0


def validate(text: str):
    keywords = find_words(text)
    result = get_search_results(keywords)
    compare = paraphrase_wesite(result)
    state = news_prediction(compare, text)
    return state

