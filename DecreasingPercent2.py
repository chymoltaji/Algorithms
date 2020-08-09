def splitpercent(n):
    total = 100
    unit = total/n
    mid_low = n//2
    if n % 2 == 0:
        mid_high = mid_low - 1
    else:
        mid_high = mid_low
    prize_list = [0]*n
    prize_list[mid_low] = unit
    prize_list[mid_high] = unit
    for i in range(n):
        if i<mid_low:
            prize_list[i] = unit + abs(mid_low-i)*(total/n**2)
        elif i>mid_high:
            prize_list[i] = unit - abs(mid_high-i)*(total/n**2)

    print(prize_list)
    print("SUM: "+str(sum(prize_list)))

splitpercent(3)
splitpercent(5)
splitpercent(10)
splitpercent(20)
splitpercent(25)