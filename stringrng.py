import string as str
import random as rng
def main():
    print("Welcome to the Random String generator.")
    print("You will input two numbers. The first is the minimum length of the string. The second will be the maximum length of the string.")
    print("The output will be a string that will fall between the two lengths provided.")
    first_input = input('Enter the first integer.\n')
    second_input = input('Enter the second integer.\n')
    first_input_int = int(first_input)
    second_input_int = int(second_input)
    if(first_input_int > second_input_int or first_input_int < 0 or second_input_int < 0):
        print("Incorrect pairing.")
    a = str.ascii_letters
    d = ""
    f = rng.randint(first_input_int,second_input_int)
    for i in range(f):
        d +=rng.choice(a)
    print(d)
main()