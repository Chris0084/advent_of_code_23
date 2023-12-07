
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def is_number(digit):
    if (digit == "0" or digit == "1" or digit == "2" or digit == "3" or digit == "4" or digit == "5" or digit == "6" or digit == "7" or digit == "8" or digit == "9"):
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

def convert_text_to_number(word):
    new_word = word.replace("zerone", "01")
    new_word = new_word.replace("oneight", "18")
    new_word = new_word.replace("twone", "21")
    new_word = new_word.replace("threeight", "38")
    new_word = new_word.replace("fiveight", "58")
    new_word = new_word.replace("eightwo", "82")
    new_word = new_word.replace("eighthree", "83")
    new_word = new_word.replace("nineight", "98")
    new_word = new_word.replace("one", "1")
    new_word = new_word.replace("two", "2")
    new_word = new_word.replace("three", "3")
    new_word = new_word.replace("four", "4")
    new_word = new_word.replace("five", "5")
    new_word = new_word.replace("six", "6")
    new_word = new_word.replace("seven", "7")
    new_word = new_word.replace("eight", "8")
    new_word = new_word.replace("nine", "9")
    new_word = new_word.replace("zero", "0")
    return new_word



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


def day1_part_b():
    total = 0
    file = open("advent_of_code_files/day1_input_file.txt", "r")
    for word in file:
        word = convert_text_to_number(word)
        print(word)
        numbers_array = array_of_numbers(word)
        first_digit = numbers_array[0]
        second_digit = numbers_array[-1]    
        two_digit_value = int(str(first_digit) + str(second_digit))
        total = total + two_digit_value

    file.close()  
    print(f'Total is, {total}')     
