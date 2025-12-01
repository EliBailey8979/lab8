from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.text import Text
from rich.theme import Theme


# -----------------------------
# Rich Theme (consistent colors)
# -----------------------------
game_theme = Theme({
    "intro": "bold bright_white",
    "prompt": "cyan",
    "path": "bright_green",
    "event": "bold magenta",
    "warning": "bold red",
})

console = Console(theme=game_theme)


# -----------------------------
# Game Logic (unchanged API)
# -----------------------------
def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."


def left_path(event):
    return "You walk left. " + event


def right_path(event):
    return "You walk right. " + event


# -----------------------------
# Rich-rendered story display
# -----------------------------
def display_intro():
    title = Text("YOU WAKE UP IN A DARK FOREST", style="intro")
    console.print(title)
    console.print("The air is cold and silent.\n", style="intro")


def display_result(text):
    """
    Rich formatting for the result text.
    Tests compare strings, so we only format the printed output,
    not the returned value from step().
    """
    if "walk left" in text:
        console.print(text.replace("You walk left.", "[path]You walk left.[/path]"), style="event")
    elif "walk right" in text:
        console.print(text.replace("You walk right.", "[path]You walk right.[/path]"), style="event")
    else:
        console.print(text, style="warning")


# -----------------------------
# Main runtime (still works)
# -----------------------------
if __name__ == "__main__":
    events = read_events_from_file("events.txt")

    display_intro()

    while True:
        choice = console.input("[prompt][bold]Which direction do you choose? [/bold](left/right/exit): [/prompt]").strip().lower()

        if choice == "exit":
            console.print("\nFarewell, traveler.", style="intro")
            break

        result = step(choice, events)
        display_result(result)
