# import re
# def multi_char_find(test_phase,test_pattern):
#     for pat in test_pattern:
#         print("search for pattern+> ", pat)
#         print(re.findall(pat,test_phase))
# test_phase="ssssdddddd --------------ssssssssssssddddddddddsssssss------ssssdddd"
# test_pattern=['s+']
# multi_char_find(test_phase,test_pattern)

import re

date = '2024-05-11'

# Corrected regular expression
res = re.search(r'\d{4}[/-]?(0[1-9]|1[0-2])[/-]?(0[1-9]|[1-2]\d|3[0-1])', date)

if res is not None:
    print("Match found")
else:
    print("No match found")

















# message='patterns serching pattern'

# res =re.search('pattern',message)
# if res!=None:
#     print("match found")
# else:
#     print("no match found")
    
# res2=re.findall('pattern',message)
# print(res2)

# res3=re.findall(r'pat{7}',message)
# if res3!= None:
#     print("match found")
# else:
#     print("not found")


# import re

# email= input("enter a email: ")

# res=re.search(r'[a-zA-z0-9]+@[a-zA-Z]+\.(com|edu|in|org|email)',email)

# if res!=None:
#     print("valid email")
# else:
#     print("not found")