import re
import nltk
from nltk.tokenize import word_tokenize

class Preprocessor:
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        # Remove unwanted characters (non-alphanumeric)
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return cleaned_text

    def tokenize_text(self):
        # Tokenize the text into words
        words = word_tokenize(self.text)
        return words

    def remove_stopwords(self):
        # Remove common stopwords
        stopwords = nltk.corpus.stopwords.words('english')
        words = self.tokenize_text()
        filtered_words = [word for word in words if word.lower() not in stopwords]
        return filtered_words
