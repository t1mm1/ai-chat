from rich.console import Console
import time


def typewriter(text, sleep=0.01, style=""):
    """
    Prints text to the console one character at a time,
    simulating a typewriter effect with optional style.

    Args:
        text (str): The string to print.
        sleep (float): Delay in seconds between each character (default: 0.01).
        style (str): Optional Rich style for the text (e.g. "bold red").
    """

    # Create a Rich Console instance for styled output
    console = Console()

    for char in text:
        # Print each character with the specified style and no new line
        console.print(char, end="", style=style, soft_wrap=True, markup=True)
        # Pause to create the typewriter effect
        time.sleep(sleep)

    # Print a new line at the end
    console.print("\n")
