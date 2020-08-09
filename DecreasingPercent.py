def split_percent(profit, n_prizes):
    total = 100 - profit
    n_prizes+=1
    unit = total//n_prizes
    prizes = {i:(unit+(n_prizes-i)*(unit/n_prizes)) for i in range(1, n_prizes)}
    sum = 0
    for j in range(1, n_prizes):
        sum += prizes[j]
        print(f"Prize at {j} is {prizes[j]}")
    print(f"-->SUM IS: {sum}")
    print(f"<<<PRIZES: {prizes}")


split_percent(40, 3)
split_percent(40, 5)
split_percent(40, 10)
split_percent(40, 20)
split_percent(40, 25)