data  = []
count = 0
i     = 0
with open('reviews.txt','r')as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            for word_count in f:
                data.append(word_count)
                i = i + len(word_count)
avg  = float( i / len(data))
print('檔案讀取完畢，總共有',len(data),"筆資料")
print("留言平均長度為:",avg)
