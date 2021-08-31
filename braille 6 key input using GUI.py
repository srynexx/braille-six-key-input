# Braille six key input or Perkins Braille uses 6 set of keys, one for each dot in a braille cell.
# To type in braille, use SDFJKL keys only in keyboard. (best if keyboard has N-key rollover feature)
# Different combinations of SDFJKL keys gives different braille code.
# Each key combinations must be pressed and released together at once.
# F = dot-1, D = dot-2, S = dot-3, J = dot-4, K = dot-5, L = dot-6.
# Hit Return key on keyboard to display typed braille code with its corresponding translation,
# or click the green button. (based on grade 1 braille)
# For extra, backspace is included to delete each braille code like deleting normal letter.
# For extra, spacebar is included to add gap between each word like normal text does.
# Make sure GUI window is in focus for key binding to work,
# best if the small textbox is tapped 1st b4 start typing

import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog, messagebox


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Typing Braille with keyboard")
        self.config(bg="grey20")

        self.variable = tk.StringVar()
        self.variable.set(hold_key_list)

        self.create_widgets()

        self.bind("<KeyPress>", self.hold_key)
        self.bind("<KeyRelease>", self.key_combine)
        self.bind("<space>", self.space_bar)
        self.bind("<BackSpace>", self.backspace)
        self.bind("<Return>", lambda event: self.write())

        self.mainloop()

    def create_widgets(self):
        self.main_frame = tk.Frame(self, bg="grey20")
        self.main_frame.grid(column=0, row=0, padx=10, pady=10)

        self.label1 = tk.Label(self.main_frame, text=f"Braille six key input")
        self.label1.config(font=("Arial Black", 12), width=30, bg="grey40", fg="snow")
        self.label1.grid(column=0, row=2, columnspan=3)

        self.text_area = tk.scrolledtext.ScrolledText(self.main_frame, height=20, width=60, bg="lavender")
        self.text_area.grid(column=0, row=3, columnspan=3)
        self.text_area.config(font=("Calibri", 12), wrap="word", state="disabled")

        self.label2 = tk.Label(self.main_frame, text="Type in this small textbox")
        self.label2.config(font=("Arial", 12, "bold"), bg="grey20", fg="snow")
        self.label2.grid(column=0, row=4, columnspan=3)

        self.input_area = tk.Text(self.main_frame, height=5, width=50, bg="lavender")
        self.input_area.grid(column=0, row=5, columnspan=2)
        self.input_area.config(font=("Calibri", 12), state="disabled")

        self.send_button = tk.Button(self.main_frame, text="Click To\nDisplay", command=self.write)
        self.send_button.config(font=("Arial", 12, "bold"), height=3, width=10, bg="green2")
        self.send_button.grid(column=2, row=5, padx=5)

    def write(self):
        self.input_area.config(state="normal")
        braille = self.input_area.get('1.0', 'end')
        self.input_area.delete('1.0', 'end')
        self.input_area.config(state="disabled")

        braille_mapping = {
            u'\u2801': "a",
            u'\u2803': "b",
            u'\u2809': "c",
            u'\u2819': "d",
            u'\u2811': "e",
            u'\u280B': "f",
            u'\u281B': "g",
            u'\u2813': "h",
            u'\u280A': "i",
            u'\u281A': "j",
            u'\u2805': "k",
            u'\u2807': "l",
            u'\u280D': "m",
            u'\u281D': "n",
            u'\u2815': "o",
            u'\u280F': "p",
            u'\u281F': "q",
            u'\u2817': "r",
            u'\u280E': "s",
            u'\u281E': "t",
            u'\u2825': "u",
            u'\u2827': "v",
            u'\u283A': "w",
            u'\u282D': "x",
            u'\u283D': "y",
            u'\u2835': "z",
            u'\u2834': "0",
            u'\u2802': "1",
            u'\u2806': "2",
            u'\u2812': "3",
            u'\u2832': "4",
            u'\u2822': "5",
            u'\u2816': "6",
            u'\u2836': "7",
            u'\u2826': "8",
            u'\u2814': "9",

            u'\u2800': " ",

            u'\u282E': "!",
            u'\u2810': '"',
            u'\u283C': "#",
            u'\u282B': "$",
            u'\u2829': "%",
            u'\u282F': "&",
            u'\u2804': "'",
            u'\u2837': "(",
            u'\u283E': ")",
            u'\u2821': "*",
            u'\u282C': "+",
            u'\u2820': ",",
            u'\u2824': "-",
            u'\u2828': ".",
            u'\u280C': "/",
            u'\u2831': ":",
            u'\u2830': ";",
            u'\u2823': "<",
            u'\u283F': "=",
            u'\u281C': ">",
            u'\u2839': "?",
            u'\u2808': "@",
            u'\u282A': "[",
            u'\u2833': "\\",
            u'\u283B': "]",
            u'\u2818': "^",
            u'\u2838': "_",
        }

        output = ""
        for letter in braille:
            if letter in braille_mapping:
                output = f"{output}{braille_mapping.get(letter)}"
            elif letter == '\t':
                output = f"{output}\t"
            elif letter == '\n':
                output = f"{output}\n"
            else:
                continue

        message = f">> {output}\n"
        message2 = f">> {braille}"

        self.text_area.config(state="normal")
        self.text_area.insert('end', message2)
        self.text_area.insert('end', message)
        self.text_area.yview('end')
        self.text_area.config(state='disabled')

    @staticmethod
    def hold_key(event):
        try:
            if hold_key_list.index(event.keysym):
                # return event.keysym
                pass
        except:
            hold_key_list.append(event.keysym)

    def key_combine(self, event):
        word = "".join(sorted(hold_key_list))
        lower_caps = word.lower()
        # print(lower_caps)
        if lower_caps in letter_combination_mapping:
            output = letter_combination_mapping.get(lower_caps)
            self.display(output)
        else:
            hold_key_list.clear()
        pass

    def backspace(self, event):
        self.input_area.config(state="normal")
        self.input_area.delete("insert -1 chars", "insert")
        self.input_area.config(state='disabled')

    def space_bar(self, event):
        self.display(event="\u2800")

    def display(self, event):
        self.input_area.config(state="normal")
        self.input_area.insert('end', event)
        self.input_area.yview('end')
        self.input_area.config(state='disabled')
        hold_key_list.clear()


