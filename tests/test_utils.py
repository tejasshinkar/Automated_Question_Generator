import unittest
from utils.preprocess import Preprocessor
from utils.summarizer import Summarizer

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.text = "Artificial Intelligence (AI) is the simulation of human intelligence in machines."
        self.preprocessor = Preprocessor(self.text)
        self.summarizer = Summarizer(self.text)

    def test_clean_text(self):
        cleaned_text = self.preprocessor.clean_text()
        self.assertNotIn('(', cleaned_text, "Text cleaning failed. Unwanted characters still present.")
    
    def test_tokenize_text(self):
        tokens = self.preprocessor.tokenize_text()
        self.assertGreater(len(tokens), 0, "Text tokenization failed.")
    
    def test_remove_stopwords(self):
        words = self.preprocessor.remove_stopwords()
        self.assertNotIn('is', words, "Stopword removal failed.")

    def test_summarize(self):
        summary = self.summarizer.summarize(num_sentences=1)
        self.assertGreater(len(summary.split()), 0, "Text summarization failed.")
    
if __name__ == "__main__":
    unittest.main()
