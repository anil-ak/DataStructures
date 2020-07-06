
# Basic Program
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class Single_Linked_List:
    def __init__(self):
        self.data = None
    def print_list(self):
        value_to_be_printed = self.data
        while value_to_be_printed is not None:
            print(value_to_be_printed.data)
            value_to_be_printed = value_to_be_printed.next
    def number_of_elements(self):
        count = 0
        element = self.data
        while element is not None:
            count+=1
            element = element.next
        print(count)


# Create a empty list using Single_Linked_List class
my_week = Single_Linked_List()

#Create Nodes for each day
my_week.data = Node(data='Monday'); # Here defined the first element i.e. day1
day2 = Node(data='Tuesday')
day3 = Node(data='Wednesday')
day4 = Node(data='Thursday')
day5 = Node(data='Friday')
#Linking Day1 and Day2
my_week.data.next = day2
day2.next = day3
day3.next = day4
day4.next = day5

print(my_week)
my_week.print_list()
my_week.number_of_elements()


