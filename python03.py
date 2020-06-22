n = input("請輸入三角形的高度後，再空一格輸入1為實心，2為空心：")
n = n.split(' ')
x = int(n[0])
z = int(n[-1])
for i in range(x):
    # 印出空白
    for y in range(x-i-1):
        print(' ', end="")
 
     # 印出*
    for j in range((2*i)+1):
        # z = 1
        if z == 1:
            print("*", end="")
 
        # z= 2
        elif z == 2:
            if j == 0 or j == 2*i or i == x-1:
                print("*", end="")
            else:
                print(" ", end="")
        
    print()