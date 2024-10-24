from tkinter import *
from tkmacosx import Button
import random

#adds to score if player wins
def player1_add():
    global player1
    player1+=1
    print(player1) 
    score.config(text=(f'{player1} - {player2}'))  
player1=0

#adds to score if computer wins
def player2_add():
    global player2
    player2+=1
    print(player2)
    score.config(text=(f'{player1} - {player2}'))
player2 = 0

#starts the game
def start_game():
    start_button.destroy()
    welcome.destroy()
    score.grid(row=0, column=1, padx=75)
    rock1.grid(row=1, column=0)
    paper1.grid(row=2, column=0)
    scissor1.grid(row=3, column=0)
    moves.grid(row=2,column=1)
    result.grid(row=3, column=1)

#if player chose rock
def Rock():
    # for computer to choose rps
    choice = ['rock', 'paper', 'scissors', ]
    chance = random.choice(choice)
    #conditions 
    if chance == 'rock':
        print("Tie")
        result.config(text="It's a tie!")
        moves.config(text=f'Computer chose: Rock \n Player chose: Rock')
    elif chance == 'paper':
        print("you lose")
        moves.config(text=f'Computer chose: Paper \n Player chose: Rock')
        result.config(text='Computer wins!')
        player2_add()
    elif chance == 'scissors':
        print("you win")
        moves.config(text=f'Computer chose: Scissors \n Player chose: Rock')
        result.config(text='You win!')
        player1_add() 

#if player chose paper
def Paper():
    # for computer to choose rps
    choice = ['rock', 'paper', 'scissors', ]
    chance = random.choice(choice)
    #conditions 
    if chance == 'rock':
        print("you win")
        moves.config(text=f'Computer chose: Rock \n Player chose: Paper')
        result.config(text='You win!')
        player1_add()
    elif chance == 'paper':
        print("Tie")
        result.config(text="It's a tie!")
        moves.config(text=f'Computer chose: Paper \n Player chose: Paper')
    elif chance == 'scissors':
        print("you lose")
        moves.config(text=f'Computer chose: Scissors \n Player chose: Paper')
        result.config(text='Computer wins!')
        player2_add()

#if player chose scissors
def Scissor():
    # for computer to choose rps
    choice = ['rock', 'paper', 'scissors', ]
    chance = random.choice(choice)
    #conditions 
    if chance == 'rock':
        print("you lose")
        moves.config(text=f'Computer chose: Rock \n Player chose: Scissors')
        result.config(text='Computer wins!')
        player2_add()
    elif chance == 'paper':
        print("you win")
        moves.config(text=f'Computer chose: Paper \n Player chose: Scissors')
        result.config(text='You win!')
        player1_add()
    elif chance == 'scissors':
        print("Tie")
        result.config(text="It's a tie!")
        moves.config(text=f'Computer chose: Scissors \n Player chose: Scissors')

# screen config
root = Tk()
root.title('Rock Paper scissors')
root.geometry('500x500')
root.resizable(False, False)
root.config(bg='black')

# images
the_rock = PhotoImage(file='Rock.png')

the_paper = PhotoImage(file='Paper.png')

the_scissor = PhotoImage(file='Scissor.png')

# All labels
welcome = Label(root, text='Welcome to Rock Paper Scissors!', fg='white', bg='black')
welcome.place(x=150, y=100)

score = Label(root, text=(f'{player1} - {player2}'), font=('arial', 50), fg='white', bg='black')

result = Label(root, font=('arial', 15), fg='white', bg='black')

moves = Label(root,bg='black',fg='white',font=('arial',20))

# All the buttons
start_button = Button(root, text='Press to start', command=start_game, highlightbackground='black', bg='black',fg='white')
start_button.config(activebackground='white',activeforeground='black')
start_button.place(x=200, y=200)

# RPS
rock1 = Button(root, text='Rock', image=the_rock, compound='top',highlightbackground='black', command=Rock)
rock1.config(bg='red',activebackground='#9e0202', activeforeground='black')

paper1 = Button(root, text='Paper', image=the_paper, compound='top',highlightbackground='black', command=Paper)
paper1.config(bg='#05D5FA',activebackground='#005ec2' , activeforeground='black')

scissor1 = Button(root, text='Scissor', image=the_scissor, compound='top',highlightbackground='black', command=Scissor)
scissor1.config(bg='#39FF14',activebackground='green', activeforeground='black')

root.mainloop()