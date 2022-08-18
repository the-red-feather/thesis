# I'm using Zotero for generating a bibtex, but that produces corrupt bibtex's sometimes, or in any case: 
# Latex doesnt like them. This fix works. I think the abstract & file can contain special characters, confusing latex.

# I dont know how to do streaming with python, 
# so this scripts reads everything in memory 

# old files 
# file = './P2/proposal/My Library.bib'
# fileNew = './P2/proposal/library.bib'

# P4 library adress
file = "./latex/My Library.bib"
fileNew = "./latex/library.bib"

# read
with open(file, 'r', encoding='utf-8') as file:
    data = file.readlines()

# process
for i, line in enumerate(data):
    # remove all abstracts
    if 'abstract = ' in line: 
        data[i] = ''
    # remove all attached files
    if 'file = ' in line: 
        data[i] = ''

# write
with open(fileNew, 'w+', encoding='utf-8') as file:
    for line in data:
        if line != '':
            file.write(line)

print("done!")