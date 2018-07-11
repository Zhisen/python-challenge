import re
path1 = "/Users/Zhisen/Downloads/paragraph_files/paragraph_1.txt"
path2 = "/Users/Zhisen/Downloads/paragraph_files/paragraph_2.txt"
outpath = "/Users/Zhisen/python-challenge/PyParagraph/paragraphs_output.txt"
with open(path1, 'r') as infile1, \
     open(path2, 'r') as infile2, \
     open(outpath, 'w') as outfile:
     p1 = infile1.readlines()
     p2 = infile2
     output = outfile
     word_list = []
     for word in p1:
         word_list += word
     print(len(word_list))
      
     p1_list = re.split("(?<=[.!?]) +", p1) 
     #print(p1_list)