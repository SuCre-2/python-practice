#题目：写一个返回矩阵面积的函数

def area(width,height):
    y= width*height
    if y >0:
        return y
    else:
        return None

w = int(input("请输入宽:"))
h = int(input("请输入高:"))

y = area(w,h)
if y is None:
    print("输入有误")
else:
    print(f"面积为：{y}")
    

    
