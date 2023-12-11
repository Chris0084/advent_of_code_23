def is_number(digit):
    if (digit == "0" or digit == "1" or digit == "2" or digit == "3" or digit == "4" or digit == "5" or digit == "6" or digit == "7" or digit == "8" or digit == "9"):
        return True

def get_location_of_numbers(line):
    for digit in line:
        location = 0
        first_digit = 0
        second_digit = 0
        third_digit = 0
        if is_number(digit):
            first_digit
      


def day3():
    total = 0
    file = open("advent_of_code_files/day3_test_file.txt", "r")
    game_total = 0
    game_number = 1
    for line in file:
       temp_array = get_location_of_numbers(line)
       if reds_in_bag >= red_count and greens_in_bag >= green_count and blues_in_bag >= blue_count:
           total = total+game_number       
           game_number+=1
       else:                
            game_number+=1
    file.close()  
    print(f'Total is, {total}')  


def day2_part_b():
    total = 0
    file = open("advent_of_code_files/day2_input_file.txt", "r")
    for line in file:
        red_count = get_largest_colour_count(line, "red")   
        green_count = get_largest_colour_count(line, "green")   
        blue_count = get_largest_colour_count(line, "blue")   
        
        total = total + (red_count*green_count*blue_count)

    file.close()  
    print(f'Total is, {total}')     
