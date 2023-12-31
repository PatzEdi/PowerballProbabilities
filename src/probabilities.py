#Simple probability finder of numbers in Powerball lottery tickets:
import re
import time

#The lottery.txt dataset path:
lottery_dataset_path = ""

#Where to save the final file:
parsed_data_save_path = ""
#Read the file contents:
f = open(lottery_dataset_path)
data = f.readlines()
f.close()
#Main list to append to (normal numbers):
total_normal_numbers = []

#Main list to append to (powerball)
total_powerball_numbers = []

#Set the list (normal vocab):
number_vocab = lambda lst: list(set(lst))

#Function to find the numbers:
def findNumbers(line):
    pattern = r"(?<=,)(\d+\s\d+\s\d+\s\d+\s\d+\s\d+)(?=,)"
    matches = re.findall(pattern, line)
    return matches


def find_numbers_in_date(line):
    #Used to filter results and only gather data from 2015 and up (format changes)
    
    # Regular expression pattern to match dates in the format YYYY-MM-DD or DD/MM/YYYY
    pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b"
    # Find the date:
    found = re.findall(pattern, line)
    date = found[0]

    pattern = r"\d+"
    numbers = re.findall(pattern, date)

    i = 0
    for number in numbers:
        numbers[i] = int(number)
        i += 1

    month = numbers[0]
    day = numbers[1]
    year = numbers[2]

    return month, day, year


#For line in data, gather the number sequences:
for line in data:
    month, day, year = find_numbers_in_date(line)

    filtered = False
    if year == 2015:
        if month > 10:
            filtered = False
        if month < 10:
            filtered = True
        elif month == 10:
            if day >= 7:
                filtered = False
            elif day <= 7:
                filtered = True
    #Skip all years that are before 2015:
    elif year < 2015:
        filtered = True
    
    if filtered == False:
        try:
            #Get the numbers:
            numbersList = findNumbers(line)[0].split(' ')
            #Convert to integers:
            for element in range(len(numbersList)): numbersList[element] = int(numbersList[element])
            #Append the powerball numbers (Check if powerball is equal to or less than 26 to follow present day format)
            total_powerball_numbers.append(numbersList[-1])
            #Filter the first 5 numbers (in order to avoid bias) that were extracted from October 4, 2015 and up (Format changes from 59 to 69 5 normal numbers, 35 to 26 Powerball range.
            numbersList.pop(-1)
            total_normal_numbers.extend(numbersList)
        except:
            pass
    
number_vocab_normal = number_vocab(total_normal_numbers)

#Define a probabilities list:
probabilities = []
#Iterates through every number:
for number in number_vocab_normal:
    count = 0
    for integer in total_normal_numbers:
        if number == integer:
            count += 1
    percent_probability = (count/len(total_normal_numbers)) * 100
    #Append probability:
    probabilities.append(percent_probability)
    #print(f"Number: {number} , Probability: {percent_probability}")

#Verify that the sum adds up to 100%:
probability_sum = sum(probabilities)

print(f"\nSum of Probabilities (Numbers): {probability_sum}")
#Now, print a list in order of probabilities (Greatest to least)

#File lines to append to:
file_lines = ["Lottery Number Probabilities from 2010 to 2023 (Greatest to Least Probabilities) (Filtered October 4th, 2015 and Up: Format Changes)"]

while len(probabilities) != 0:
    iterator = 0
    for probability in probabilities:
        #Get the max probablity:
        max_probability = max(probabilities)
        #Then, find the position of where the max is:
        #If the probability at the placement of the iterator is equal to the max_probability:
        if probability == max_probability:
            matching_number = number_vocab_normal[iterator]
            print(f"Number: {matching_number} , Probability: {probability}")
            file_lines.append(f"\nNumber: {matching_number} , Probability: {probability}")
            #Pop the two values so new max values can be gathered:
            probabilities.pop(iterator)
            number_vocab_normal.pop(iterator)
        iterator += 1

#Write to a file:
file_lines.append(f"\n\nSum of Probabilities (Numbers): {probability_sum}\n")

#Let's do the powerball part of it :)

file_lines.append("\n\nPowerball Numbers")
powerball_vocab = number_vocab(total_powerball_numbers)


powerball_probabilities = []

for number in powerball_vocab:
    count = 0
    for integer in total_powerball_numbers:
        if number == integer:
            count += 1
    percent_probability = (count/len(total_powerball_numbers)) * 100
    powerball_probabilities.append(percent_probability)

powerball_probability_sum = sum(powerball_probabilities)

while len(powerball_probabilities) != 0:
    iterator = 0
    for probability in powerball_probabilities:

        #Get the max:
        max_probability = max(powerball_probabilities)

        if probability == max_probability:
            matching_number = powerball_vocab[iterator]
            file_lines.append(f"\nPowerball: {matching_number}, Powerball Probability: {probability}")
            #Then, pop the value:
            powerball_probabilities.pop(iterator)
            powerball_vocab.pop(iterator)
        iterator += 1

file_lines.append(f"\n\nSum of Probabilities (Powerball): {powerball_probability_sum}")

#Write the file:
f = open(parsed_data_save_path, 'w')
f.writelines(file_lines)
f.close()

#IMPORTANT Note: Only gather data from 2015 and above (format changes!) (fixed)