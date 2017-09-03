## 题目

来源：《Python编程：从入门到实践》
内容： 
>如何学习编写第一个程序，每个程序员都有不同的故事。我还是孩子是就开始学习变成了，当我的父亲在计算时代的先锋之一——数字设备公司（Digital Equipment Corporation）工作。我使用了一台简陋的计算机编写了第一个程序，这台计算机是父亲在家里的地下室组装而成的，他没有机箱，裸露的主板与键盘相连，显示器是裸露的阴极射线管。我编写的这个程序是一款简单的猜数字有习，其输出类似于下面这样。

效果：

![python_show1.png](http://upload-images.jianshu.io/upload_images/4988302-170b5dd48ff165b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 我的解法
```python
import random

num = random.randint(1,100)
one = "I'm thinking of a number! Try to guess the number,You are thinking of:"
print(one, end="")
while 1:
	guessNumber = input()
	guessNumber = int(guessNumber)
	if guessNumber > num:
		print("too high! Guess again:")
	elif guessNumber < num: 
		print("too low! Guess again:")
	else:
		print("That's it! You're smart")
		break
input("点击 enter 键退出")
```
## 注意
- print()默认换行，end="\n"  改为 end="" 
- python 六个基本类型Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Sets（集合）、Dictionary（字典）   没有布尔类型
- input() 为输入的默认为str ， Python 不用申明类型（Python是强类型，动态类型检测语言），但需要显示类型转换（与js不同）