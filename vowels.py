count = 0 
vowels ='aeiouy'
name = input('Please enter your name')
for chars in name : 
    if chars in vowels : 
       print(chars,sep=',l')
       count = count + 1 
print(count)
