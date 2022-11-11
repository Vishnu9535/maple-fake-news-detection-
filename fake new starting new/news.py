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
    search_words=""
    for x in keywords:
        search_words=search_words+x[0]+" "
    print(search_words)
    googlenews.search(search_words)
    result=googlenews.result()
    print(result[0]['link'])

get_search_results(keywords)
