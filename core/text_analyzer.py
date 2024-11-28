import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.sentences = nltk.sent_tokenize(text)

    def extract_named_entities(self):
        named_entities = []
        for sentence in self.sentences:
            words = word_tokenize(sentence)
            tagged_words = pos_tag(words)
            tree = ne_chunk(tagged_words)
            for subtree in tree:
                if isinstance(subtree, nltk.Tree):
                    entity = " ".join([word for word, tag in subtree])
                    named_entities.append(entity)
        return named_entities

    def extract_keywords(self):
        keywords = []
        for sentence in self.sentences:
            words = word_tokenize(sentence)
            tagged_words = pos_tag(words)
            keywords += [word for word, tag in tagged_words if tag in ['NN', 'NNS', 'NNP', 'JJ']]
        return keywords
