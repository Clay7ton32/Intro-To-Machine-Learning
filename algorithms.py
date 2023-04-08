def display_all(N, maxV):
    choice = []
    display_all_helper(N, maxV, choice)


def display_all_helper(N, maxV, choice):
    if N == 0:
        print(choice)
        return
    for i in range(1, maxV + 1):
        choice[N] = i
        display_all_helper(N-1, maxV, choice)



display_all(2, 3)

