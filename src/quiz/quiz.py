# quiz.py
from string import ascii_lowercase
import random
import pathlib
import tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "QUESTIONS.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())


def main():
    """
    1. call preprocess() for the list of questions and their alternatives
    2. call main_process() with each question and labeled shuffled alternatives
    in the list of questions
    3. increment num_correct by the value returned by main_process()
    3. Display record of correct alternatives after all questions asked
    """
    questions = preprocess(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

    num_correct = 0
    for index_label, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {index_label}:")
        num_correct += main_process(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {len(questions)} questions")


def preprocess(questions, num_questions):
    """
    1. Decide how many questions will be presented to the user
    2. return to main() with the list of questions and their
        alternatives
    """
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def main_process(question, alternatives):
    """
    1. remember this iteration's question's correct alternative
    2. shuffle the alternatives
    3. present the question and shuffled alternatives to user
    4. compare the alternative string chosen by the user via
        alternative label to the correct alternative
    5. return to main() with the value with which to increment
        num_correct
    """
    correct_alternative = alternatives[0]
    shuffled_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = main_loop(question, shuffled_alternatives)
    if answer == correct_alternative:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_alternative!r}, not {answer!r}")
        return 0


def main_loop(question, alternatives):
    """
    1. display the question and labeled shuffled alternatives to user
    2. return to main_process() with the alternative string for the
        acceptable answer_label
    """
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for labeled_index, alternative in labeled_alternatives.items():
        print(f"  {labeled_index}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


if __name__ == "__main__":
    main()
