from data import question_data


class Question:
    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer


class QuizGame:
    def __init__(self):
        self.question_number = 0
        self.question_bank = []
        for question in question_data:
            question_text = question["text"]
            question_answer = question["answer"]
            self.question_bank.append(Question(question_text, question_answer))
        self.correct_answers = 0

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        user_answer = str(input("Q{}. {} (True/False) \n".format(self.question_number + 1, current_question.text)))
        if user_answer == current_question.answer:
            print("Correct answer!")
            self.correct_answers += 1
        else:
            print("Wrong answer!")
        print("Score: {}/{}".format(self.correct_answers, self.question_number + 1))
        self.question_number += 1

    def has_more_questions(self):
        if self.question_number < len(self.question_bank):
            return True
        else:
            return False

    def game_score(self):
        print("You scored {}%".format(100 * self.correct_answers / self.question_number))
