import re


test_str=""" 0 1923  23423984 234 98234 239 4923 4239
                @%#*&^($&@  @(*#&($&@( & @&($&($&@(
                1 3 5 7  7 5 3 """

pattern=re.compile('[0-9]')
pattern1=re.compile('[0-9]+')

c=pattern.findall(test_str)
d=pattern1.findall(test_str)

#print(c) 하나의 숫자로 띄어서 출력
print(d) #덩어리 단위의 숫자로 출력
