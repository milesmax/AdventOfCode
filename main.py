# This is a sample Python script.
import csv

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def parse_input(csvinput):
    # Parses a csv with two columns of equal length. Creates two Ascending sorted lists of integers
    unsorted_left_list = []
    unsorted_right_list = []
    sorted_left_list = []
    sorted_right_list = []
    parsed_input = []

    # opens csv and seaparates each row into a list item
    with open(csvinput, newline='') as csvfile:
        inputreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in inputreader:
            #print(row[0], row[3])
            parsed_input.append((int(row[0]), int(row[3])))

    print('Input parsed')

    # Puts each column from last step into their own unsorted lists
    for item in parsed_input:
        unsorted_left_list.append(item[0])
        unsorted_right_list.append(item[1])

    sorted_left_list = sorted(unsorted_left_list)
    sorted_right_list = sorted(unsorted_right_list)

    distance_list = []
    for x, item in enumerate(sorted_left_list):
        distance_list.append(int(sorted_left_list[x] - sorted_right_list[x]))

    return distance_list


def add_distances(distancelist):
    sum = 0
    for item in distancelist:
        if int(item) < 0 :
            sum = sum + (int(item) * -1)
        else:
            sum = sum + int(item)
    return sum


def count_times_in_list(listToCount):
    # given a list, count the number of times each element in the list appears in another list
    resultsDict = {}
    for item in listToCount:
        resultsDict[item] = 0
        if item in :
            listsum = testlist.count(item)
            resultsDict[item] = listsum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parsed_input = parse_input('myinput.csv')
    print('Parsed input : ' + str(parsed_input))
    summed_distances = add_distances(parsed_input)
    print('Summed distances : ' + str(summed_distances))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# new comment here - changed to test github code editor
