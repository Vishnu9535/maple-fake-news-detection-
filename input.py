from multi_rake import Rake


def get_words():
    text=input("Enter Text")
    return text


def find_words(text):
    rake = Rake()
    keywords = rake.apply(text.lower())
    return keywords
