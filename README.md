Bhaiya Ji GPT — Gemini AI Powered Chatbot
A simple Python-based command-line chatbot built using Google Gemini API.
This project demonstrates how to safely use AI APIs in Python without exposing your secret API key in code.

📌 Features
✔️ Conversational AI using Gemini 2.0 Flash
✔️ Secure API handling using Environment Variables
✔️ Clean & beginner-friendly Python code
✔️ Error handling for missing API keys
✔️ Easy to customize and extend

🔐 Why Environment Variables?
Your API key is confidential.
This project uses:
API_KEY = os.environ['GEMINI_API_KEY']

So your key stays hidden in your system, not in GitHub.
Anyone who wants to run this project simply adds their own API key as an environment variable.

🚀 How to Run the Project
1. Install dependencies
pip install google-generativeai python-dotenv

2. Set your API key
🔹 Windows (CMD):
setx GEMINI_API_KEY "your_api_key_here"

🔹 Mac / Linux (Terminal):
export GEMINI_API_KEY="your_api_key_here"

Restart your terminal.

3. Run the chatbot
python main.py


🧠 How It Works
Your script automatically:


Loads the Gemini API key from system environment


Configures the Gemini client


Starts a chat loop


Sends your message to the model


Prints the response



🗂️ Project Structure
ChatBot/
│── main.py
│── README.md
│── requirements.txt


📌 Note for Developers
If you copy this project:


Add your own GEMINI_API_KEY environment variable


DO NOT put your API key inside the code


DO NOT upload .env files to GitHub

