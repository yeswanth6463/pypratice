###set###
s={10,20,40,50,60,60,"hello","water"}

print(s)
print(type(s))

set=eval(input("enter a input in set format: "))
print(type(set))
for i in set:
    for j in (2,10):
        print(i,end=" ")
# create a program count of vowels given string
def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string.lower():
        if char in vowels:
            count += 1
    return count


user_input = input("Enter a string: ")
result = count_vowels(user_input)
print(f"Number of vowels in the input string: {result}")
#create pattern program
n=int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
n1=int(input("n:"))
res=["even","odd"][n1%2]
print(res)
res=[10,20][0]
l=[1,4,6,7,8]
res=l.index(4)

print(res)