hold_key_list = []
str(hold_key_list)
letter_combination_mapping = {
    "f": u'\u2801',  # a
    "df": u'\u2803',  # b
    "fj": u'\u2809',  # c
    "fjk": u'\u2819',  # d
    "fk": u'\u2811',  # e
    "dfj": u'\u280B',  # f
    "dfjk": u'\u281B',  # g
    "dfk": u'\u2813',  # h
    "dj": u'\u280A',  # i
    "djk": u'\u281A',  # j
    "fs": u'\u2805',  # k
    "dfs": u'\u2807',  # l
    "fjs": u'\u280D',  # m
    "fjks": u'\u281D',  # n
    "fks": u'\u2815',  # o
    "dfjs": u'\u280F',  # p
    "dfjks": u'\u281F',  # q
    "dfks": u'\u2817',  # r
    "djs": u'\u280E',  # s
    "djks": u'\u281E',  # t
    "fls": u'\u2825',  # u
    "dfls": u'\u2827',  # v
    "djkl": u'\u283A',  # w
    "fjls": u'\u282D',  # x
    "fjkls": u'\u283D',  # y
    "fkls": u'\u2835',  # z
    "kls": u'\u2834',  # 0
    "d": u'\u2802',  # 1
    "ds": u'\u2806',  # 2
    "dk": u'\u2812',  # 3
    "dkl": u'\u2832',  # 4
    "dl": u'\u2822',  # 5
    "dks": u'\u2816',  # 6
    "dkls": u'\u2836',  # 7
    "dls": u'\u2826',  # 8
    "ks": u'\u2814',  # 9

    # " ": u'\u2800',  # space (separate key binding)

    "djls": u'\u282E',  # !
    'k': u'\u2810',  # "
    "jkls": u'\u283C',  # #
    "dfjl": u'\u282B',  # $
    "fjl": u'\u2829',  # %
    "dfjls": u'\u282F',  # &
    "s": u'\u2804',  # '
    "dfkls": u'\u2837',  # (
    "djkls": u'\u283E',  # )
    "fl": u'\u2821',  # *
    "jls": u'\u282C',  # +
    "l": u'\u2820',  # ,
    "ls": u'\u2824',  # -
    "jl": u'\u2828',  # .
    "js": u'\u280C',  # /
    "fkl": u'\u2831',  # :
    "kl": u'\u2830',  # ;
    "dfl": u'\u2823',  # <
    "dfjkls": u'\u283F',  # =
    "jks": u'\u281C',  # >
    "fjkl": u'\u2839',  # ?
    "j": u'\u2808',  # @
    "djl": u'\u282A',  # [
    "dfkl": u'\u2833',  # \
    "dfjkl": u'\u283B',  # ]
    "jk": u'\u2818',  # ^
    "jkl": u'\u2838',  # _

}

Root()
