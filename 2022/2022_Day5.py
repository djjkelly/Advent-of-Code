
import codecs
import csv
import re

# create a list of lists containing the initial stack of boxes
with codecs.open("2022/2022_Day5.csv",'r',encoding='utf-8-sig') as input:
    csv_reader = csv.reader(input)
    array = []
    for row in csv_reader:
        first_element = row[0]
        list = []
        for column in range(9):
            list.append(first_element[1+column*4])
        array.append(list)


# create a list of instructions from the txt file with strings
box_number_list =[]
initial_locations_list = []
destination_locations_list = []
with open("2022/2022_Day5instructions.txt") as instruction_text:
    for line in instruction_text:
        extracted_numbers = re.findall(r'\b\d+\b',line)
        box_number_list.append(extracted_numbers[0])
        initial_locations_list.append(extracted_numbers[1])
        destination_locations_list.append(extracted_numbers[2])
        if len(extracted_numbers)>3:
            print("Error on line "+line+": too many numbers in instruction text")
        if len(extracted_numbers)<3:
            print("Error on line "+line+": too few numbers in instruction text")

for j in range(len(array)):
    print(array[j])

# actually move the boxes from one part of the array to another
for line in range(len(box_number_list)):
    box_number = int(box_number_list[line])
    initial_location = int(initial_locations_list[line])
    destination_location = int(destination_locations_list[line])
    print("Moving " + str(box_number) +" boxes from stack " + str(initial_location) + " to stack " + str(destination_location))

    for box in range(box_number):

        #identify the drop required by the crane - how far from the height of the highest stack
        for drop in range(len(array)):
            if array[0][destination_location-1].isalpha():
                array.insert(0,[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
            if array[drop][destination_location-1].isalpha() or array[drop][destination_location-1].isnumeric():
                new_drop = drop
                break
        
        if len(array)-drop < 0:
            break

        for i in range(len(array)-1):
            # identify crate at top of stack
            if array[i][initial_location-1].isalpha():
                crate = array[i][initial_location-1]
                print("The crate to be moved is " + crate)
            # remove box from initial_location
                array[i][initial_location-1]=' '            
            # add box to destination_location
                array[new_drop-1][destination_location-1]=crate
                break
    for j in range(len(array)):
        print(array[j])

# return a string to record the top crate on each stack
return_string = ""
for j in range(9):
    for i in range(len(array)):
        if array[i][j].isalpha():
            return_string+=array[i][j]
            break
print(return_string)
