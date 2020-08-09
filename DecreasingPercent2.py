def split_percent(profit, n):
    total = 1-profit
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
    return prize_list

print(split_percent(0.4, 3))
print(split_percent(0.3, 5))
print(split_percent(0.1, 10))
print(split_percent(0.2, 20))
print(split_percent(0.2, 25))