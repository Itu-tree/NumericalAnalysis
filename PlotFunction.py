# 入力した１変数の関数をplotします。

from sympy import *


# 入力
print(
"""1変数の関数をplotします。
-----------------------------------------------------
使用できる演算子と関数と定数の例
(https://docs.sympy.org/latest/modules/functions/elementary.html 参照):
 + , - , * , ** ,
 Abs(x) , root(x,n) ,sqrt(x)
 sin(x) , cos(x) , tan(x),
 asin(x),acos(x) ,atan(x),
 exp(x) , log(x) , pi , E ,
 など
-----------------------------------------------------
関数を入力して下さい（例 2*x*sin(pi+x**2))"""
)
x = symbols("x")
fx = eval(input("f(x) = "))
# fx = eval("関数")
# 関数のplot
print("定義域を入力してください ( a < x < b)")
a = eval(input("a = "))
b = eval(input("b = "))


# plot(expr1, expr2, ..., range, **kwargs)
# https://docs.sympy.org/latest/modules/plotting.html
# color = "b", (1.0,0,0),#e41a1c'
plot(fx,(x,a,b),line_color="b",xlabel="x",ylabel="y",title=str(fx),legend=True) 

