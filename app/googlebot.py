# import google.generativeai as genai
# # import os
# # from dotenv import load_dotenv

# # Load API key securely
# # load_dotenv()
# genai.configure(api_key="AIzaSyAIcZAS8b3VQBdhDrEWXSdeef5GmBoCu2Q")

# # Initialize the chatbot model
# model = genai.GenerativeModel("gemini-pro")

# def chat_with_gemini(prompt):
#     response = model.generate_content(prompt)
#     return response.text

# # Interactive chat loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["quit", "exit", "bye"]:
#         print("Chatbot: Goodbye!")
#         break
#     response = chat_with_gemini(user_input)
#     print("Chatbot:", response)


from google import genai

client = genai.Client(api_key="AIzaSyAIcZAS8b3VQBdhDrEWXSdeef5GmBoCu2Q")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=input("Enter : ")
)
print(response.text)