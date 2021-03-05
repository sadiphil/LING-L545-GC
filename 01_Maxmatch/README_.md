# implementation of code to run wer.py is listed below
# cat allows us to display the contests of a file without having to open the file for editing. cut, cuts
# a section of the line. 'f' delimits whats being cut by field. The grep command searches the file for
# a specified character and '-v' asks it to print what does not correspond to the search. Then we use 'sed' to stream edit and replace numbers with '@@@'. 'tr' will
# translate all new lines to spaces. Then 'sed' will search and replace the new '@@@ symbols  with a new line globally and stream editing any number of 
# spaces at the beginning of a line and 
# save this as the file name after '>'
# cat ja_gsd-ud-test.conllu | cut -f2 | grep -v '^#' | sed 's/^$/@@@/g' | tr '\n' ' ' | sed 's/@@@/\n/g' | sed 's/^ *//g' > ja_gsd-ud-test.reference
# python3 wer.py ja_gsd-ud-test.reference japanesehypothesis.txt
# output = Average WER 3603.673946429622 Line Count 543
# WER = 6.636600269667812
# Given that this is a percentage of error, 6.63 percent is pretty good because these means we were 93.37 percent accurate.


# Maxmatch is used to tokenise a text or corpus by processing the text character by character to try
# to find the boundary between two characters. Maxmatch uses a dictionary as input for the algorithm to 
# help determine how to tokenise the second text.
# Maxmatch is used to tokenise a text or corpus by processing the text character by character to try to find the boundary between two characters. 
# Maxmatch uses a dictionary as input for the algorithm to help determine how to tokenise the second text.To determine how good your tokeniser has done,
# we can implement another python script that will evaluate our method. WER measures the word error rate by comparing a reference text and the hypothesis 
# text. The reference text is the dictionary and the hypothesis text is the tokenised text.Then you add all of the WER percentages together 
# and divide it by the number of lines.
