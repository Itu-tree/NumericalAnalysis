"""
二分法で1変数n次方程式の近似解を１つ求めます。
"""
from sympy import *

LIMIT = 1e-20

# 関数の定義

def fxplot(fx) :
    pass
    # 関数のplot
    print("定義域を入力してください ( a < x < b)")
    a = eval(input("a = "))
    b = eval(input("b = "))
    plot(fx,(x,a,b),line_color="b",xlabel="x",ylabel="y",title=str(fx),legend=True) 



# 入力
print(
"""二分法で1変数の方程式の近似解の一つを求めます。
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
関数を入力して下さい（例　x**2 -sin(x) - exp(x) + 1)"""
)
fx = input("f(x) = ")
print("初期値を入力してください")
xm = float(eval(input("xm = ")))
xp = float(eval(input("xp = ")))

x = symbols("x")
fx = eval(fx)

count = 0
while fx.subs(x,xm)>= 0 :
    if count >= 3 :
        pass
        #fxplot(fx)
    
    print("f(x)<0となるxを入力して下さい")
    xm = float(eval(input("xm = ")))
    count += 1
    
while fx.subs(x,xp) < 0 :
    if count >= 3 :
        pass
        #fxplot(fx)
    
    print("f(x)>=0となるxを入力して下さい")
    xp = float(eval(input("xp = ")))
    count += 1


# 計算

n = 0
print("  %5s : %18s : %18s"   % ("n","xm","xp"))
print("  %5d : % .15f : % .15f" % (n,xm,xp))

while (xm-xp)*(xm-xp) > LIMIT:
    xmid = (xp+xm)/2
    n += 1
    if fx.subs(x,xmid) > 0 :
        xp = xmid
    else :
        xm = xmid
    
    print("  %5d : % .15f : % .15f" % (n,xm,xp))