# quiz.py
from string import ascii_lowercase

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
}

for i, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {i}: {question}?")
    CORRECT_ANSWER = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == CORRECT_ANSWER:
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {CORRECT_ANSWER!r}, not {answer!r}")
