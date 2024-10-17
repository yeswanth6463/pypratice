def right_angle(n):
    for i in range(n):
        for j in range(n):
            if i >= j:
                print("*", end=" ")
        print()

def right_top_angle(n):
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def left_angle(n):
    for i in range(n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def left_top_angle(n):
    for i in range(n):
        for j in range(n):
            if i + j <= n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def back_slash(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def forward_slash(n):
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


print("Enter a option")
print("1: Right angle\t2: Right top angle\t3: Left angle\t4: Left top angle\t5: Back slash angle\t6: Forward slash ")
n1 = int(input("Enter a option for selecting angle: "))

if n1 > 6:
    print("Invalid option")
else:
    n = int(input("Enter a number: "))
    match n1:
        case 1:
            right_angle(n)
        case 2:
            right_top_angle(n)
        case 3:
            left_angle(n)
        case 4:
            left_top_angle(n)
        case 5:
            back_slash(n)
        case 6:
            forward_slash(n)
