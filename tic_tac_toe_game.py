''''
Python implementation of Tic Tac Toe game.
'''
import random
def turn():
    '''
    Chose which player would go first
    '''
    num=random.randint(0,1)
    return num


def display(board):
    '''
    To display the current state of the Tic-Tac-Toe board
    '''
    print(board[1],'|',board[2],'|',board[3])
    print(board[4],'|',board[5],'|',board[6])
    print(board[7],'|',board[8],'|',board[9])

def space_check(board,pos):
    '''
    Check whether the place/ spot chosen by the player is available
    '''
    if board[pos] != '':
        print('Place already occupied!')
        return False
    return True

def select_player():
    '''
    Initial selection of the player and chosing the symbol to play with. 
    The symbol choice is given to th eplayer going first and the second
    player's symbol is automatically assigned 
    '''
    acceptable_val=['X','O']
    player_flag=False
    while player_flag is False:
        player1=input('Do you want to be an X or O ?')
        if player1.upper() not in acceptable_val:
            print('Invalid choice!')
        else:
            player_flag=True
    player1=player1.upper()
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return player1,player2

def chose_position(board,moves):
    '''
    Ask and validate the move and check if a winning sequence is found
    '''
    acceptable_range=range(0,10)
    pos_flag=False
    win_flag=False

    while pos_flag==False and win_flag==False:        
        pos=input('Choose your position: ')
        try:
            if int(pos) not in acceptable_range:
                print('Number not in acceptable range! Try again!')
            else:
                if space_check(board, int(pos)):
                    pos_flag=True
                    up_flag=update_val(board,int(pos),moves)
                    if up_flag == False:
                        pos_flag=False
                    else:
                        if moves[-1]=='#':
                            print('Caught in a tie! Game ends here')
                            break
                        if check_winner(board, board[int(pos)]):
                            win_flag=True
                            pos_flag=True
                            print(f'Winner found! {board[int(pos)]} Wins the game!')
                            display(board)
                            break
                        else:
                            win_flag=False
                            pos_flag=False
                else:
                    print('Select another position!')
            display(board)
        except:
            print('Please enter a number to proceed')

def update_val(board,pos,moves):
    '''
    Update board with the move
    '''

    play=moves.pop()
    #print(f'{play} played')
    board[pos]=play
    return True


def playagain():
    '''
    Ask if the player wants to play again
    '''
    replay=True
    while replay:
        print('Hi\nWelcome to Tic-Tac-Toe game\nEnter a number from 1-9 (corresponding to a telephone numberpad) to proceed.\n***Good Luck***\n\n ')
        num=turn()
        if num==0:
            print('Player 1 goes first!')
        else:
            print('Player 2 goes first!') 
        
        player1,player2=select_player()
        print(f'Player 1: {player1}\nPlayer 2: {player2}')
        #declaring the move sequence
        if player1=='X':
            moves=['#','X','O','X','O','X','O','X','O','X']
        else:
            moves=['#','O','X','O','X','O','X','O','X','O']

        board={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
        
        replay=chose_position(board,moves)
        replay=input('\nDo you want to play again? Y \ N :')
        if replay.upper()=='Y':
            replay=True
        else:
            replay=False
    return False

def check_winner(board,mark):
    '''
    checking for winning sequence
    '''
    return ((board[1]==board[2]==board[3]==mark) or
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[3]==board[5]==board[7]==mark)
    )
   
replay=True
game=playagain()
if not game:
    print('Thanks for playing')


