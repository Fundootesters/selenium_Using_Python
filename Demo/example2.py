file = open("D:\\PythonAutomation\\q.txt", "r+")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
        list = list.append(wordcount)
print(word, wordcount)

list = list.append(wordcount)
print(list)
file.close()
