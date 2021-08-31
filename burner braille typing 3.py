# update to myself

import sys
import tkinter as tk
import tkinter.scrolledtext

root = tk.Tk()


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

    # " ": u'\u2800',  # space # separate key binding

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

variable = tk.StringVar()
hold_key_list = []
str(hold_key_list)
variable.set(hold_key_list)


def display(event):
    text_area.config(state="normal")
    text_area.insert('end', event)
    text_area.yview('end')
    text_area.config(state='disabled')
    hold_key_list.clear()


def backspace(event):
    text_area.config(state="normal")
    text_area.delete("insert -1 chars", "insert")
    text_area.config(state='disabled')


def hold_key(event):
    try:
        if hold_key_list.index(event.keysym):
            # return event.keysym
            pass
    except:
        hold_key_list.append(event.keysym)


def key_combine(event):
    word = "".join(sorted(hold_key_list))
    print(word)
    if word in letter_combination_mapping:
        output = letter_combination_mapping.get(word)
        display(output)
    else:
        hold_key_list.clear()


text_area = tk.scrolledtext.ScrolledText(root, height=20, width=50)
text_area.pack(padx=10, pady=10)
text_area.config(state="disabled")

text_area.bind("<KeyPress>", hold_key)
text_area.bind("<KeyRelease>", key_combine)
text_area.bind("<space>", lambda event: display(event="\u2800"))
text_area.bind("<BackSpace>", backspace)

root.mainloop()
