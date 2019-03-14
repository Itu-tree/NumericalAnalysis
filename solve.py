"""
sympyのsolverを使って1変数の方程式の解を求めます。
"""

from sympy import *

# 入力
print(
"""1変数の方程式の解を求めます
-----------------------------------------------------
使用できる演算子と関数と定数の例
(https://docs.sympy.org/latest/modules/functions/elementary.html 参照):
 + , - , * , ** ,
 Abs(x) , root(x,n) ,sqrt(x)
 sin(x) , cos(x) , tan(x),
 asin(x),acos(x) ,atan(x),
 exp(x) , log(x) , pi , E ,
 など
 注意：
 solver のない方程式は解けません！
-----------------------------------------------------
関数を入力して下さい（例　x**2 - x*3 + 2)"""
)

x = symbols("x")
fx = eval(input("f(x) = "))
equation = Eq(fx,0)
answer = solve(equation)
print(answer)