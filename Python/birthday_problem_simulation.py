# 生日悖论 (Birthday Problem) 是一个概率问题，即在一个房间里，如果有多少人，那么至少有两个人生日相同的概率超过50%？
# 该问题的答案是23人，这个问题的答案可以通过数学计算得到，也可以通过模拟实验得到。
# 以下代码通过模拟实验计算出了在不同人数下至少有两个人生日相同的概率。
# 代码中使用了matplotlib库绘制了概率随人数变化的折线图。
# 可以看到，当人数达到23人时，概率超过50%，符合生日悖论的结论。
# 参考：https://en.wikipedia.org/wiki/Birthday_problem


import matplotlib.pyplot as plt


def birthday_probability(n):
    p = 1
    for i in range(1, n):
        p *= (366 - i) / 366
    return 1 - p


x = list(range(2, 101))
y = [birthday_probability(i) * 100 for i in x]

plt.plot(x, y, "-o", color="royalblue", linewidth=2, markersize=6)
plt.xlabel("Number of people", fontsize=12)
plt.ylabel("Probability of two people sharing a birthday (%)", fontsize=12)
plt.title("Birthday paradox probability by number of people", fontsize=14)
plt.grid(alpha=0.4)
plt.show()
