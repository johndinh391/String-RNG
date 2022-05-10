import string as str
import random as rng
def main():
    print("Welcome to the Random String generator.")#introduce user to program
    print("You will input two numbers. The first is the minimum length of the string. The second will be the maximum length of the string.")#provide instructions
    print("The output will be a string that will fall between the two lengths provided.")
    first_input = input('Enter the first integer.\n')#input first integer
    second_input = input('Enter the second integer.\n')#input second integer
    first_input_int = int(first_input)#convert both inputs into integers
    second_input_int = int(second_input)
    if(first_input_int > second_input_int or first_input_int < 0 or second_input_int < 0):#check for incorrect values in either input
        print("Incorrect pairing.")
    alphabetlist = str.ascii_letters#list of letters, both capitalized and not
    string_result = ""#where the output will go
    int_between_range = rng.randint(first_input_int,second_input_int)#random number between integers provided
    for i in range(int_between_range):#from 0 to the random number
        string_result += rng.choice(alphabetlist)#append a random letter to the result
    print(string_result)#output it to terminal
main()