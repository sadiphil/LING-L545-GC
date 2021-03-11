import sys
# tells the system what file will be used as the dictionary, defines the dictionary function
dictionary = [line.strip() for line in open("japanesedict.dict").readlines()]
# returns a list in a specific sorted manner 
dictionary.sort()
dictionary.reverse()

def maxmatch(sentence, dictionary):

# function to check whether the list is empty
        if sentence == '':
# returning the result
                return []
# look up the longest word within the range of a string, starting at the beginning of the string, which is marked by the use of 0. 
# and goes until the end of 'i' counting from the back of the string as designated by the negative mark.
# return the first word and add to the return a new maxmatch to the remainder after the last running in the same dictionary. Essentially, 
# keep looking up the longest word in the dictionary.
        for i in range(0, len(sentence)):
                firstword = sentence[0:-i]
                remainder = sentence[-i:]
                if firstword in dictionary:
                        return [firstword] + maxmatch(remainder, dictionary)
# the first word is the first word of the list 'sentence', which is designated by 0 because lists start at 0 in python, not 1.
# remainder tells python that the remainder will be the everthing after 0 in the list. The position of the colon is designating that its to the end of the list.
        firstword = sentence[0]
        remainder = sentence[1:]
        return [firstword] + maxmatch(remainder, dictionary)
# defining the fd or the file directory as opening the specific file designated by sys.argv
fd = open(sys.argv[1])
line = fd.readline()

# while line equals empty is false, print a space and join it into the iterable string. Line.strip allows us to remove the characters in 
# line that come before or after the new line.
while line != '':
        print(' '.join(maxmatch(line.strip('\n'), dictionary)))

        line = fd.readline()


# run in the terminal as: cat japanesedict.txt | python3 maxmatch.py japanesedict.txt
