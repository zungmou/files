# 三门悖论 (Monty Hall Problem) 是一个概率问题，源自美国电视节目“Let's Make a Deal”中的一个游戏。游戏规则如下：
# 1. 主持人在三扇门后面放置了一个汽车和两只山羊。
# 2. 参赛者首先选择一扇门。
# 3. 主持人打开一扇没有汽车的门，显示出门后面的山羊。
# 4. 参赛者可以选择是否改变选择。
# 5. 如果参赛者选择了汽车所在的门，他就赢得了汽车；否则，他得到的是一只山羊。
# 三门悖论的解法是：如果参赛者改变选择，他赢得汽车的概率是2/3；如果不改变选择，他赢得汽车的概率是1/3。
# 本程序模拟了三门悖论的游戏过程，使用了Python的tkinter模块创建了一个简单的GUI界面。

import random
import tkinter
import tkinter.messagebox


class MontyHall:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("三门悖论（Monty Hall Problem）")

        self.car = random.randint(1, 3)
        self.choice = 0

        # 创建三个门和一个“选择”按钮
        self.door1 = tkinter.Button(
            self.window,
            text="门 1",
            width=10,
            height=5,
            command=lambda: self.choose_door(1),
        )
        self.door1.grid(row=0, column=0, padx=10, pady=10)
        self.door2 = tkinter.Button(
            self.window,
            text="门 2",
            width=10,
            height=5,
            command=lambda: self.choose_door(2),
        )
        self.door2.grid(row=0, column=1, padx=10, pady=10)
        self.door3 = tkinter.Button(
            self.window,
            text="门 3",
            width=10,
            height=5,
            command=lambda: self.choose_door(3),
        )
        self.door3.grid(row=0, column=2, padx=10, pady=10)
        # self.choice_button = tkinter.Button(
        #     self.window, text="选择", width=10, height=2, command=self.show_results
        # )
        # self.choice_button.grid(row=1, column=1, padx=10, pady=10)

        # 将窗口放在屏幕中央
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry("{}x{}+{}+{}".format(width, height, x, y))

        # 进入主循环
        self.window.mainloop()

    # 选择一个门
    def choose_door(self, door):
        self.choice = door
        self.show_results()

    # 显示结果
    def show_results(self):
        # 打开一个有山羊的门
        options = [1, 2, 3]

        # 如果汽车在其中一扇门，就不再打开它
        options.remove(self.car)

        # 如果用户已经选择了一扇门，就不再打开它
        if self.choice in options:
            options.remove(self.choice)

        # 随机打开一个有山羊的门
        goat = random.choice(options)

        switch_to = [x for x in options if x != self.choice][0]

        # 提示用户是否改变选择
        message = f"你选择了门 {self.choice}，门 {goat} 后面有一只山羊，你想要改变选择到门 {switch_to} 吗？"
        result = tkinter.messagebox.askyesno("三门悖论", message)

        # 显示最终结果
        if result:
            if switch_to == self.car:
                tkinter.messagebox.showinfo("三门悖论", "恭喜你！你赢得了汽车！")
            else:
                tkinter.messagebox.showinfo("三门悖论", "很遗憾，你得到了一只山羊。")
        else:
            if self.choice == self.car:
                tkinter.messagebox.showinfo("三门悖论", "恭喜你！你赢得了汽车！")
            else:
                tkinter.messagebox.showinfo("三门悖论", "很遗憾，你得到了一只山羊。")

        self.door1["text"] = "汽车" if self.car == 1 else "山羊"
        self.door2["text"] = "汽车" if self.car == 2 else "山羊"
        self.door3["text"] = "汽车" if self.car == 3 else "山羊"

        tkinter.messagebox.showinfo("三门悖论", "游戏结束。")

        # 重置游戏
        self.car = random.randint(1, 3)
        self.door1["text"] = "门 1"
        self.door2["text"] = "门 2"
        self.door3["text"] = "门 3"


MontyHall()
