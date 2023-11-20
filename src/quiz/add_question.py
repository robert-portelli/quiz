import pathlib
import tomllib
from string import ascii_lowercase
from quiz import main_loop

QUESTIONS_PATH = pathlib.Path(__file__).parent / "QUESTIONS.toml"
TRIVIA_TOML = tomllib.loads(QUESTIONS_PATH.read_text())

#topics = dict(zip(ascii_lowercase, TRIVIA_TOML.keys()))

def main():
    #topic_path = toml_path_to_topic()
    #new_question = create_question()
    #append_new_question = write_to_toml(topic_path, new_question)
    pass

def create_question():
    """
    create a dictionary with items {
        'question': str,
        'answers': List,
        'alternatives': List,
        'hint': None
        'explanation': None
    }
    """
    question = input("Enter your question prompt: ")
    answers = input("Enter one correct answer at a time: ")
    alternatives = input("Enter one alternative at a time: ")
    hint = input("Offer a hint? -enter to skip")
    explanation = input("Offer an explanation? - enter to skip")
    return {
        "question": question,
        "answers": answers,
        "alternatives": alternatives,
        "hint": hint,
        "explanation": explanation
    }



def toml_path_to_topic():
    """
    Return the path to a list of dictionaries where:
        each dictionary is of keys: question, answers, alternatives,
        hint, explanation.
    """
    topic_label = main_loop(
        question="Which topic do you want to add a question to",
        alternatives=TRIVIA_TOML.keys(),
    )[0]
    # append new question dictionaries here
    # THIS IS "TOPIC QUESTIONS PATH"
    return TRIVIA_TOML[topic_label]['questions']


if __name__ == "__main__":
    topic_path = toml_path_to_topic()
    new_question = create_question()
