def streak():
    points = [1,5,3,0,8,0,2,3]
    streak = 0
    best = 0

    for i in points:
        if i > 0:
            streak += i
        else:
            streak = 0
        if streak>best:
            best = streak

    print('Streak:',streak,'Best:',best)

streak()