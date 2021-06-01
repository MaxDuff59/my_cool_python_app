# Open the file in read mode
text = open("shakespeare.txt", "r")
d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

print(d)

for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        cnt = Counter()
        cnt[word] += 1

print(cnt)