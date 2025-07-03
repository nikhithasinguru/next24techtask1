import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext


pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there!"]],
    [r"what is your name?", ["I'm a Python Chatbot."]],
    [r"how are you?", ["I'm doing great. How about you?"]],
    [r"(.*) your name?", ["My name is PyBot."]],
    [r"(.*) help (.*)", ["Sure, I can help. Please tell me your issue."]],
    [r"(.*) (location|city)", ["I'm in the cloud, everywhere!"]],
    [r"bye|exit|quit", ["Goodbye! Have a nice day."]],
    [r"(.*)", ["Sorry, I didn't understand that. Can you rephrase?"]],
]


chatbot = Chat(pairs, reflections)


def send_message(event=None):
    user_input = user_entry.get().strip()
    if user_input == "":
        return
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_input + "\n", "user")
    response = chatbot.respond(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n", "bot")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)
    user_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Chatbot - PyBot")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#eef")


chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 10))
chat_area.place(x=10, y=10, width=380, height=400)
chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")
chat_area.config(state=tk.DISABLED)


user_entry = tk.Entry(root, font=("Segoe UI", 11))
user_entry.place(x=10, y=420, width=280, height=30)
user_entry.bind("<Return>", send_message)  # Trigger on Enter key


send_btn = tk.Button(root, text="Send", bg="#007acc", fg="white", font=("Segoe UI", 10), command=send_message)
send_btn.place(x=300, y=420, width=90, height=30)


root.mainloop()
