

swaps = 0

# Your Code Here
def bubble_sort(sequence):
    for i in range(len(sequence)-1, 0, -1):
        for num in range(i):
            if sequence[num] > sequence[num + 1]:
                global swaps
                swaps += 1
                sequence[num], sequence[num + 1] = sequence[num + 1], sequence[num]
    return sequence

sequence = [4, 3, 5, 0, 1]
result = (bubble_sort(sequence))

print(f"Final result: {result}")
print(f"Swaps: {swaps}")
