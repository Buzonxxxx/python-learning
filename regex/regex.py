# https://regex101.com/

import re

pattern = re.compile(r"[a-zA-Z].[a]")
string = 'search inside of this text please!'


print(pattern.search(string).group(0))
print(pattern.findall(string))
print(pattern.fullmatch(string))
print(pattern.match(string))

