import re
url = # Any Youtube URL
exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
s = re.findall(exp,url)[0][-1]
thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
print(thumbnail)
