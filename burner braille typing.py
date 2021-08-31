import tkinter as tk
import tkinter.scrolledtext


root = tk.Tk()


def key_handling(event):
    message = f"{event.keysym}"
    text_area.config(state="normal")
    text_area.insert('end', message)
    text_area.yview('end')
    text_area.config(state='disabled')


text_area = tk.scrolledtext.ScrolledText(root, height=20, width=50)
text_area.pack(padx=10, pady=10)
text_area.config(state="disabled")

text_area.bind("<KeyRelease>", key_handling)
text_area.bind_all()

root.mainloop()
