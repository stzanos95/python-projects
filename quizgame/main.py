from question_model import QuizGame


def main():
    game = QuizGame()
    while game.has_more_questions():
        game.next_question()
    game.game_score()


if __name__ == "main":
    main()
