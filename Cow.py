f = open('gymnastics.in', 'r', encoding='UTF-8')
ranks = f.readlines()
trash = ranks.pop(0)
trash2 = trash.split()
total_count = 0
bulls = int(trash2[1])
times = int(trash2[0])
for bull1 in range(1, bulls+1):
    for bull2 in range(1, bulls+1):
        if bull1 != bull2:
            count = 0
            for r in ranks:
                rank = r.split()
                if rank.index(str(bull1)) < rank.index(str(bull2)):
                    count = count + 1
            if count == times:
                total_count = total_count + 1
with open('gymnastics.out', 'w') as fout:
    string = str(total_count)
    fout.write(string)