import nltk
from nltk.tokenize import sent_tokenize

class Summarizer:
    def __init__(self, text):
        self.text = text
        self.sentences = sent_tokenize(text)

    def summarize(self, num_sentences=3):
        # Simple summarization by extracting the first few sentences
        summary = " ".join(self.sentences[:num_sentences])
        return summary
