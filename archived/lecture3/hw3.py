# -*-coding:UTF-8 -*-
# 字串作業練習 EX03_hw.py
#
# 條件1: 若有符合的字串，將其索引值印出 (全部印出， 並非印出第一個符合的索引值)
# 條件2: 最後印出 總共有 x 個"的", (若輸入的字為"的")
#
# 文字來源 http://technews.tw/2015/07/22/apple-watch-sales/

text = '''2015年7月21日蘋果公司發表2015年第二季財報，Apple Watch的銷售狀況和營收與iPod、
Beats耳機和機上盒化為「其他產品」統計，蘋果公司未公開這款產品的具體銷售狀況，各類研究機構對於
Apple Watch的銷量評估也大相徑庭，單季銷量從190萬台到430萬台不等，顯然 Apple Watch 的銷量並沒有達到市場預期。
在蘋果公司的財報會議上，CEO Tim Cook 沒有正面回應分析師有關 Apple Watch 銷量的問題，蘋果公司暫時不關注
Apple Watch 的銷量，重點是打造一個生態體系，為 2015 年的聖誕購物季做準備。之前曾有消息稱 Apple Watch
進入6月後日銷量暴跌，Tim Cook 表示這款產品在 6 月的銷量高於上市初期。
據市場研究公司 Canalys 的報告顯示，2015 年第二季 Apple Watch 的銷量大約為 430 萬台，憑藉這一款產品，
蘋果公司輕鬆地超過了 Fitbit、小米等廠商，在穿戴式裝置市場佔據領先地位。但 Apple Watch
在該季的銷量出現了下滑的趨勢，僅為 2015 年第一季 60%。Canalys 認為蘋果公司在穿戴式裝置市場表現出了強大的市場號召力，
Apple Watch 的銷售均價遠高於其他競爭對手，但還是創造了非常驚人的銷售業績，Apple Watch 的目標客戶主要是蘋果產品的忠實消費者，
普通消費者對於 Apple Watch 的興趣不大。隨著電子產品銷售旺季的到來，Apple Watch 的銷量有望反彈。
2015 年第二季蘋果公司「其他產品」總營收為 26 億美元，2014 年同期為 17 億美元，
這表明Apple Watch至少為蘋果公司帶來了 10 億美元的營收，據 Bloomberg 的資料顯示，
Apple Watch 的銷售均價為 499 美元，據此估算 Apple Watch 在 2015 年第二季的銷量至少為 190 萬台，
若產品均價高於 550 美元，則意味著蘋果公司只售出了大約 100 萬台 Apple Watch，與市場平均 400 萬台的預期相去甚遠。
以往蘋果公司在發表新品後，銷售初期就會及時公開產品銷量，Apple Watch 上市數月至今仍未公開任何官方銷售資料，
蘋果公司只是一再表示 Apple Watch 賣得很好。這樣反常的表現加深了外界對於 Apple Watch 銷量的質疑，
從 Tim Cook 在財報會議上的表態來說，Apple Watch 在 2015 年 6 月之後已經進入了供貨穩定期，
也就是說 Apple Watch 已經開始有庫存，對於一款上市 3 個月的新品而言，這不是一個好消息。'''

find_str = input('請輸入要找的字:')

startIndex = 0
while text.find(find_str, startIndex) != -1:
    findIndex = text.find(find_str, startIndex)
    print("符合的索引值為: %d" % (findIndex))
    startIndex = findIndex + 1

print("總共有 %d 個'的'" % (text.count(find_str)))
