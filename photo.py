f = open('photo.in', 'r', encoding='UTF-8')
File = f.readlines()
N = int(File[0].split()[0])
L = File[-1].split()
cow_list = [x for x in range(1,N+1)]
final_list = []
cow = 0
with open('photo.out', 'w') as fout:
    while cow <= N-1:
        left = cow_list[cow]
        final_list.append(left)
        cow_list.remove(left)
        for i in L:
            num = int(i)
            left = num - left
            try:
                cow_list.remove(left)
            except ValueError:
                break
            else:
                final_list.append(left)
        if len(final_list) == N:
            final_list_new = [str(x) for x in final_list]
            fout.write(" ".join(final_list_new))
        final_list.clear()
        cow_list = [x for x in range(1,N+1)]
        cow += 1