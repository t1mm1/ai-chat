# Console Chatbot (Python, GPT-4o-mini)

A simple and interactive command-line chatbot written in Python, powered by the OpenAI GPT-4o-mini API.

## Requirements

- Python 3.7+
- [pipenv](https://pipenv.pypa.io/) for dependency management
- OpenAI API key

## Features

- Answers questions using OpenAI GPT-4o-mini
- Stores chat history in memory
- Typewriter animation in the console
- Spinner animation while waiting for OpenAI response
- Command `q` to exit chat

## Project Structure

```
project/
├── .env.sample
├── .gitignore
├── main.py # Main entry point
├── Pipfile # Python dependencies
└── utils/
    ├── chat.py # Chat class implementation
    ├── spinner.py # Spinner animation
    └── typewriter.py # Typewriter text effect
```

## Installation

1. **Install pipenv**
   ```
   pip install pipenv
   ```

2. **Install dependencies using pipenv:**
   ```
   pipenv install
   ```

3. **Create `.env` from `.env.sample` and set your `OPENAI_API_KEY`:**
   ```
   cp .env.sample .env
   ```

   Then edit `.env` and add your API key:
   OPENAI_API_KEY=your-openai-key

4. **Run the chatbot:**
   ```
   pipenv run python main.py
   ```

## How to Use the Chat

- Once the chat is started, you will see a welcome message and instructions in the console.
- Type your question or message and press Enter.
- Wait for the assistant’s reply (a spinner animation will be shown).
- The assistant’s response is printed with a typewriter animation.
- Continue the conversation by entering new messages.
- To exit the chat, type `q` and press Enter. You will see a goodbye message.

## Usage

- The chat will display a welcome message and wait for your input in the console.
- Enter your questions or prompts and press Enter.
- Type q and press Enter to exit the chat.

## Main Files

- `main.py` — main script entrypoint
- `utils/chat.py` — Chat class
- `utils/spinner.py` — spinner animation
- `utils/typewriter.py` — typewriter animation

## How to use the Chat class

You can use the `Chat` class directly in your own Python scripts.

### Example

You can use the `Chat` class directly in your own Python scripts. Example:

```python
from utils.chat import Chat

# Create an instance of Chat
chat = Chat()

# Start the chat loop (console interaction begins)
chat.chat()
```

### Constructor Parameters

You can change the model and the spinner's message when creating the class instance.
Note: Only text-based models are supported. By default, you can omit these variables.

- `model` (str): The OpenAI GPT model to use (text models only). Default is "gpt-4o-mini".
- `message` (str): Spinner message displayed while waiting for a response. Default is an empty string.

### Example with parameters:

```python
from utils.chat import Chat

# Create an instance of Chat
chat = Chat(model="gpt-4", message="Thinking")

# Start the chat loop (console interaction begins)
chat.chat()
```

You can change model and message for spinner. But remember, you can use text models only. By default you can keep these variables empty.

## License

MIT
