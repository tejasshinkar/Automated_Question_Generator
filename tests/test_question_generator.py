import unittest
from core.question_generator import QuestionGenerator

class TestQuestionGenerator(unittest.TestCase):
    def setUp(self):
        self.text = "Artificial Intelligence (AI) is the simulation of human intelligence in machines."
        self.generator = QuestionGenerator(self.text)

    def test_generate_mcq(self):
        questions = self.generator.generate_questions(question_type='mcq')
        self.assertTrue(len(questions) > 0, "MCQ question generation failed.")
        self.assertIn('Options', questions[0][1], "MCQ options are missing.")

    def test_generate_true_or_false(self):
        questions = self.generator.generate_questions(question_type='true_or_false')
        self.assertTrue(len(questions) > 0, "True or False question generation failed.")
        self.assertTrue(questions[0][1] in ['True', 'False'], "True/False option is incorrect.")

    def test_generate_descriptive(self):
        questions = self.generator.generate_questions(question_type='descriptive')
        self.assertTrue(len(questions) > 0, "Descriptive question generation failed.")
        self.assertIsInstance(questions[0][1], str, "Descriptive answer should be a string.")
    
if __name__ == "__main__":
    unittest.main()
