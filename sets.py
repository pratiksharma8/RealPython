s = "this is a sample string with many characters"
news = []
print(s.count("s"))
print(s)
print(set(s))
for i in s:
    if i not in news:
        news.append(i)
j_news = "".join(news)
print(news)
print(j_news)
newn = []

n = "3265418974719857623485766432569147983018095747836527713085743"
print(n.count("3"))
print(n)
print(set(n))
for i in n:
    if i not in newn:
        newn.append(i)
j_newn = "".join(newn)
print(newn)
print(j_newn)
