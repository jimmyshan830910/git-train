def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
 
    return fibo(n-1) + fibo(n-2)
 
if __name__ == '__main__':    
    
    while True:
        x = input("請輸入數字：")
        try:
            if not x.isdigit() or int(x) == 0:
                break
        except:
            break
        print(fibo(int(x)))