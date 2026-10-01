def max_score(n):
    arr = [1]*n + [0] + [1]*n

    streak = best = 0

    for i in arr:
        if i:
            streak+= 1
        else:
            streak = 0

        if streak > best:
            best = streak

    return best

n = int(input('Enter number: '))
print('Best Streak:',max_score(n))