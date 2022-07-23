import random
import tkinter as tk
from tkinter import *
list_of_numbers = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
possible_insert_array = []
def insert_twos(possible_insert_array, list_of_numbers, num_of_twos):
    possible_insert_array = []
    counter = 0
    for z in range(num_of_twos):
        next = True
        while next == True:
            possible_insert_array = []
            for i in range(2):
                possible_insert_array_index_first_dimension = random.randrange(0,4)
                possible_insert_array.append(possible_insert_array_index_first_dimension)
            if list_of_numbers[possible_insert_array[0]][possible_insert_array[1]] > 0:
                next = True
            else:
                list_of_numbers[possible_insert_array[0]][possible_insert_array[1]] = 2
                next = False
                counter += 1

def smash_left():
    global list_of_numbers
    for i in range(4):
        for j in range(4):
            for s in range(3):
                if list_of_numbers[i-1][j-1] == 0:
                    list_of_numbers[i-1].pop(j-1)
                    list_of_numbers[i-1].append(0)
    for j in range(4):
        for i in range(4):
            if (list_of_numbers[j-1][i-2] > 0) and (list_of_numbers[j-1][i-2] == list_of_numbers[j-1][i-1]):
                multiply = list_of_numbers[j-1][i-2] * 2
                list_of_numbers[j-1][i-2] = multiply
                list_of_numbers[j-1].pop(i-1)
                list_of_numbers[j-1].append(0)
    num_of_twos = 1
    print('####')
    print(list_of_numbers)
    print('####')
    insert_twos(possible_insert_array, list_of_numbers, num_of_twos)
    for i in range(4):
        for j in range(4):
            inttld = ((i)*4) + (j)
            tld = str(inttld)
            globals()['string%s' % tld].config(text=list_of_numbers[i][j])

def flip_left(x):
    global list_of_numbers
    for q in range(x):
        columns = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                columns[i].append(list_of_numbers[j][i])
    #print('columns = ', columns)
        list_of_numbers = columns
    smash_left()
    for w in range():
        columns = [[],[],[],[]]
        for s in range(4):
            for p in range(4):
                columns[s].append(list_of_numbers[p][s])
    list_of_numbers = columns
    for i in range(4):
        for j in range(4):
            inttld = ((i)*4) + (j)
            tld = str(inttld)
            globals()['string%s' % tld].config(text=list_of_numbers[i][j])
def down():
    x = 3
    flip_left(x)
def up():
    x = 1
    flip_left(x)
def right():
    x = 2
    flip_left(x)


flip_array = [[],[],[],[]]
num_of_twos = 2
insert_twos(possible_insert_array, list_of_numbers, num_of_twos)
print(list_of_numbers)
frame = tk.Tk()
frame.geometry("272x328")
frame.title("2048")
for i in range(4):
    for j in range(4):
        inttld = ((i)*4) + (j)
        tld = str(inttld)
        globals()['string%s' % tld] = Label(frame, text=list_of_numbers[i][j], height=4, width=5)
        globals()['string%s' % tld].grid(column=(j), row=(i))
       
left_button = Button(frame, height=4, width=4, text="left", command=smash_left).grid(column=(6), row=(6))
up_button = Button(frame, height=4, width=4, text="up", command=up).grid(column=(7), row=(7))
right_button = Button(frame, height=4, width=4, text="right", command=right).grid(column=(8), row=(8))
down_button = Button(frame, height=4, width=4, text="down", command=down).grid(column=(9), row=(9))
frame.mainloop()
