#  File: Radix.py

#  Description: Queues are used to order strings of lowercase letters and numbers.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/22/2022

#  Date Last Modified: 10/22/2022

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

    def __str__(self):
        return str(self.queue)


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    # The total number of passes required to sort the list is determined
    num_passes = 0
    for i in range(len(a)):
        if len(a[i]) > num_passes:
            num_passes = len(a[i])

    # Adds spaces at the end of the string so all the strings are of the length of the longest string
    for i in range(len(a)):
        if len(a[i]) < num_passes:
            a[i] = a[i] + (" " * (num_passes - len(a[i])))
    dictionary, queue_objects = prep_radix_sort(a)

    # i is the index of the passes
    i = num_passes - 1
    while i >= 0:
        # The queue is determined each time
        queue_objects = queue_helper(queue_objects, dictionary, i)
        i -= 1
    lst = []
    # All the spaces are removed from the words
    while queue_objects[36].is_empty() == False:
        str = queue_objects[36].dequeue()
        i = len(str) - 1
        while str[i] == " ":
            str = str[:i]
            i -= 1
        lst.append(str)
    return lst

def prep_radix_sort(a):
    # 97-122 is lower case letters. 48-57 is numbers. Dictionary is created
    dictionary = {}
    i = 48
    idx = 0
    while i <= 57:
        dictionary[chr(i)] = idx
        i += 1
        idx += 1

    i = 97
    while i <= 122:
        dictionary[chr(i)] = idx
        i += 1
        idx += 1

    # There are 26 letters + 10 digits + 1 to dequeue the numbers in all the queues and enqueue them
    queue_objects = []
    for i in range(37):
        b = Queue()
        queue_objects.append(b)

    # Adds all the strings from a to the last queue
    for i in range(len(a)):
        queue_objects[36].enqueue(a[i])
    return dictionary, queue_objects

def queue_helper(queue_objects, dictionary, index):
    # All the strings are dequeued from the last queue to the respective index based on the letter or the digit
    while queue_objects[36].size() > 0:
        str = queue_objects[36].dequeue()
        if str[index] == " ":
            queue_objects[0].enqueue(str)
        else:
            idx_queue = dictionary.get(str[index])
            queue_objects[idx_queue].enqueue(str)

    # The last queue is dequeued
    while queue_objects[36].is_empty() == False:
        queue_objects[36].dequeue()

    # The last queue is enqueued in the order of the the other queues and the other queues are dequeued
    for i in range(len(queue_objects) - 1):
        if queue_objects[i].is_empty() == False:
            while queue_objects[i].is_empty() == False:
                str = queue_objects[i].dequeue()
                queue_objects[36].enqueue(str)
    return queue_objects

def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()

