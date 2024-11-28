import random

class DistractorGenerator:
    def __init__(self):
        self.fake_answers = [
            "The moon is green.",
            "The Earth is flat.",
            "The sun is cold.",
            "Birds cannot fly.",
            "Water boils at 0 degrees."
        ]

    def generate_distractors(self, correct_answer):
        # Generate fake distractors for MCQs
        distractors = random.sample(self.fake_answers, 3)
        distractors.append(correct_answer)  # Ensure correct answer is included
        random.shuffle(distractors)
        return distractors
