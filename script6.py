import re
#read from clipboard

f = open('line.txt')
content = []
currPara = str()
for line in f:
    if (line.strip() == ''):
        content.append(currPara)
        currPara = str()
    else:
        currPara += line
else:
    if (currPara != ''):
        content.append(currPara)

f.close()

def openCopy(orig):
    out = open('out.htm', 'w')
    f = open(orig)
    out.write(f.read())
    f.close()
    return out

out = openCopy('test.htm')

def placeLink(f, w1, w2):
    w1a = re.sub(',|\"', '', w1)
    w2a = re.sub(',|\"', '', w2)
    f.write('<a href="javascript:void(0)" onclick="load(\'' + w1a + '\', \'' + w2a + '\');">' + w1 + ' </a>')

for para in content:
    para = para.strip()
    if (para == ''):
        continue
    wordList = []
    currWord = str()
    for char in para:
        if (char == ' ' or char == '\n'):
            wordList.append(currWord)
            currWord = str()
        else:
            currWord += char
    wordList.append(currWord)

    out.write('<p>')
    for i in range(len(wordList) - 1):
        w1 = wordList[i]
        w2 = wordList[i+1]
        placeLink(out, w1, w2)

    placeLink(out, wordList[-1], '')
    out.write('</p>')


out.close()

print 'Done'
