f = open('word.in', 'r', encoding='UTF-8')
File = f.readlines()
Data = File[0].split()
N = int(Data[0])
K = int(Data[-1])
words = File[-1].split()
final_list = []
i = 0
with open('word.out', 'w') as fout:
    while i < N:
        final_list.append(words[i])
        length = 0
        for m in final_list:
            length = length + len(m)
        if length < K:
            i += 1
        if length == K:
            fout.write(" ".join(final_list)+"\n")
            final_list.clear()
            i += 1
        if length > K:
            final_list.pop()
            fout.write(" ".join(final_list)+"\n")
            final_list.clear()
    fout.write(" ".join(final_list)+"\n")
