
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

![GH Actions](https://github.com/robert-portelli/NewLibrary/actions/workflows/main.yaml/badge.svg)

![Black](https://img.shields.io/badge/code%20style-black-000000.svg)

![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Quiz Game

A simple command-line quiz game.

This script reads questions from a TOML file, allows the user to choose a topic,
and quizzes the user with a set number of random questions from that topic.

## Requirements

- Python 3.7 or later
- The `tomllib` library for TOML parsing

Install `tomllib` with:

```bash
pip install toml
```

## Usage

1. Clone the repo
```bash
git clone https://github.com/robert-portelli/quiz
```

2. Navigate to the project directory
```
cd quiz
```

3. Run the quiz
```bash
python quiz.py
```

## How to Play
The script will prompt you to choose a topic from the available options.
You will then be asked a set number of random questions from the chosen topic.
Answer the questions as prompted.
Your performance will be displayed at the end of the quiz.

## Questions File
Questions are stored in a TOML file (QUESTIONS.toml). You can customize this file by adding your own questions and topics.

Example structure:
```toml
[topic_name]
label = "Topic Name"

[[topic_name.questions]]
questions = "What is the capital of France?",
answers = ["Paris"],
alternatives = ["London", "Berlin"],
explanation = "Paris is the capital of France."
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/robert-portelli/quiz/blob/main/LICENSE) file for details.
