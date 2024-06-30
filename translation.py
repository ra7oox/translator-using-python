import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        src_lang = src_lang_combo.get()
        dest_lang = dest_lang_combo.get()
        text = src_text.get("1.0", tk.END)

        if text.strip():
            translator = Translator()
            translated = translator.translate(text, src=src_lang, dest=dest_lang)
            dest_text.delete("1.0", tk.END)
            dest_text.insert(tk.END, translated.text)
        else:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Translator")


# Create and place the source language combo box
src_lang_label = ttk.Label(root, text="Source Language:")
src_lang_label.grid(row=0, column=0, padx=10, pady=10)

src_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
src_lang_combo.grid(row=0, column=1, padx=10, pady=10)
src_lang_combo.current(21)  # default to English

# Create and place the destination language combo box
dest_lang_label = ttk.Label(root, text="Destination Language:")
dest_lang_label.grid(row=1, column=0, padx=10, pady=10)

dest_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
dest_lang_combo.grid(row=1, column=1, padx=10, pady=10)
dest_lang_combo.current(27)  # default to Spanish

# Create and place the source text box
src_text_label = ttk.Label(root, text="Source Text:")
src_text_label.grid(row=2, column=0, padx=10, pady=10)

src_text = tk.Text(root, height=10, width=40)
src_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create and place the destination text box
dest_text_label = ttk.Label(root, text="Translated Text:")
dest_text_label.grid(row=2, column=2, padx=10, pady=10)

dest_text = tk.Text(root, height=10, width=40)
dest_text.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

# Create and place the translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Run the main loop
root.mainloop()
