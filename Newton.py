"""
ニュートン法で1変数n次方程式の近似解を１つ求めます。
"""
from sympy import *

LIMIT = 1e-20

# 関数の定義

def fxplot(fx) :
    # 関数のplot
    print("定義域を入力してください ( a < x < b)")
    a = eval(input("a = "))
    b = eval(input("b = "))
    plot(fx,(x,a,b),line_color="b",xlabel="x",ylabel="y",title=str(fx),legend=True) 


# 入力
print(
"""ニュートン法で1変数の方程式の近似解の一つを求めます。
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
関数を入力して下さい（例　exp(-x) - x**2)"""
)

x = symbols("x")
fx = eval(input("f(x) = "))
print("初期値を入力してください")
x0 = input("x0 = ")
xold = float(eval(x0))
print("初期値は xm = % .15f です" % xold)


# 計算
df = diff(fx)

n = 0
print("  %5s : %18s" % ("n","x"))
print("  %5d : % .15f" % (n,xold))
    
while True :
    xnew = xold - fx.subs(x,xold) / df.subs(x,xold)
    n += 1
    print("  %5d : % .15f" % (n,xnew))
    #print("{:^8} : {:.15f}".format(n,xnew)) #TypeError:sin(x)のとき unsupported format string passed to Zero.__format__となる
    if Abs(xnew - xold) <= LIMIT * Abs(xnew): #相対誤差(%)
        break
    xold = xnew

#fxplot(fx)
