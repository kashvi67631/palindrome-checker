#palindrome checker
s=input('enter a word to check if it is palindrome or not')
k=s[::-1]
if s==k:
    print("Yes! it's palindrome")
else:
    print('No')
