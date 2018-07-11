import time
import os
moves={'A1':' ', 'A2':' ', 'A3':' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}
p1=1
p2=0
print("\n-How to Play: Write  A1 X  or  a1 x  to display it on the following board.\n ")
print("      1  2  3\n\n A   {} | {} | {} \n     ---------\n B   {} | {} | {}\n     ---------\n C   {} | {} | {}\n\n".format(moves['A1'],moves['A2'],moves['A3'],moves['B1'],moves['B2'],moves['B3'],moves['C1'],moves['C2'],moves['C3']))
position=0
def whoWon():
    if moves['A1'] == moves['A2'] == moves['A3'] == 'O' or moves['A1'] == moves['A2'] == moves['A3'] == 'X':
        print(moves['A1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['B1'] == moves['B2'] == moves['B3'] == 'O' or moves['B1'] == moves['B2'] == moves['B3'] == 'X':
        print(moves['B1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['C1'] == moves['C2'] == moves['C3'] == 'O' or moves['C1'] == moves['C2'] == moves['C3'] == 'X':
        print(moves['C1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['A1'] == moves['B1'] == moves['C1'] == 'O' or moves['A1'] == moves['B1'] == moves['C1'] == 'X':
        print(moves['A1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['A2'] == moves['B2'] == moves['C2'] == 'O' or moves['A2'] == moves['B2'] == moves['C2'] == 'X':
        print(moves['A1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['A3'] == moves['B3'] == moves['C3'] == 'O' or moves['A3'] == moves['B3'] == moves['C3'] == 'X':
        print(moves['A1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['A1'] == moves['B2'] == moves['C3'] == 'O' or moves['A1'] == moves['B2'] == moves['C3'] == 'X':
        print(moves['A1'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
    if moves['A3'] == moves['B2'] == moves['C1'] == 'O' or moves['A3'] == moves['B2'] == moves['C1'] == 'X':
        print(moves['A3'] + " Has won!\n\nExiting in 5 seconds...")
        time.sleep(5)
        exit()
def play1():
    position = input("Player 1: ")
    position = position.split()
    if moves[position[0].upper()] != ' ':
        print("Player 1, the box already taken, you blew your chance.")
    else:
        os.system('cls')
        moves[position[0].upper()]=position[1].upper()
        print("\n      1  2  3\n\n A   {}| {} |{} \n    ---------\n B   {}| {} |{}\n    ---------\n C   {}| {} | {}\n\n".format(moves['A1'], moves['A2'], moves['A3'], moves['B1'], moves['B2'], moves['B3'], moves['C1'], moves['C2'],moves['C3']))
def play2():
    position = input("Player 2: ")
    position = position.split()
    if moves[position[0].upper()] != ' ':
        print("Player 2, the box already taken, you blew your chance.")
    else:
        os.system('cls')
        moves[position[0].upper()]=position[1].upper()
        print("\n      1  2  3\n\n A   {}| {} |{} \n    ---------\n B   {}| {} |{}\n    ---------\n C   {}| {} |{}\n\n".format(moves['A1'], moves['A2'], moves['A3'], moves['B1'], moves['B2'], moves['B3'], moves['C1'], moves['C2'],moves['C3']))
for goon in range(9):
    if p1 == 1:
        p1=0
        play1()
    else:
        p1=1
    if p2 == 1:
        p2=0
        play2()
    else:
        p2=1

    whoWon()
