# CATGPT Terminal 1.0.X.X [C] - Local Server 1.0 [C] Flames Labs 20XX
# Developed by: [Your Name]
# Date: [Current Date]

# Import the necessary modules
import os
from openai import OpenAI
import tkinter as tk

# Set the OpenAI API key (keep it secret, keep it safe!)
os.environ["OPENAI_API_KEY"] = "lm-studio"

# Initialize the OpenAI client (let's get this party started!)
client = OpenAI(base_url="http://localhost:1234/v1")

# Define the ChatApp class (where the magic happens!)
class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CATGPT Terminal 1.0.X.X [C] - Local Server 1.0 [C] Flames Labs 20XX")
        self.geometry("800x600")
        self.resizable(False, False)
        self.create_widgets()
        self.init_chat_history()

    def create_widgets(self):
        # Create the chat history text area (for all the juicy conversations!)
        self.chat_history = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create the input frame (where the user types their heart out!)
        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        # Create the user input entry field (let the user speak their mind!)
        self.user_input = tk.Entry(input_frame)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Create the send button (because hitting Enter is too mainstream!)
        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.LEFT, padx=(10, 0))

        # Bind the Enter key to the send_message function (for the lazy folks!)
        self.user_input.bind("<Return>", lambda event: self.send_message())

        # Create the output window (where CATGPT struts its stuff!)
        self.output_window = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED)
        self.output_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def init_chat_history(self):
        # Initialize the chat history with a friendly message (because first impressions matter!)
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "CATGPT: Hello! I'm CATGPT. Share your prompt, and I'll generate code or context showcasing my capabilities!\n\n")
        self.chat_history.configure(state=tk.DISABLED)

    def send_message(self):
        # Get the user's prompt (let's see what they've got!)
        user_prompt = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.update_chat_history(f"User: {user_prompt}\n\n")

        try:
            # Generate a response using the OpenAI API (fingers crossed!)
            completion = client.completions.create(
                model="LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF",
                prompt=f"As CATGPT, research the following prompt:\n{user_prompt}\nGenerate code or context based on the prompt, showcasing the potential of CATGPT in this domain.\nYour final answer should be the generated code or context.",
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ai_output = completion.choices[0].text.strip()
        except Exception as e:
            # Oops, something went wrong! Let the user know (and try to look cool doing it!)
            ai_output = f"Sorry, I encountered an error while processing your prompt: {str(e)}"

        # Update the chat history with CATGPT's response (drum roll, please!)
        self.update_chat_history(f"CATGPT: {ai_output}\n\n")
        self.update_output_window(user_prompt, ai_output)

    def update_chat_history(self, message):
        # Update the chat history with the latest message (because scrolling is so 90s!)
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message)
        self.chat_history.configure(state=tk.DISABLED)
        self.chat_history.see(tk.END)

    def update_output_window(self, user_prompt, ai_output):
        # Update the output window with the user's prompt and CATGPT's output (ta-da!)
        self.output_window.configure(state=tk.NORMAL)
        self.output_window.delete('1.0', tk.END)
        self.output_window.insert(tk.END, f"User Prompt:\n{user_prompt}\n\nCATGPT Output:\n{ai_output}")
        self.output_window.configure(state=tk.DISABLED)

# Let's get this show on the road!
if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
