import tkinter as tk
import random
def play(choice):
    computer = random.choice(['rock', 'paper', 'scissors'])
    if choice == computer:
        result = "It's a tie!"
    elif (choice == 'rock' and computer == 'scissors') or \
         (choice == 'paper' and computer == 'rock') or \
         (choice == 'scissors' and computer == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"
    result_label.config(text=f"You chose {choice}, Computer chose {computer}. {result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Button(root, text="Rock", command=lambda: play('rock')).pack()
tk.Button(root, text="Paper", command=lambda: play('paper')).pack()
tk.Button(root, text="Scissors", command=lambda: play('scissors')).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()