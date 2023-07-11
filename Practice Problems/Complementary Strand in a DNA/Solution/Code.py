
# Dictionary to map nucleotides to their complements
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the length of the string
    N = int(input())

    # Read the string S
    S = input()

    # Create an empty string to store the complementary strand
    complementary_strand = ""

    # Iterate over each nucleotide in the string S and append its complement to the complementary strand
    for nucleotide in S:
        complementary_strand += complement[nucleotide]

    # Print the complementary strand
    print(complementary_strand)
