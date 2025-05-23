def chatbot():
    print("Chatbot: Hello! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I help you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a code, but I'm doing great! Thanks for asking.")
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple chatbot created by a swastik.")
        elif 'help' in user_input:
            print("Chatbot: I can answer simple questions. Try saying hello or ask about me!")
        elif 'bye' in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you try something else?")


chatbot()
