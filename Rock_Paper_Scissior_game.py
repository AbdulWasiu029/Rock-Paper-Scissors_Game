import tkinter as tk
import random

def determine_winner(user):
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image = user_images[user.lower()]
    computer_image = computer_images[computer.lower()]
    user_label.config(image=user_image)
    computer_label.config(image=computer_image)
    if user == computer:
        result_label.config(text="It's a tie!")
    elif (user == "Rock" and computer == "Scissors") or \
            (user == "Scissors" and computer == "Paper") or \
            (user == "Paper" and computer == "Rock"):
        result_label.config(text=f"User wins! Computer chose {computer}.")
    else:
        result_label.config(text=f"Computer wins! Computer chose {computer}.")

def select_choice(choice):
    determine_winner(choice)

root = tk.Tk()
root.geometry("1300x700")
root.title("Rock-Paper-Scissors Game")

title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 30, "bold"),
                        border=7, relief=tk.GROOVE, bg="DimGray", fg="White")
title_label.pack(side="top", fill="x")

image_frame = tk.Frame(root)
image_frame.pack(pady=20)

user_label = tk.Label(image_frame, text="User", font=("Arial", 14))
user_label.grid(row=0, column=0, padx=10, pady=10)

computer_label = tk.Label(image_frame, text="Computer", font=("Arial", 14))
computer_label.grid(row=0, column=2, padx=10, pady=10)

user_image_label = tk.Label(image_frame)
user_image_label.grid(row=1, column=0, padx=20)

computer_image_label = tk.Label(image_frame)
computer_image_label.grid(row=1, column=2, padx=20)

result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=20)

user_images = {
    "rock": tk.PhotoImage(file="rock.png"),
    "paper": tk.PhotoImage(file="paper.png"),
    "scissors": tk.PhotoImage(file="scissors.png")
}

computer_images = {
    "rock": tk.PhotoImage(file="rock.png"),
    "paper": tk.PhotoImage(file="paper.png"),
    "scissors": tk.PhotoImage(file="scissors.png")
}

button_frame = tk.Frame(root)
button_frame.pack(side="bottom", pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: select_choice("Rock"))
rock_button.pack(side="left", padx=20)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: select_choice("Paper"))
paper_button.pack(side="left", padx=20)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: select_choice("Scissors"))
scissors_button.pack(side="left", padx=20)

root.mainloop()