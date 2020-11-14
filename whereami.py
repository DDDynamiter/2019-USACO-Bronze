f = open('whereami.in', 'r', encoding='UTF-8')
File = f.readlines()
N = File[0]
letter0 = File[1]
letter = list(letter0)
letter.pop()
length = len(letter)
List = []
newlist = []
for i in range(int(N)):
    for n in range(int(N)):
        data = letter[n:n+i]
        List.append(data)
    for m in List:
        if m not in newlist:
            newlist.append(m)
    if len(newlist)==len(List):
        break 
    newlist.clear()
    List.clear()
# output
with open('whereami.out', 'w') as fout:
    string = str(i)
    fout.write(string)