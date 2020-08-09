def split_percent(profit, n_prizes):
    total_prizes = 100 - profit
    n_prizes+=1
    unit = total_prizes//n_prizes
    prizes = {i:(unit+(n_prizes-i)*(unit/(n_prizes))) for i in range(1, n_prizes)}
    sum_prizes = 0
    for j in range(1, n_prizes):
        sum_prizes += prizes[j]
        print(f"Prize at {j} is {prizes[j]}")
    if sum_prizes == total_prizes:
        correct = "\033[92m"+"CORRECT""\033[0m"
    else:
        correct = "\033[91m"+"INCORRECT"+"\033[0m"
    print(f"-->SUM IS: {sum_prizes} |||"+correct)
    print(f"<<<PRIZES: {prizes}")


split_percent(40, 3)
# split_percent(40, 5)
split_percent(40, 10)
# split_percent(40, 20)
# split_percent(40, 25)