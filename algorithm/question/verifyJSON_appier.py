
import datetime

jsonData = {
  "email": "song1234@kimo.com",
  "keywords": [
    "dailymotion",
    "dramaq",
    "創業",
    "一夜新娘",
    "趙薇",
    "劉嘉玲",
    "肖戰",
    "孫藝珍"
  ],
  "keywords frequency": {
    "dailymotion": -3, 
    "dramaq": 0,
    "一夜新娘": 2,
    "趙薇": 29482,
    "劉嘉玲": 10,
    "肖戰": 1,
    "孫藝珍": 4
  },
  "keywords recency": {
    "dailymotion": 5,
    "dramaq": 6,
    "一夜新娘": 5,
    "趙薇": 15,
    "劉嘉玲": 15,
    "肖戰": 32
  },
  "Keyword Recency Date": { # use date obj, now is 2021-02-06
    "創業": "2020-01-02",
    "dailymotion": "2021-02-04",
    "dramaq": "2021-02-03",
    "一夜新娘": "2021-02-04",
    "趙薇": "2021-02-01",
    "劉嘉玲": "2021-01-25",
    "肖戰": "2021-01-08"
  }
}

# // Get keywords
# // Get "keywords frequency", "keywords recency" and "Keyword Recency Date"
# // loop each key and verify its frequency, recency and recency Date
# // verify if frequency >= 0
# // verify if recency <= 12
# // verify if date < 6
def isValidJson(jsonData):
  isValid = True
  keyword = jsonData["keywords"]
  keywordFrequency = jsonData["keywords frequency"]
  keywordRecency = jsonData["keywords recency"]
  keywordRecencyDate = jsonData["Keyword Recency Date"]
  now_date = datetime.date(2021, 2, 6)  # mm-dd-yyyy

  for key in keyword:
    frequency = keywordFrequency.get(key, None)
    recency = keywordRecency.get(key, None)
    recencyDate = keywordRecencyDate.get(key, None)

    if (frequency is None or frequency < 0):
       print(f'The {key}\'s frequency: {frequency} is invalid')
       isValid = False

    if (recency is None or recency > 12):
      print(f'The {key}\'s recency: {recency} is invalid')
      isValid = False

    if (recencyDate is not None):
        date = datetime.datetime.strptime(recencyDate, "%Y-%m-%d").date()
        diff = (now_date - date).days
        if (diff > 6):
            print(f'The {key}\'s recency date: {recency} is invalid')
            isValid = False
    
    if (recencyDate is None):
       print(f'The {key}\'s recency date: {recency} is invalid')
       isValid = False

  return isValid

print(isValidJson(jsonData))