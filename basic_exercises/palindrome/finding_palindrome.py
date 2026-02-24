name='madam'
reverse=""
for x in name:
    reverse=x+reverse
if name==reverse:
    print('palindrome')
else:
    print('not palindrome')