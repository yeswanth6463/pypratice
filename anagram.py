#creat anagram
word1=input("enter a first word: ")
word2=input("enter a second word: ")

check_word1=set(word1)
check_word2=set(word2)
print(check_word1)
print(check_word2)

if check_word1==check_word2:
    print("anagram")
else:
    print("not anagram")
    
    
# check_word1 ^= check_word2
# print(check_word1)
sentence=input("enter a sentence")

cleandesentence = ''.join(c.lower() for c in sentence if c.isalpha())

unique_letters=set(cleandesentence)

print(cleandesentence)
print(unique_letters)

if len(unique_letters)==26:
    print("pangram")
else:
    print("not pangram")


    

    