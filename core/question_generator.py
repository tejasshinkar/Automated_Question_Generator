import random
from nltk import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

class QuestionGenerator:
    def __init__(self, text):
        self.text = text
        self.sentences = sent_tokenize(text)

    def generate_questions(self, question_type='mcq'):
        questions = []
        if question_type == 'mcq':
            questions = self.generate_mcq()
        elif question_type == 'true_or_false':
            questions = self.generate_true_or_false()
        elif question_type == 'descriptive':
            questions = self.generate_descriptive()
        return questions

    def generate_mcq(self):
        questions = []
        for sentence in self.sentences:
            # Extract key noun or verb for MCQ
            words = word_tokenize(sentence)
            tagged_words = pos_tag(words)
            noun_phrases = [word for word, tag in tagged_words if tag in ['NN', 'NNS', 'NNP']]
            if noun_phrases:
                question = f"What is related to {random.choice(noun_phrases)}?"
                options = [f"Option {i}" for i in range(1, 5)]
                questions.append((question, options))
        return questions

    def generate_true_or_false(self):
        questions = []
        for sentence in self.sentences:
            if len(sentence.split()) > 5:  # Avoid very short sentences
                question = f"Is the statement true or false? {sentence}"
                questions.append((question, ['True', 'False']))
        return questions

    def generate_descriptive(self):
        questions = []
        for sentence in self.sentences:
            question = f"Describe in your own words: {sentence}"
            questions.append((question,))
        return questions

