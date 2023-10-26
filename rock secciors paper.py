# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:52:50 2023

@author: PC
"""
import random

while True:
    print("1-Play again")
    print("2-Endgame")
    choice=input("Enter a choice")
    if choice == "1":
        x=["rock","paper","scissor"]
        player1 = input("select Rock,Paper,Scissor:").lower()
        if player1 in x:
            player2 =random.choice(x).lower()
            print("Player 2 selected:",player2)
            
            if player1 == "rock" and player2 == "paper":
                print("Player 2 won")
            elif player1 == "paper" and player2 == "scissor":
                print("Player 2 won")
            elif player1 == "scissor" and player2 == "rock":
                print("Player 2 won")
            elif player1 == player2:
                print("Tie")
            else:
                print("player 1 Won")
        else:
            print("invalid input")
    elif choice == "2":
        print("Game Over")
        break
    else:
        print("invalid input")
        break
    
