# quiz.py
from string import ascii_lowercase
import random
import pathlib
import tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "QUESTIONS.toml"


def main():
    """
    1. call preprocess() for the list of dictionaries
    2. call main_process() with each dictionary
    3. increment num_correct by the value returned by main_process()
    3. Display record of correct alternatives after all questions asked
    """
    questions = preprocess(QUESTIONS_PATH,
                           num_questions=NUM_QUESTIONS_PER_QUIZ)

    num_correct = 0
    for index_label, question in enumerate(questions, start=1):
        print(f"\nQuestion {index_label}:")
        num_correct += main_process(question)

    print(f"\nYou got {num_correct} correct out of {len(questions)} questions")


def preprocess(path, num_questions):
    """
    1. Retrieve the list of dictionaries assigned to the key "questions"
    1. Decide how many questions will be presented to the user
    2. return to main() with a list of dictionaries
    """
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)


def main_process(question):
    """
    1. remember this iteration's question's correct alternative
    2. shuffle the alternatives
    3. present the question and shuffled alternatives to user
    4. compare the alternative string chosen by the user via
        alternative label to the correct alternative
    5. return to main() with the value with which to increment
        num_correct
    """
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    shuffled_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = main_loop(
        question=question["question"],
        alternatives=shuffled_alternatives,
        num_choices=len(correct_answers),
    )
    if set(answers) == set(correct_answers):
        print("⭐ Correct! ⭐")
        return 1
    else:
        # adjust error message grammar based on number of expected correct
        # answers
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))
        return 0


def main_loop(question, alternatives, num_choices):
    """
    1. Display the question and labeled shuffled alternatives to user
    2. Display grammar presented to user based on multiple choice or not
    3. Be lenient with user input
        - if duplicate correct answer given, keep only one
        - allow for irregular spacing in input by removing commas and adding
        back in

    4. Handle the incorrect number of choices given
        - choose the correct grammar for the incorrect number of answers given
        - rerun the loop
    5. Handle  any evaluate to True, a choice input not in list of
    alternatives, tell the user which input is invalid, which alternatives to
    choose from, and rerun the loop
    6. Return to main_process() with a list of correct answers
    """
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for labeled_index, alternative in labeled_alternatives.items():
        print(f"  {labeled_index}) {alternative}")

    # rerun input prompt loop until return statement reached
    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle incorrect quantity of answers input
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        # Handle incorrect character(s) given as answer
        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]


if __name__ == "__main__":
    main()
