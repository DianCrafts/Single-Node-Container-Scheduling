#!/bin/bash/python3
import sys
import operator
import os


def min():
	minimum = 99999
	for i in content:
		if (int(i) < minimum):
			minimum = int(i) 

	f = open(output, "a")
	f.write(str(minimum)+'\n\n')
	f.close()
	# print(os.getcwd())
	# print(output)

def max():
	maximum = -99999
	for i in content:
		if (int(i) > maximum):
			maximum = int(i) 
	f = open(output, "a")
	f.write(str(maximum)+'\n\n')
	f.close()
	# print(os.getcwd())
	# print(output)



def average():
	sumOfNumbers = 0
	avg= 0
	for i in content:
		sumOfNumbers += int(i)
	avg = sumOfNumbers/len(content)
	f = open(output, "a")
	f.write(str(avg) + '\n\n')
	f.close()
	# print(os.getcwd())
	# print(output)




def sort():
	content.sort()
	f = open(output, "a")
	for i in range(len(content)):
		f.write(str(content[i])+'\n\n')
	f.close()
	# print(os.getcwd())
	# print(output)


def word_count():
    counts = dict()
    for word in content:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1) ,reverse=True)
    f = open(output, "a")
    f.write('\n')

    for index, tuple in enumerate(sorted_counts):
    	f.write(str(tuple[0])+ '\t' + str(tuple[1]) + '\n')
    f.close()
    # print(os.getcwd())
    # print(output)


method=sys.argv[1]
path=sys.argv[2]
output = sys.argv[3]


with open(path) as f:
    temp = f.readlines()
    
temp = [x.strip() for x in temp] 
content = [int(i) for i in temp]
 

if (method == 'min'):
	min()

if(method == 'max'):
	max()


if(method == 'avg'):
	average()

if(method == 'sort'):
	sort()

if(method == 'wc'):
	word_count()
