import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"quit",
        ["Bye-bye! Take care."]
    ]
]
chatbot = Chat(pairs, reflections)
print("Hello! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    response = chatbot.respond(user_input)
    print(response)
