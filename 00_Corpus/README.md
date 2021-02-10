# This code has been written to hande text segmentation. That is, it can run a corpus of text, and based on the stipulations provided by the code, it will segment the corpus into
# lines. Each new sentence (however you want to define a sentence) will start a new line. So, the 
# code basically tells the segmenter when to start a new line. The initial code was not very 
# accurate. There were lists of numbers that triggered a new line, even though they should stay with
# the sentence that follows them, as those numbers are tagging the sentence's position in a specific 
# list. There was also the problem of '...' in two places within the text that I saw where a new line
# was started, which was not ideal in the specific contexts. There was also the issue of new lines
# that should have been created but were not. For example, oftentimes a semicolon or colon is the 
# connection of two independent clauses. So, I wanted to add those in as well. Below I talk a little
# more about the specific of where and why I added in specific characters to the code.
# Because I still had sentences that were being segmented in the middle instead of at the end, I wanted to expand my list of tokens for 'if token in []'
# following 'elif token[-1] == '.':'. By doing this, I can exclude phrases, abbreviations, elipses, etc. that end in a '.' but do not mark the end of a sentence.
# Because I was working with French, I added the abbrevations 'Mlle.' and 'Mdme.'. I also added 'k.g.' as that is a measurement frequently used in Europe and a ":" as those are
# frequently followed by lists and do not signal the end of a sentence.
# Following suggestions from Mikheev (2002), I also included elipses and then ran it to see what the new output would be. There were still some issues, which prompted me to
# add some strage combinations in the same subset. Mikheev (2002) mentioned that errors frequently occur because many corpora like Wikipedia have typos or ungrammatical
# sentences, and that's what I found here as well. There were cases where there was a '.' for  no reason, followed by several spaces, and finally followed by a comma. So, I 
# added to the subset some '.'s followed by spaces, followed by commas. This fixed that issue. I also had to add a ':' followed by spaces, followed by a comma, for the same reason.
# I also added a semicolon to the list 'if token[-1] in '!?;': |  sys.stdout.write(token + '\n')' as this tells the system for which punctuation marks signal the end of a sentence.
# Then tells the system to add a new line. The last problem I had was that numbers in a numbered list were on separate lines. I could have added each individual number to the
# 'if token in [ ]' subset mentioned above, but there was an easier way to do this. At the top of the screen, I added ', re' after 'import sys' which means 'all expressions'.
# This allowed me to add this: elif re.findall('[0-9]+\.', token): | sys.stdout.write(token + ' '). This asks the program to find all strings where there is one or more of any number
# 0-9 which is followed by a period, and mark is as an exception to the rule of breaking the line after a '.'. I belive that those were all of the changes that I made. Based on the
# small portion of the text that the segmenter.py was run on, it fixed all of the errors. However, if 
# it was being run on the whole corpus, more changes would need to be made.
# For example, it is completely possible for an abbreviation like k.g. to end a sentence. In this
# case, my current code would not be sufficient to account for this. For the held-out text, it seems
# like the additions made did a nice job of segmenting the text in a way that I felt was the most
# logical. 
