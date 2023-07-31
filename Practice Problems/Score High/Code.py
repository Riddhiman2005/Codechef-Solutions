def max_marks_guaranteed(N, NA, NB, NC, ND):
    """
    This function calculates the maximum number of marks Chef can guarantee in the exam.

  

    # Maximum number of correct answers for any answer type (A, B, C, or D).
    max_correct_answers = max(NA, NB, NC, ND)

    # Maximum number of marks Chef can guarantee = maximum number of correct answers.
    return max_correct_answers

# Input
T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Number of problems in the exam
    NA, NB, NC, ND = map(int, input().split())  # Number of correct answers for each answer type
    result = max_marks_guaranteed(N, NA, NB, NC, ND)  # Calculate the maximum marks Chef can guarantee

    print(result)  # Output the result for each test case
