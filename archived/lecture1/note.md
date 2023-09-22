# Data Type
- 整數 int
  > 100
- 浮點數 float
  > 123.45
- 複數 complex
  > 3+4j
- 字串 str
 > 
- 字節 bytes
- 字節陣列 bytearray
- 串列 list: 
元素是有序的, 特徵是中括號[ ], 使⽤索引位置可以存取元素
 ```
    a = [2, 7, 3.5, “Hello”]
    x = a[1] 
    y = b[1:3]
    z =d[1][0][2]
    b[0] = 42
  ```
- 序對 tuple: 
與list類似，最⼤的不同tuple是⼀種唯讀且不可
變更的資料結構，不可取代tuple中的任意⼀個
元素，因為它是唯讀不可變更的
``` 
    f = (2,3,4,5)
    g = ()
    h = (2, [3,4], (10,11,12))
```
- 集合 set:
set 的元素是無序的(誰前誰後沒關係), 沒有重複的元素，而且設定時的順序也不影響
```
    passMath = {"Tom", "John", "Mary", "Jimmy", "Summy", "Amy"}
    passEnglish = {"John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}
```
- 字典 dict:
key : value 為配對的資料項，若有多筆資料再
以逗號區隔開

# 型態轉換
• 我們在處理資料的時候，有些資料型別不是我們想要的，該怎麼處理？
• 資料型別轉換：型別(資料)
• 將 x 轉換為整數：int(x)
• 將 x 轉換為浮點數：float(x)
• 將 x 轉換為字串：str(x)
• 將 x 轉換為布林型別：bool(x)
• 型別轉換會在記憶體空間配置出新的物件，內容為轉換
後的結果