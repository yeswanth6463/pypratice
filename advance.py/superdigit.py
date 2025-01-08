class my_sups:
    def my_method(self, *param):
        res = 0
        for i in param:
            if isinstance(i, int):
                res += i
        
        while len(str(res)) != 1:  
            sum_digits = 0
            for digit in str(res):
                sum_digits += int(digit)
            res = sum_digits
        
        return res



m1 = my_sups()
rest = m1.my_method(True, 10, 'pusp', 23, 33.46, 435, [1, 2, 3, 4, 5], 67, False)
print(rest)  # Output: 4
print(rest)  # Output: 4
print(rest)  # Output: 4
print(rest)  # Output: 4
print(rest)  # Output: 4