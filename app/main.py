import sys
from core.question_generator import QuestionGenerator
from core.distractor_generator import DistractorGenerator
from core.text_analyzer import TextAnalyzer
from utils.summarizer import Summarizer
from utils.preprocess import Preprocessor
from utils.logger import Logger

class QuestionGenerationApp:
    def __init__(self, text):
        self.text = text
        self.logger = Logger()

    def generate_questions(self, question_type='mcq'):
        try:
            # Text preprocessing
            preprocessor = Preprocessor(self.text)
            cleaned_text = preprocessor.clean_text()
            preprocessed_text = preprocessor.remove_stopwords()

            # Summarize text if needed (optional)
            summarizer = Summarizer(self.text)
            summary = summarizer.summarize()

            # Generate questions based on preprocessed text
            question_generator = QuestionGenerator(cleaned_text)
            questions = question_generator.generate_questions(question_type)

            self.logger.log(f"Generated {len(questions)} questions of type '{question_type}'.")

            # Displaying the questions
            for idx, (question, options) in enumerate(questions, start=1):
                print(f"Q{idx}: {question}")
                if options:
                    print("Options: " + ", ".join(options))
                print()
        except Exception as e:
            self.logger.log_error(f"Error generating questions: {e}")
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Sample text input (can be modified by user)
    input_text = """
    Artificial Intelligence (AI) is the simulation of human intelligence in machines
    that are programmed to think like humans and mimic their actions. The term may also
    be applied to any machine that exhibits traits associated with a human mind such as
    learning and problem-solving.
    """

    # Instantiating the app
    app = QuestionGenerationApp(input_text)

    # Generating questions based on user's choice (default: 'mcq')
    question_type = sys.argv[1] if len(sys.argv) > 1 else 'mcq'
    app.generate_questions(question_type)
