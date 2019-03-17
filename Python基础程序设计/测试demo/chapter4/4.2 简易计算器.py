def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b==0):
        print('ErrorInput!')
    else:
        return a/b

print("请选择运算类型：")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")
choose = input("请输入你的选择:")
a=int(input("输入第一个数字："))
b=int(input("输入第二个数字："))
if choose=='1':
    print(add(a,b))
elif choose=='2':
    print(sub(a,b))
elif choose=='3':
    print(mul(a,b))
elif choose=='4':
    print(div(a,b))
else:
    print('ErrorInput!')

'''
Note1:choose判断输入时需要将数字用单引号括起来，因为输入的choose虽然是数字，
但是计算机会默认其为字符串
Note2：if...elif...elif结构不能弄混，因为是在一个逻辑结构下面，若是if...if，则
最后会输出ErrorInput.
'''
