import copy
import math as m
# import math
# from decimal import *
from decimal import Decimal


def task1():
    print('What is your name: ')
    name = input()
    print('How old are you: ')
    age = input()
    print('Where are you live: ')
    live_place = input()
    print('This is {0}\nYou are {1} y.o.\nYou live in {2}'.format(name, age, live_place))


def example():
    ex = "4 * 100 - 54"
    print(ex)
    ex_ans = 4 * 100 - 54
    return ex_ans


def task2():
    print("Can you figure it out?")
    ex_ans = example()
    print("Input your answer: ")
    answer = input()
    if int(answer) == ex_ans:
        print("Congratulations! Your answer in correct")
    else:
        print("Sorry, your answer isn't correct. Correct answer is ", format(example()))


def task3():
    print("Input 4 numbers:")
    numbers = []
    for num in range(4):
        num = int(input())
        numbers.append(num)
    numerator = numbers[0] + numbers[1]
    denominator = numbers[2] + numbers[3]
    answer = numerator / denominator
    print("Answer is" + format(round(answer, 2)))


def tasks4_11(answer_for_output_all):
    txt = "Hello, world!"

    def task4():
        new_txt = txt[2:5]
        print("New txt is: " + new_txt)

    def task5():
        s = txt[:]
        print(f'id = {id(s)}', s)
        s = txt[0:len(txt)]
        print(f'id = {id(s)}', s)
        s = txt
        print(f'id = {id(s)}', s)

    def task6():
        s = txt[:3]
        print(s)

    def task7():
        s = txt[2:]
        print(s)

    def task8():
        txt2 = "  Hello, world!  "
        counter = {'0': 0, '1': 0}
        i = 0
        while i < len(txt2):
            if txt2[i] == ' ':
                counter['0'] += 1
                i += 1
            else:
                break
        j = len(txt2) - 1
        while j > 0:
            if txt2[j] == ' ':
                counter['1'] += 1
                j -= 1
            else:
                break
        ans_txt = txt2[counter['0']: len(txt2) - counter['1']]
        print(ans_txt)

    def task9():
        new_txt = txt.upper()
        print(new_txt)

    def task10():
        new_str = ''
        for temp in txt:
            if temp == 'H':
                if temp == 'h':
                    new_str += 'j'
                new_str += 'J'
            else:
                new_str += temp
        print(new_str)

    tasks = {
        4: task4,
        5: task5,
        6: task6,
        7: task7,
        8: task8,
        9: task9,
        10: task10
    }
    if answer_for_output_all:
        for i in range(4, 11):
            print("Task " + format(i))
            tasks[i]()
            print("\n\n")
    else:
        print("Input number of task you want to do: ")
        num = int(input())
        tasks[num]()


tasks4_11(True)

numb = Decimal("0.1")
print(f'decimal 0.3 = {numb + numb + numb}')
print(f'float 0.3 {0.1 + 0.1 + 0.1}')
# task3()
# task2()
some_str = "Vladislavius"
idx = 0
symb = 'a'
while idx < len(some_str):
    if some_str[idx] == symb:
        print("your symbol in str (while)")
        break
    idx += 1
else:
    print('NO (while)')
for i in range(len(some_str)):
    if some_str[i] == symb:
        print('your symbol in str (for)')
        break
else:
    print('NO (for)')
some_str2 = some_str.isalpha()
print(some_str2)
some_str = "                   HELLO                           "
some_str2 = some_str.strip()
print(some_str2)
some_str = "Thank you\n for the music\nWelcome \nto the \njungle"
some_str2 = some_str.splitlines()
print(some_str2)
str_test = "aaaaa"
print(str_test)
str_test = "b" + str_test
print(str_test)