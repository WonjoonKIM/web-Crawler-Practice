import re


test_str="""
I have graduated an electronic technical high school
and I had worked a semiconductor company in an equipment maintenance departure.
However, I really wanted to be a researcher who invents new one and
tries fresh attempts rather than having stable jobs.
I boldly had stop my 3 years career in the enterprise
since I hoped to study in universities.
Finally, I could admit a computer science departure I want.
Now, I am satisfying my course and want to keep on my studying
in higher education institutes, especially based on Europe.
When I mention about quality as an exchange student,
I have dwelled in Only English Dormitory where I had to share a room
with an international student in my home school.
In there, I could experience some various cultures, religions,
life style and so on. These value experience could make me stay-well
with local people in abroad. Not only that,
I am really looking forward to share knowledge with international students."""

pattern=re.compile('[a-z]+')
pattern1=re.compile('[A-Z]')

c=pattern.findall(test_str)
d=pattern1.findall(test_str)


print(c)
print(d)

#대문자와 소문자 찾기
pattern3=re.compile('[a-zA-Z]') #a부터 z까지와 A부터 Z까지 포함된 것을 모두 찾는다.
pattern4=re.compile('[a-zA-Z]+')

e=pattern3.findall(test_str)
f=pattern4.findall(test_str)

print(e)
print(d)
