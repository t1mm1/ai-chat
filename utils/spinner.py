from rich.console import Console
from dotenv import load_dotenv
import sys
import threading
import time

# Load environment variables from .env file, if present
load_dotenv()


class Spinner:
    def __init__(self, message="In process"):
        """
        Initialize the Spinner with an optional message
        """
        self.running = True
        self.thread = None
        self.message = message
        self.console = Console()

    def start(self):
        """
        Start the spinner animation in a separate thread
        """

        def run():
            self.running = True
            dots = ""
            while self.running is True:
                # Create a string with up to 3 dots after the message
                dots = dots + "." if len(dots) < 3 else ""
                output = f"\r{self.message}{dots}{' '*(3-len(dots))}"
                sys.stdout.write(output)
                sys.stdout.flush()
                time.sleep(0.5)
                if len(dots) >= 3:
                    dots = ""
            # Clear the line when stopping
            sys.stdout.write("\r" + " " * (len(self.message) + 3) + "\r")

        # Create and start the thread for the spinner animation
        self.thread = threading.Thread(target=run)
        self.thread.start()

    def stop(self):
        """
        Stop the spinner animation and wait for the thread to finish
        """
        self.running = False
        self.thread.join()
