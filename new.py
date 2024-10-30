from tkinter import *
import random

# Constants
SCORE_FILE = "high_scores.txt"
MAX_HIGH_SCORES = 1

# Colours present
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
time = 30

# Start the Game
def startGame(event):
    if time == 30:
        # start the countdown timer
        countdown()

    # function to choose the next color
    nextcolor()

def nextcolor():
    global score
    global time

    # if a game is in play
    if time > 0:
        # make the text entry box active
        colour_entry.focus_set()

        if colour_entry.get().lower() == colours[1].lower():
            score += 1

        # clear the entry box
        colour_entry.delete(0, END)

        random.shuffle(colours)

        # change the colour to type, by changing the text and the colour to a random colour value
        
        colour.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))

# Countdown Timer Function
def countdown():
    global time

    # if a game is in play
    if time > 0:
        # decrement the value
        time -= 1

        # update the time left label
        timeLabel.config(text="Time left: " + str(time))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
    else:
        # game over, show final score
        game_over()

# Game Over Function
def game_over():
    # Disable entry and unbind return key
    colour_entry.config(state='disabled')
    root.unbind('<Return>')
    # Show Game Over message and final score
    colour.config(text="Game Over!", fg="red")
    scoreLabel.config(text="Final Score: " + str(score))
    # Update high scores
    update_high_scores(score)

# Update High Scores Function
def update_high_scores(final_score):
    try:
        # Read existing high scores
        with open(SCORE_FILE, "r") as file:
            high_scores = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        high_scores = []

    # Add current score to high scores
    high_scores.append(final_score)
    high_scores.sort(reverse=True)

    # Truncate to maximum number of high scores
    high_scores = high_scores[:MAX_HIGH_SCORES]

    # Write updated high scores to file
    with open(SCORE_FILE, "w") as file:
        for score in high_scores:
            file.write(str(score) + "\n")

    # Update high scores label
    high_scores_label.config(text="High Scores:\n" + "\n".join(map(str, high_scores)))

# GUI Improvements Function
def gui_improvements():
    # Add background color
    root.config(bg="#f0f0f0")

    # Add a title label
    title = Label(root, text="Color Game", font=("Helvetica", 24), bg="#f0f0f0")
    title.pack()

    # Add instructions label
    instructions = Label(root, text='Type in the colour of the words, and not the word text!', font=('Helvetica', 14), bg="#f0f0f0")
    instructions.pack()

    # Add high scores label
    global high_scores_label
    high_scores_label = Label(root, text="High Scores:", font=('Helvetica', 14), bg="#f0f0f0")
    high_scores_label.pack()

# Driver Code
if __name__ == '__main__':
    root = Tk()

    # Setting the title
    root.title('Color Game')

    # Setting the geometry of the window
    root.geometry('600x400')

    # Apply GUI improvements
    gui_improvements()

    # Create a Score label
    scoreLabel = Label(root, text='Score :' + str(score), font=('Helvetica', 15), bg="#f0f0f0")
    scoreLabel.pack()

    # Create a Time Label
    timeLabel = Label(root, text='Time Left : ' + str(time), font=('Helvetica', 15), bg="#f0f0f0")
    timeLabel.pack()

    # create a colour label
    colour = Label(root, font=('Helvetica', 17), bg="#f0f0f0")
    colour.pack()

    # Entry box for input from user
    colour_entry = Entry(root, font=('Helvetica', 16))
    colour_entry.focus_set()
    colour_entry.pack()

    root.bind('<Return>', startGame)

    root.mainloop()
