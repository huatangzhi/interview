import re
pattern = ('\w+:\w+')
tmp = ''
itext = ('and(or(name:equals("adam"),age:equals(32)), not(gender:equals("male")))')
text = tmp.join(itext.split())

print len(itext)
print len(text)




scankeywords=['(', ')' , ',']
list = []
start = 0
i = 0
while i < len(text):
    if text[i] in scankeywords:
        if text[i-1] not in scankeywords:
            list.append(text[start:i])
        list.append(text[i])
        i = i+1
        start = i
    else:
        i = i+1

finallist = []
j = 0
while j < len(list):
    if re.match(pattern, list[j]):
        strtmp =''.join(list[j:j+4])
        finallist.append(strtmp)
        j = j + 4
    else:
        finallist.append(list[j])
        j = j + 1



for i in finallist:
    print i