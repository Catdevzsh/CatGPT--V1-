import os
from openai import OpenAI
import tkinter as tk

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "lm-studio"

# Initialize OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1")

class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Assistant 1.0 [Beta] - Local Server 1.0 [C] Flames Labs 20XX")
        self.geometry("600x400")
        self.resizable(False, False)
        self.create_widgets()
        self.init_chat_history()

    def create_widgets(self):
        self.chat_history = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        self.user_input = tk.Entry(input_frame)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.LEFT, padx=(10, 0))

        self.user_input.bind("<Return>", lambda event: self.send_message())

    def init_chat_history(self):
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "AI Assistant: Hello! I'm an AI assistant. Please provide a prompt and I will generate relevant output.\n\n")
        self.chat_history.configure(state=tk.DISABLED)

    def send_message(self):
        user_prompt = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.update_chat_history(f"User Prompt: {user_prompt}\n\n")

        completion = client.completions.create(
            model="LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF",
            prompt=user_prompt
        )
        ai_output = completion.choices[0].text

        self.update_chat_history(f"AI Assistant Output: {ai_output}\n\n")

    def update_chat_history(self, message):
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message)
        self.chat_history.configure(state=tk.DISABLED)
        self.chat_history.see(tk.END)

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
