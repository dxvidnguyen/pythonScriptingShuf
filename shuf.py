# Libraries used
import argparse
import sys
import random
import string


#---FUNCTIONS---

# input-range function    
def input_range_function(myList):
    # variables used a - d
    d = myList.split('-') #split the string into list of 2
    a = int(d[0]) #convert lower end to an int
    b = int(d[1]) #convert higher end to an int
    rangeList = [] #declare an array
    for c in range(a,b+1): #create list with numbes from a to b inclusive 
        rangeList.append(c)
    return rangeList

# head-count function
def head_count_function(num, myList):
    if (num >= len(myList)): #num of lines is same as orginal list
        return len(myList)
    else:   
        return num #num of lines is headcount amount    

# main function
if __name__=='__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('read_file', nargs='?', type=argparse.FileType('r'), help='read an input file') 
    parser.add_argument('-e', '--echo', nargs='*', help='treat each ARG as an input line')
    parser.add_argument('-i', '--input-range', metavar='LO-HI', help='treat each number LO through HI as an input line' )
    parser.add_argument('-n', '--head-count', type=int, metavar='COUNT', help='output at most COUNT lines')
    parser.add_argument('-r', '--repeat', action='store_true', help='output lines can be repeated')
    args = parser.parse_args()

    lines = [] #declare list called lines

    #first set of if/elif statements to determine if echo,input-range or read_file 
    if(args.echo):
        lines = args.echo
        #special case where it is just echo and nothing else
        if(args.echo and (not args.head_count) and (not args.repeat)):
            random.shuffle(lines)
            print(*lines, sep="\n")
            exit() #exit the whole program 
    elif(args.input_range):
        lines = input_range_function(args.input_range)
    elif(args.read_file):
        lines = args.read_file.readlines()
        lines = [str(item).strip() for item in lines] #strip file of excess lines 
        #special case where it is just read_file
        if(args.read_file and (not args.head_count) and (not args.repeat)):
            random.shuffle(lines)
            print(*lines, sep='\n')
            exit()

    #strip of extra spaces 
    lines = [str(item).strip() for item in lines] 

    #check if statment includes head_count function
    if(args.head_count):
        numLines = head_count_function(args.head_count, lines)
    else:
        numLines = len(lines)

    #check if statment includes repeat function
    if(args.repeat):
        if(args.head_count): #repeat is limited by head count 
            numLines = args.head_count #change to limit by head count 
            for x in range(0, numLines):
                random.shuffle(lines)
                print(lines[0])
        else: #no head count to limit so repeat goes on forever
            while(True):
                random.shuffle(lines)
                print(lines[0])
    else: #shuffling and printing when there is no repeat
        random.shuffle(lines)
        for x in range(0, numLines):
            random.shuffle(lines)
            print(lines[0])


