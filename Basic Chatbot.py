import tkinter as tk
from datetime import datetime

# Function to send message
def send_message(event=None):
    user_msg = entry.get()
    entry.delete(0, tk.END)

    if user_msg.strip() == "":
        return

    time = datetime.now().strftime("%H:%M")

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You ({time}): {user_msg}\n", "user")

    user_msg_lower = user_msg.lower()

    # Bot responses
    if "hello" in user_msg_lower:
        bot_reply = "Hi! 😊"
    elif "how are you" in user_msg_lower:
        bot_reply = "I'm doing great! How about you?"
    elif "your name" in user_msg_lower:
        bot_reply = "I am your Python Chatbot 🤖"
    elif "bye" in user_msg_lower:
        bot_reply = "Goodbye! Have a nice day!"
    else:
        bot_reply = "Hmm... I don't understand that."

    # Simulate typing delay
    root.after(500, lambda: display_bot_reply(bot_reply, time))

def display_bot_reply(reply, time):
    chat_box.insert(tk.END, f"Bot ({time}): {reply}\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

# Clear chat
def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete(1.0, tk.END)
    chat_box.config(state=tk.DISABLED)

# Window
root = tk.Tk()
root.title("Advanced Chatbot 🤖")
root.geometry("450x550")
root.configure(bg="#F0F0F0")

# Chat box with scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Text(frame, width=50, height=20, yscrollcommand=scrollbar.set, state=tk.DISABLED)
chat_box.pack()

scrollbar.config(command=chat_box.yview)

# Styling text
chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="green")

# Entry box
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)
entry.bind("<Return>", send_message)  # Press Enter to send

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

send_btn = tk.Button(btn_frame, text="Send", command=send_message, bg="#4CAF50", fg="white")
send_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear Chat", command=clear_chat, bg="#f44336", fg="white")
clear_btn.grid(row=0, column=1, padx=5)

root.mainloop()
