
def pas(n, sequence):
    for i in range(1, n-1):
        diff1 = abs(int(sequence[i-1])-int(sequence[i]))
        diff2 = abs(int(sequence[i])-int(sequence[i+1]))
        if diff2 != diff1:
            sequence.sort()
            for j in range(1, n-1):
                diff1 = abs(int(sequence[j - 1]) - int(sequence[j]))
                diff2 = abs(int(sequence[j]) - int(sequence[j + 1]))
                if diff2 != diff1:
                    return 'non-arithmetic'
            return 'permuted arithmetic'
    return 'arithmetic'


n = int(input())
ran = [i for i in range(n)]
numbers = list(map(lambda x: input().split(' '), ran))
for seq in numbers:
    seq = [int(i) for i in seq]
    first = int(seq[0])
    rest = seq[1:]
    print(pas(first, rest))
