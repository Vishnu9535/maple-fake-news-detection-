from multi_rake import Rake
from GoogleNews import GoogleNews
# text_input=input('enter the news to search in ')
text_input="modi is precident of india"
def find_words(text_input):
    rake=Rake()
    keywords=rake.apply(text_input.lower())
    print(keywords)
    return keywords
keywords=find_words(text_input)
def get_search_results(keywords):
    googlenews=GoogleNews()
    googlenews.search(*(x[0] for x in keywords))
    googlenews=

get_search_results(keywords)
