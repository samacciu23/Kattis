# source: https://open.kattis.com/problems/commercials
import time as t
import random as rd
import matplotlib.pyplot as plt


def best_profit(breaks):
    income = 0
    outcome = 0
    if len(breaks)==0:
        return max(profits)
    else:
        for i in breaks:
            income+=int(i)
            outcome+=20
            profits.append(income-outcome)
            # print(profits)
        return best_profit(breaks[1:])


# n_p = input().split()
# n = int(n_p[0])
# p = int(n_p[1])
# crowns_x_break = input().split()
lengths = []
times = []
for length in range(1, 900):
    breaks_lst = [rd.randint(5, 40) for i in range(length)]
    profits = []
    t0 = t.time()
    print(best_profit(breaks_lst))
    total_time = t.time()-t0
    print("Time: ", total_time)

    lengths.append(length)
    times.append(total_time)

plt.xlabel('List Length')
plt.ylabel('Execution Time (s)')
plt.plot(lengths, times, label='best_profit(breaks_lst)')
plt.show()

