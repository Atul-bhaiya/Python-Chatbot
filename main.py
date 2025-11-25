import os
import google.generativeai as genai

# --- Configuration Section ---
try:
    API_KEY = os.environ['GEMINI_API_KEY']
    genai.configure(api_key=API_KEY)
except KeyError:
    print("❌ Error: The 'GEMINI_API_KEY' environment variable is not set.")
    print("Please set the environment variable and run the script again.")
    print("See the explanation below on how to set the environment variable.")
    exit() # Stop the script if the key isn't found

# --- Model and Main Loop ---
model = genai.GenerativeModel("gemini-2.0-flash")

print("🤖 Bhaiya Ji GPT (Type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Generate content using the model
    try:
        response = model.generate_content(user_input)
        print("ChatBot:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
        