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
    questions = preprocess(
        QUESTIONS_PATH,
        num_questions=NUM_QUESTIONS_PER_QUIZ
        )

    num_correct = 0
    for index_label, question in enumerate(questions, start=1):
        print(f"\nQuestion {index_label}:")
        num_correct += main_process(question)

    print(f"\nYou got {num_correct} correct out of {len(questions)} questions")


def preprocess(path, num_questions):
    """
    1. Read and parse the entire toml
    1. for each global key, create a dictionary from its values
    2. prompt the user to choose from the dictionary keys, i.e. topics
    4. Choose the first element from a list of one string
    5. assign all the questions for that topic
    6. decide the number of questions to be asked
    7. return to main() with a random sample of questions
    """
    trivia_toml = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in trivia_toml.values()
    }
    topic_label = main_loop(
        question="Which topic do you want to be quizzed about",
        alternatives=sorted(topics),
    )[0]

    questions = topics[topic_label]
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
        hint=question.get("hint"),
    )

    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        # adjust error message grammar based on number of expected correct
        # answers
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))

    # display a message after the input answer is judged
    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    # performing an action after judging answer regardless of correctness
    # means you can't return inside the if ...  else block any longer.
    return 1 if correct else 0


def main_loop(question, alternatives, num_choices=1, hint=None):
    """
    1. Display the question to the user
    2. Check if hint is not None, create an index label "?" assigned to
        "Hint"
    3. Display all alterative labels with their values to the user
    4. Display grammar presented to user based on multiple choice or not
    5. Be lenient with user input
        - if duplicate correct answer given, keep only one
        - allow for irregular spacing in input by removing commas and adding
        back in
    6. Handle the presence of Hint not None
    7. Handle the incorrect number of choices given
        - choose the correct grammar for the incorrect number of answers given
        - rerun the loop
    8. Handle  any evaluate to True, a choice input not in list of
    alternatives, tell the user which input is invalid, which alternatives to
    choose from, and rerun the loop
    9. Return to main_process() with a list of correct answers
    """
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    # check if hint not None, assign a label "?" to the value "Hint"
    if hint:
        labeled_alternatives["?"] = "Hint"

    for labeled_index, alternative in labeled_alternatives.items():
        print(f"  {labeled_index}) {alternative}")

    # rerun input prompt loop until return statement reached
    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hint not None and "?" given as answer,
        #  i.e user wants to see hint
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle incorrect quantity of answers input
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        # Handle incorrect character(s) given as answer
        if any(
            (invalid := answer)
            not in labeled_alternatives
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
