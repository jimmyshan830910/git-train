num = []
while True:
    x = input("請輸入數字：")
    try:
        if not x.isdigit() and isinstance(x,float):
            break
        elif int(x) == 9999:
            break
    except:
        break    
    num.append(int(x))
print(min(num))