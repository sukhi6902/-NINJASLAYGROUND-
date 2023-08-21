def lookAndSequence(n):
    sequence = ["1"]  # Initialize with the first term
    for _ in range(n - 1):
        next_term = generate_next_term(sequence[-1])
        sequence.append(next_term)
    return sequence

def generate_next_term(term):
    result = []
    count = 1
    for i in range(1, len(term)):
        if term[i] == term[i - 1]:
            count += 1
        else:
            result.append(str(count) + term[i - 1])
            count = 1
    result.append(str(count) + term[-1])
    return ''.join(result)

def takeInput():
    n = int(input().strip())
    return n

t = int(input().strip())  # Number of test cases
for _ in range(t):
    n = takeInput()  # Read the number of terms for this test case
    sequence = lookAndSequence(n)
    for term in sequence:
        print(term)

  https://www.codingninjas.com/studio/problems/look-and-say-sequence_9065115?challengeSlug=ninja-slayground
