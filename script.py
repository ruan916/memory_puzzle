from tkinter import *
import random, sys
from tkinter import messagebox

root = Tk()
root.title('Memory Puzzle')
root.geometry("450x500")

global winner
winner = 0

matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict = {}

def win():
    my_label.config(text="Congratulations! You win!!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    for button in button_list:
        button.config(bg="Green")

def button_click(b, number):
    global count, answer_list, answer_dict, winner

    if b["text"] == ' ' and count < 2:
        b["text"] = matches[number]
        answer_list.append(number)
        answer_dict[b] = matches[number]
        count += 1
    
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text = "MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            winner += 1
            if winner == 6:
                win()
        else:
            my_label.config(text = "DOH!")
            count = 0
            answer_list = []
            messagebox.showinfo("Incorrect!", "Incorrect")
            for key in answer_dict:
                key["text"] = " "
            answer_dict = {}

b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b0, 0))
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b1, 1))
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b2, 2))
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b3, 3))
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b4, 4))
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b5, 5))
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b6, 6))
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b7, 7))
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b8, 8))
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b9, 9))
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b10, 10))
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b11, 11))

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text = "")
my_label.pack(pady = 20)

my_label2 = Label(root)
my_label2.pack()

def button_click_close():
    sys.exit()

btclose = Button(my_label2, text="CLOSE", font=("Helvetica", 10), height=1, width=5, command=lambda: button_click_close)
btclose.grid(row=0,column=0)

root.mainloop()