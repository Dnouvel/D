#This program will:
# 1- merge all text files in a folder into a certain allfiles.txt
# 2- Return a file (f_count_all.txt) with the list of all words and their frequencies (comma separated)

# 1- merging files

from glob import glob

txt_mask = r'C:\Users\DDNOU\Downloads\Text Mining\TBBTCorpus-master\TBBTCorpus-master\preprocessing\raw_corpus\*.txt'
filenames = glob(txt_mask)

#for fn in txt_names:
    
with open('allfiles.txt', 'w',errors='ignore') as outfile:
    for fname in filenames:
        with open(fname, 'r',encoding='cp437') as infile:
            #for line in infile:
            outfile.write(infile.read())
            infile.close()
outfile.close()

# 2- word list and frequency using re
import re
frequency = {}

document_text = open('allfiles.txt', 'r', encoding='cp437')

text = document_text.read().lower()
pattern = re.findall(r'\b[a-z]{2,15}\b', text)
for word in pattern:
     count = frequency.get(word,0)
     frequency[word] = count + 1
frequency_list = frequency.keys()

f=open('f_cout_all.txt','w', errors='ignore')
   

for words in frequency_list:
    f.write(words+';'+str(frequency[words])+'\n')
    
f.close()
