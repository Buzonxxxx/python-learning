
# u Q1. 使⽤set型別完成下列問題: 本班期末考試
# u 數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy
# u 英⽂及格的有: John, Mary , Tony , Bob , Pony, Tom , Alice
# u 分別印出數學及格但英⽂不及格的名單，數學不及格
# 但英⽂及格的名單，兩科都及格的名單
# u 最後印出全班總共有幾個同學
passMath = { "Tom", "John", "Mary", "Jimmy", "Summy", "Amy" }
passEnglish = { "John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}



dic = {
  "Tom": [80, 100, 90, 95],
  "John": [100, 93, 75, 80]
}

listTom = dic["Tom"]
totalTom = listTom[0] + listTom[1] + listTom[2] + listTom[3]
avgTom = float(totalTom) / 4

listJohn = dic["John"]
totalJohn = listJohn[0] + listJohn[1] + listJohn[2] + listJohn[3]
avgJohn = float(totalJohn) / 4

print ("Tom\'s average grade is: ", avgTom)
print ("John\'s average grade is: ", avgJohn)