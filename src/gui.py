from tkinter import Tk, Label, Button, StringVar, messagebox
import kbc
import random

class KBCGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kaun Banega Crorepati")
        self.master.configure(bg="#1a1a1a")
        self.master.geometry("600x400")
        self.current_question = 0
        self.total_won = 0
        self.current_level = 0
        
        # StringVar to hold the current question and options
        self.question_var = StringVar()
        self.option_vars = [StringVar() for _ in range(4)]
        
        # Shuffle the questions to randomize the order
        self.questions = random.sample(kbc.questions, len(kbc.questions))
        
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        # Label to display the current question
        self.question_label = Label(self.master, textvariable=self.question_var, wraplength=500, bg="#1a1a1a", fg="#ffffff", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            # Buttons for the answer options
            button = Button(self.master, textvariable=self.option_vars[i], command=lambda i=i: self.check_answer(i), bg="#333333", fg="#ffffff", font=("Helvetica", 14), width=20)
            button.pack(pady=5)
            self.option_buttons.append(button)

        # Button to quit the game
        self.quit_button = Button(self.master, text="Quit", command=self.quit_game, bg="#ff0000", fg="#ffffff", font=("Helvetica", 14), width=20)
        self.quit_button.pack(pady=20)

    def load_question(self):
        if self.current_question < len(self.questions):
            # Load the current question and options
            question_data = self.questions[self.current_question]
            self.question_var.set(f"Q{self.current_question + 1}: {question_data[0].split(': ', 1)[1]}")
            for i in range(4):
                self.option_vars[i].set(question_data[i + 1])
        else:
            # End the game if there are no more questions
            self.end_game()

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question][5]
        if selected_option + 1 == correct_answer:
            # Correct answer, update the total won and load the next question
            self.total_won = kbc.prize_levels[self.current_question]
            next_prize = kbc.prize_levels[self.current_question + 1] if self.current_question + 1 < len(kbc.prize_levels) else "the final prize"
            messagebox.showinfo("Correct!", f"Correct answer! You have won Rs. {self.total_won}. Next question is for Rs. {next_prize}")
            self.current_question += 1
            if self.current_question in kbc.level_milestones:
                self.current_level += 1
            self.load_question()
        else:
            # Wrong answer, end the game
            messagebox.showerror("Wrong!", f"Wrong answer! Game over. You have won Rs. {self.total_won}")
            self.end_game()

    def end_game(self):
        # Show the final amount won and quit the game
        messagebox.showinfo("Game Over", f"You finished the game with Rs. {self.total_won}")
        self.master.quit()

    def quit_game(self):
        # Quit the game and show the final amount won
        messagebox.showinfo("Quit Game", f"You have finished the game with Rs. {self.total_won}")
        self.master.quit()

if __name__ == "__main__":
    root = Tk()
    game = KBCGameGUI(root)
    root.mainloop()