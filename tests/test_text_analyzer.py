import unittest
from core.text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.text = "Artificial Intelligence (AI) is the simulation of human intelligence."
        self.analyzer = TextAnalyzer(self.text)

    def test_extract_keywords(self):
        keywords = self.analyzer.extract_keywords()
        self.assertTrue(len(keywords) > 0, "Keyword extraction failed.")

    def test_analyze_syntax(self):
        syntax_analysis = self.analyzer.analyze_syntax()
        self.assertIn('NN', syntax_analysis, "Syntax analysis failed. Expected noun phrases.")
    
if __name__ == "__main__":
    unittest.main()
