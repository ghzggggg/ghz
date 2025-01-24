import re
str1 = '@明日科技 @扎克伯格 @盖茨'
pattern = r'\s*[@]'
list = re.split(pattern,str1)
for item in list:
    if item !="":
        print(item)