path1 = "/Users/Zhisen/Downloads/paragraph_files/paragraph_1.txt"
path2 = "/Users/Zhisen/Downloads/paragraph_files/paragraph_2.txt"
outpath = "/Users/Zhisen/python-challenge/PyParagraph/paragraphs_output.txt"
with open(path1, 'r',encoding = "utf-8") as infile1, \
     open(path2, 'r',encoding = "utf-8") as infile2, \
     open(outpath, 'w') as outfile:
     p1 = infile1.read()
     p2 = infile2.read()
     output = outfile
     words = p1.split()
     word_count = len(words)
     sentences = p1.split('.')
     sentence_count = len(sentences)
     letter_list = []
     for word in words:
         for letter in word:
              letter_list.append(letter)
     letter_count = len(letter_list)
     print('Paragraph Analysis (paragraph_1)')
     output.write('Paragraph Analysis (paragraph_1)\n')
     print('------------------------------------------')
     output.write('------------------------------------------\n')
     print(f'Approximate Word Count: {word_count}')
     output.write(f'Approximate Word Count: {word_count}\n')
     print(f'Approximate Sentence Count: {sentence_count}')
     output.write(f'Approximate Sentence Count: {sentence_count}\n')
     print(f'Average Letter Count (per word): {letter_count/word_count: .11f}')
     output.write(f'Average Letter Count (per word): {letter_count/word_count: .11f}\n')
     print(f'Average Sentence Length (in words): {word_count/sentence_count: .1f}')
     output.write(f'Average Sentence Length (in words): {word_count/sentence_count: .1f}\n')
         
     words = p2.split()
     word_count = len(words)
     sentences = p2.split('.')
     sentence_count = len(sentences)
     letter_list = []
     for word in words:
         for letter in word:
             letter_list.append(letter)
     letter_count = len(letter_list)
     print('\n')
     output.write('\n')
     print('Paragraph Analysis (paragraph_2)')
     output.write('Paragraph Analysis (paragraph_2)\n')
     print('------------------------------------------')
     output.write('------------------------------------------\n')
     print(f'Approximate Word Count: {word_count}')
     output.write(f'Approximate Word Count: {word_count}\n')
     print(f'Approximate Sentence Count: {sentence_count}')
     output.write(f'Approximate Sentence Count: {sentence_count}\n')
     print(f'Average Letter Count (per word): {letter_count/word_count: .11f}')
     output.write(f'Average Letter Count (per word): {letter_count/word_count: .11f}\n')
     print(f'Average Sentence Length (in words): {word_count/sentence_count: .1f}')
     output.write(f'Average Sentence Length (in words): {word_count/sentence_count: .1f}\n')
