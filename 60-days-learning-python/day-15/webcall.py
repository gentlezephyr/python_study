import tkinter as tk
import webbrowser


def on_enter(event=None):
    user_input = entry.get()
    webbrowser.open(f"https://www.google.com/search?q={user_input}")
    root.quit()  # Fecha a janela após a entrada


root = tk.Tk()
root.overrideredirect(True)  # Remove as bordas e a barra de título
root.geometry("300x50+500+300")  # Define o tamanho e a posição da janela

entry = tk.Entry(root, font=('Arial', 14))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

entry.bind("<Return>", on_enter)  # Liga a tecla Enter ao evento de entrada

entry.focus_set()  # Coloca o foco no campo de entrada

root.mainloop()

# Testar TTK
