import sys

dictionary = [line.strip() for line in open("japanesedict.dict").readlines()]
dictionary.sort()
dictionary.reverse()

def maxmatch(sentence, dictionary):

# function to check whether the list is empty
        if sentence == '':
# returning the result
                return []
        for i in range(0, len(sentence)):
                firstword = sentence[0:-i]
                remainder = sentence[-i:]
                if firstword in dictionary:
                        return [firstword] + maxmatch(remainder, dictionary)

        firstword = sentence[0]
        remainder = sentence[1:]
        return [firstword] + maxmatch(remainder, dictionary)

fd = open(sys.argv[1])
line = fd.readline()

while line != '':
        print(' '.join(maxmatch(line.strip('\n'), dictionary)))

        line = fd.readline()


# run in code line cat japanesedict.txt | python3 maxmatch.py japanesedict.txt
