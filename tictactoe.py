from time import sleep
import numpy as np
import os

arr = np.array(['0' , '1' , '2' ,'3', '4' ,'5' ,'6' ,'7', '8', '9'])
player = 1
flag = 0
clear = lambda: os.system('cls')

def boarder() :
        print("     |     |      ")
        print(f"  {arr[1]}  |  {arr[2]}  |  {arr[3]}")
        print("_____|_____|_____ ")
        print("     |     |      ")
        print(f"  {arr[4]}  |  {arr[5]}  |  {arr[6]}")
        print("_____|_____|_____ ")
        print("     |     |      ")
        print(f"  {arr[7]}  |  {arr[8]}  |  {arr[9]}")
        print("     |     |      ")

def checkwin() :
    if arr[1] == arr[2] and arr[2] == arr[3] :
        return 1
    if arr[4] == arr[5] and arr[5] == arr[6] :
        return 1
    if arr[7] == arr[8] and arr[8] == arr[9] :
       return 1
    if arr[1] == arr[4] and arr[4] == arr[7] :
        return 1
    if arr[2] == arr[5] and arr[5] == arr[8] :
        return 1
    if arr[3] == arr[6] and arr[6] == arr[9] :
        return 1
    if arr[1] == arr[5] and arr[5] == arr[9] :
        return 1
    if arr[7] == arr[5] and arr[5] == arr[3] :
        return 1
    elif arr[1] != '1' and arr[2] != '2'  and arr[3] != '3' and arr[4] != '4' and arr[5] != '5' and arr[6] != '6' and arr[7] != '7' and arr[8] != '8' and arr[9] != '9' :
        return -1
    
    return 0

while flag == 0 : 
    if player % 2 == 0 :
     print("player 2 chance")
    else :
     print("player 1 chance") 
    boarder()
    choice_ = int(input())
    if arr[choice_] != '0' and arr[choice_] != 'X' :
       if player % 2 == 0 :
           arr[choice_] = 'X'
           player += 1
       else :
        arr[choice_] = '0'
        player += 1

    else   :
        print("This position already marked") 
        sleep(2)

    flag = checkwin()

    clear()
    
    
if flag == 1 :
    print("Player {} won".format((player % 2)+1))

if flag == -1 :
    print("Draw")





