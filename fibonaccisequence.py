sequence = [1]
count = 0
n = int(input("Please enter the length of your sequence ")) - 1
for i in range(n):
    if len(sequence) > 1:
        sequence.append(sequence[count] + sequence[count + 1])
        count = count + 1
        n = n - 1
        print(sequence)
    else:
        sequence.append(1)