arr = [1,1,0,0,1,0,0,0,0,1,0]
streak = best = 0

for x in arr:
    if not x:
        streak+= 1
   
    else:
        streak = 0
    
    if streak>best:
        best = streak

print(best)