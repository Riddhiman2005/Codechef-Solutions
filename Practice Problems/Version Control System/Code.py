def count_tracked_and_ignored(N, M, K, ignored_files, tracked_files):
    ignored_set = set(ignored_files)
    tracked_set = set(tracked_files)

    tracked_and_ignored = len(ignored_set.intersection(tracked_set))
    untracked_and_unignored = N - len(ignored_set.union(tracked_set))

    return tracked_and_ignored, untracked_and_unignored

# Input
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    ignored_files = list(map(int, input().split()))
    tracked_files = list(map(int, input().split()))

    # Calculate and print the result
    result = count_tracked_and_ignored(N, M, K, ignored_files, tracked_files)
    print(*result)
