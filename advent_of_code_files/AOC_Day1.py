
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def is_number(digit):
    if (digit == "1" or digit == "2" or digit == "3" or digit == "4" or digit == "5" or digit == "6" or digit == "7" or digit == "8" or digit == "9"):
        return True

def read_digit(digit):
    if is_number(digit):
        return int(digit)
    return 0

def array_of_numbers(word):
    num_array = []
    for x in word:
        if is_number(x):
            num_array.append(read_digit(x))

    return num_array





def day1():
    total = 0
    file = open("advent_of_code_files/day1_input_file.txt", "r")
    for word in file:
        numbers_array = array_of_numbers(word)
        first_digit = numbers_array[0]
        second_digit = numbers_array[-1]    
        two_digit_value = int(str(first_digit) + str(second_digit))
        total = total + two_digit_value

           

    file.close()  
    print(f'Total is, {total}')  
