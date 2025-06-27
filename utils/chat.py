from openai import OpenAI
from dotenv import load_dotenv
import sys
import os
from utils.typewriter import typewriter
from utils.spinner import Spinner


class Chat:

    def __init__(self, model="gpt-4o-mini", message=""):
        """
        Initialize the Chat class:
        - create OpenAI client,
        - create spinner,
        - set model name,
        - set up message storage,
        - load environment variables.
        """

        # OpenAI client for generating responses
        self.client = OpenAI()
        # Spinner for console effects
        self.spinner = Spinner(message=message)
        # Model to use for chat
        self.model = model
        # List to store conversation history
        self.messages = []
        # Load environment variables
        load_dotenv()

    def __message(self, role, type, content):
        """
        Build a single message dictionary for the OpenAI API.
        Args:
            role: The sender's role (e.g., "user")
            type: The content type (e.g., "text")
            content: The message itself
        Returns:
            dict: Message ready for OpenAI API
        """
        return {
            "role": role,
            "content": [
                {
                    "type": type,
                    "text": content,
                },
            ],
        }

    def __request(self):
        """
        Send all conversation history to the OpenAI API and receive the next message.
        Returns:
            str: Content of the assistant reply
        Exits if the API call fails or returns nothing.
        """
        try:
            responce = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
            )
        except Exception as e:
            typewriter(f"Error: {e}")
            sys.exit()

        # If a valid response is received, save it and return the content
        if responce.choices[0].message:
            message = responce.choices[0].message
            self.messages.append(message)

            # Return response content
            return message.content

        # If not, notify user and exit
        typewriter("No responce from OpenAI, try later.")
        sys.exit()

    def __run(self):
        """
        Run the spinner while waiting for chat response.
        Returns:
            str: The assistant's message content.
        """
        self.spinner.start()

        # Get assistant response
        content = self.__request()
        self.spinner.stop()
        return content

    def __welcome(self):
        """
        Show a welcome and instructions message at start of chat.
        """
        typewriter(
            "Hi, this is test console GPT chat\nI use model gpt-4o-mini.\n"
            "You can ask something and I will try give you an answer.\n"
            "I use MD format for the response.\nPlease, pay attention to this point.\n"
            "For exit command type 'q'.",
            sleep=0.001,
            style="bold green",
        )

    def __console_clear(self):
        """
        Clears the console screen (cross-platform).
        """
        if os.name == "nt":
            # For Windows
            os.system("cls")
        else:
            # For macOS/Linux
            os.system("clear")

    def chat(self):
        """
        Start the chat loop: show welcome, handle user input,
        exchange messages with assistant, and display everything.
        """

        # Clear screen for a clean start
        self.__console_clear()

        # Print chat instructions
        self.__welcome()

        while True:
            # Prompt user for input
            input_user = input("Me: ")

            # If user wants to quit, print goodbye and break the loop
            if input_user == "q":
                typewriter("Be in touch, see you!", sleep=0.001, style="bold green")
                break
            else:
                # Store user message
                self.messages.append(self.__message("user", "text", input_user))

                # Get assistant's reply (with spinner)
                content = self.__run()

                # Show assistant's answer
                typewriter("GPT: " + content, sleep=0.001, style="green")
