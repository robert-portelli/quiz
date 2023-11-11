#quiz.py
from string import ascii_lowercase
import random

NUM_QUESTIONS_PER_QUIZ = 5

QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781",
        "1771",
        "1871",
        "1881",
    ],
    "Which built-in function can get information from the user": [
        "input",
        "get",
        "print",
        "write",
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for",
        "while",
        "each",
        "loop",
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort",
        "Quicksort",
        "Merge sort",
        "Bubble sort",
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None",
        "key",
        "True",
        "False",
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ],
    "Which version of Python is the first with TOML support built in": [
        "3.11",
        "3.9",
        "3.10",
        "3.12",
    ],
    "What's the name of the list-like data structure in TOML": [
        "Array",
        "List",
        "Sequence",
        "Set",
    ],
}


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
