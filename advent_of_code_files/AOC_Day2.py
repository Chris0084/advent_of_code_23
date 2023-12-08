

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def get_largest_colour_count(line, colour):
    index = line.find(colour)
    count = 0
    while index >= 0:
        first_char = line[index-3]
        second_char = line[index-2]
        temp_count = int((first_char + second_char).strip())
        if temp_count > count:
            count = temp_count

        line = line[index+3:]
        index = line.find(colour)

    return count

def get_smallest_colour_count(line, colour):
    index = line.find(colour)
    count = 99
    while index >= 0:
        first_char = line[index-3]
        second_char = line[index-2]
        temp_count = int((first_char + second_char).strip())
        if temp_count < count:
            count = temp_count

        line = line[index+3:]
        index = line.find(colour)

    return count
    


def day2(reds_in_bag, greens_in_bag, blues_in_bag):
    total = 0
    file = open("advent_of_code_files/day2_input_file.txt", "r")
    game_total = 0
    game_number = 1
    for line in file:
        red_count = get_largest_colour_count(line, "red")   
        green_count = get_largest_colour_count(line, "green")   
        blue_count = get_largest_colour_count(line, "blue")   
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
