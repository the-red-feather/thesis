# I dont know how to continuously read and write, so this scripts reads everything in memory 
file = './proposal/My Library.bib'
fileNew = './proposal/library.bib'


# read
with open(file, 'r', encoding='utf-8') as file:
    data = file.readlines()

# process
for i, line in enumerate(data):
    if 'abstract = ' in line: 
        data[i] = ''
    if 'file = ' in line: 
        data[i] = ''



# write
with open(fileNew, 'w+', encoding='utf-8') as file:
    for line in data:
        if line != '':
            file.write(line)