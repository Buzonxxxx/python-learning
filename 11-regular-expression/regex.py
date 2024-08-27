# https://regex101.com/

import re

pattern = re.compile(r"[a-zA-Z].[a]") # 匹配a-z一個字母（可以是大寫或小寫），然後是任意一個字符，最後再匹配一個字母a
string = 'search inside of this text please!'

print(pattern.search(string).group(0))
print(pattern.findall(string)) # ['sea', 'lea']
print(pattern.fullmatch(string))
print(pattern.match(string))

