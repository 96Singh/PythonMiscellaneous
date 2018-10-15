#Type the colour and not the word

#import the modules we need, for creating a GUI...
import tkinter
#...and for creating random numbers.
import random

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','Brown']
score=0
timeleft=30

def startGame(event):

    if timeleft == 30:
        countdown()
        
    nextColour()


def nextColour():

    #use the globally declared 'score' and 'play' variables above.
    global score
    global timeleft

    #if a game is currently in play...
    if timeleft > 0:

        #...make the text entry box active.
        e.focus_set()

        #if the colour typed is equal to the colour of the text...
        if e.get().lower() == colours[1].lower():
            #...add one to the score.
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))
        

#a countdown timer function. 
def countdown():

    global timeleft

    if timeleft > 0:

        #decrement the timer.
        timeleft -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeleft))
        #run the function again after 1 second.
        timeLabel.after(1000, countdown)
    
#create a GUI window.
root = tkinter.Tk()
root.title("ColourNotWord")
root.geometry("600x300")

#add an instructions label.
instructions = tkinter.Label(root, text="Type in the colour of the words you see, and not the word text!", font=('Helvetica', 12))
instructions.pack()

#add a score label.
scoreLabel = tkinter.Label(root, text="Please press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

#add a time left label.
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

#add a label for displaying the colours.
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

#add a text entry box for typing in colours.
e = tkinter.Entry(root)
#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
e.pack()
#set focus on the entry box.
e.focus_set()

#start the Game GUI
root.mainloop()