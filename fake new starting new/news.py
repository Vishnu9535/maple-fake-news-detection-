from multi_rake import Rake
from GoogleNews import GoogleNews


def get_search_results(keywords):
    googlenews = GoogleNews()
    search_words = ""
    for x in keywords:
        search_words = search_words+x[0]+" "
    googlenews.search(search_words)
    result = googlenews.result()
    return result
