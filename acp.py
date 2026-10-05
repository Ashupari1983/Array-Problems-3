def streak():
    points = [1,0,1,1,0,1,0,1]
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