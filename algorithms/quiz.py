import typer
import yaml
from pathlib import Path

app = typer.Typer()


@app.command()
def quiz(
    yaml_file: Path = typer.Argument(
        ..., help="Path to the YAML file containing questions and answers."
    )
):
    """
    Read in a YAML file of question: answer pairs and quiz the user.
    """
    try:
        # Load the YAML file
        with open(yaml_file, "r", encoding="utf-8") as f:
            qa_pairs = yaml.safe_load(f)

        if not isinstance(qa_pairs, dict):
            typer.echo(
                "The YAML file should contain key-value pairs. Please check your file format."
            )
            raise typer.Exit(code=1)

        # Iterate over each question-answer pair
        for question, correct_answer in qa_pairs.items():
            while True:
                # Prompt the user for an answer
                user_answer = typer.prompt(f"{question}")

                # Check if the answer matches
                if user_answer.strip().lower() == str(correct_answer).strip().lower():
                    typer.echo("Correct!")
                    break
                else:
                    typer.echo("Incorrect, please try again.")

        typer.echo("Congratulations! You have answered all questions correctly.")

    except FileNotFoundError:
        typer.echo(f"File not found: {yaml_file}")
        raise typer.Exit(code=1)
    except yaml.YAMLError:
        typer.echo("Error parsing the YAML file. Please check its formatting.")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
