from tkinter import *
from tkmacosx import Button
import random


# adds to score if player wins
def player1_add():
    global player1
    player1 += 1
    print(player1)
    score.config(text=f'{player1} - {player2}')


player1 = 0


# adds to score if computer wins
def player2_add():
    global player2
    player2 += 1
    print(player2)
    score.config(text=f'{player1} - {player2}')


player2 = 0


# starts the game
def rps_mode():
    start_button.destroy()
    welcome.destroy()
    one_p.place(x=100,y=230)
    two_p.place(x=300,y=230)
    
    

def single_player():
    one_p.destroy()
    two_p.destroy()
    score.grid(row=0, column=1, padx=75)
    rock.grid(row=1, column=0)
    paper.grid(row=2, column=0)
    scissor.grid(row=3, column=0)
    moves.grid(row=2, column=1)
    result.place(row=3, column=1)


def players_two():
    one_p.destroy()
    two_p.destroy()
    turn.grid(row=0, column=1,padx=50)
    turn.config(text="Player 1's turn")
    rock_player1.grid(row=1, column=0)
    paper_player1.grid(row=2, column=0)
    scissors_player1.grid(row=3, column=0)
    result.grid(row=1,column=1,padx=175)



#for 2 players gamemode

def rock_p1():
    global player1_choice
    player1_choice = 'Rock'
    turn.config(text='Pass to second player')
    rock_player1.grid_remove()
    paper_player1.grid_remove()
    scissors_player1.grid_remove()

    rock_player2.grid(row=1, column=0)
    paper_player2.grid(row=2, column=0)
    scissors_player2.grid(row=3, column=0)

def paper_p1():
    global player1_choice
    player1_choice = 'Paper'
    turn.config(text='Pass to second player')
    rock_player1.grid_remove()
    paper_player1.grid_remove()
    scissors_player1.grid_remove()

    rock_player2.grid(row=1, column=0)
    paper_player2.grid(row=2, column=0)
    scissors_player2.grid(row=3, column=0)

def scissors_p1():
    global player1_choice
    player1_choice = 'Scissors'
    turn.config(text='Pass to second player')
    rock_player1.grid_remove()
    paper_player1.grid_remove()
    scissors_player1.grid_remove()

    rock_player2.grid(row=1, column=0)
    paper_player2.grid(row=2, column=0)
    scissors_player2.grid(row=3, column=0)


def rock_p2():
    global player2_choice
    player2_choice = 'Rock'
    checker()

def paper_p2():
    global player2_choice
    player2_choice = 'Paper'
    checker()

def scissors_p2(): 
    global player2_choice
    player2_choice = 'Scissors'
    checker()

#checks for winner
def checker():
    #checks for rock in player one
    if player1_choice == 'Rock' and player2_choice == 'Rock':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nIt's a tie!")
    elif player1_choice == 'Rock' and player2_choice == 'Paper':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nPlayer 2 wins!")
    elif player1_choice == 'Rock' and player2_choice == 'Scissors':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nPlayer 1 wins!")
    
    #checks for paper in player 1
    elif player1_choice == 'Paper' and player2_choice == 'Rock':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nPlayer 1 wins!")
    elif player1_choice == 'Paper' and player2_choice == 'Paper':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nIt's a tie!")
    elif player1_choice == 'Paper' and player2_choice == 'Scissors':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nPlayer 2 wins!")

    elif player1_choice == 'Scissors' and player2_choice == 'Rock':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nPlayer 2 wins!")
    elif player1_choice == 'Scissors' and player2_choice == 'Paper':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nPlayer 2 wins!")
    elif player1_choice == 'Scissors' and player2_choice == 'Scissors':
        result.config(text=f"Player 1's choice: {player1_choice} \nPlayer 2's choice: {player2_choice} \nIt's a tie!")

    restart.place(x=200,y=225)
    rock_player2.grid_remove()
    paper_player2.grid_remove()
    scissors_player2.grid_remove()
    turn.config(text='')
    
    

def replay():
    players_two()
    result.config(text='')
    restart.place_forget()
    
def backToMenu():
    pass


# if player chose rock
def Rock():
    # for computer to choose rps
    choice = ['rock', 'paper', 'scissors', ]
    chance = random.choice(choice)

    # conditions
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


# if player chose paper
def Paper():
    # for computer to choose rps
    choice = ['rock', 'paper', 'scissors', ]
    chance = random.choice(choice)
    # conditions
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


# if player chose scissors
def Scissor():
    # for computer to choose rps
    choice = ['rock', 'paper', 'scissors', ]
    chance = random.choice(choice)
    # conditions
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
score = Label(root, text=f'{player1} - {player2}', font=('arial', 50), fg='white', bg='black')
result = Label(root, font=('arial', 15), fg='white', bg='black')
moves = Label(root, bg='black', fg='white', font=('arial', 20))
turn = Label(root,font=('arial 25 '),bg='black',fg='white')


# All the buttons
start_button = Button(root, text='Press to start', command=rps_mode, highlightbackground='black', bg='black',fg='white')
start_button.config(activebackground='white', activeforeground='black')
start_button.place(x=200, y=200)

one_p = Button(root,text="Single player", command=single_player)

two_p = Button(root,text="Two players", command=players_two)

restart = Button(root,text='Restart',bg='black',fg='white',highlightbackground='black', command=replay)

# RPS
#single player buttons
rock = Button(root, text='Rock', image=the_rock, compound='top', highlightbackground='black', command=Rock)
rock.config(bg='red', activebackground='#9e0202', activeforeground='black')

paper = Button(root, text='Paper', image=the_paper, compound='top', highlightbackground='black', command=Paper)
paper.config(bg='#05D5FA', activebackground='#005ec2', activeforeground='black')

scissor = Button(root, text='Scissor', image=the_scissor, compound='top', highlightbackground='black', command=Scissor)
scissor.config(bg='#39FF14', activebackground='green', activeforeground='black')

#for 2 players
#player 1 buttons
rock_player1 = Button(root, text='Rock', image=the_rock, compound='top', highlightbackground='black', command=rock_p1)
rock_player1.config(bg='red', activebackground='#9e0202', activeforeground='black')

paper_player1 = Button(root, text='Paper', image=the_paper, compound='top', highlightbackground='black', command=paper_p1)
paper_player1.config(bg='#05D5FA', activebackground='#005ec2', activeforeground='black')

scissors_player1 = Button(root, text='Scissors', image=the_scissor, compound='top', highlightbackground='black', command=scissors_p1)
scissors_player1.config(bg='#39FF14', activebackground='green', activeforeground='black')

#player 2 buttons
rock_player2 = Button(root, text='Rock', image=the_rock, compound='top', highlightbackground='black', command=rock_p2)
rock_player2.config(bg='red', activebackground='#9e0202', activeforeground='black')

paper_player2 = Button(root, text='Paper', image=the_paper, compound='top', highlightbackground='black', command=paper_p2)
paper_player2.config(bg='#05D5FA', activebackground='#005ec2', activeforeground='black')

scissors_player2 = Button(root, text='Scissors', image=the_scissor, compound='top', highlightbackground='black', command=scissors_p2)
scissors_player2.config(bg='#39FF14', activebackground='green', activeforeground='black')

root.mainloop()
