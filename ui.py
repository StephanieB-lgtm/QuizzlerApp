from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.canvas = Canvas(height=250, width=300, bg="white",)
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # score
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)



        #Buttons
        true= PhotoImage(file="images/true.png")
        self.right_button=Button(image=true, highlightthickness=0, command=self.correct)
        self.right_button.grid(row=2, column=0)



        false= PhotoImage(file="images/false.png")
        self.false_button=Button(image=false, highlightthickness=0, command=self.incorrect)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def incorrect(self,):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)

