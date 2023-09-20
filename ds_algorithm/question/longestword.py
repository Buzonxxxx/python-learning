def LongestWord(sen):
  word_list = sen.split()
  new_list = []
  final_word = ''
  for word in word_list:  
    for char in word:
      if char.isalnum():
        final_word += char
    new_list.append(final_word)
    final_word = ''
  
  maxLen = 0
  result = ''
  for word in new_list:
    if len(word) > maxLen:
      maxLen = len(word)
      result = word

  return result

# keep this function call here 
print(LongestWord("hello world"))
print(LongestWord("hel!@#!@$ world"))