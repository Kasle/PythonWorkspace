import praw

r = praw.Reddit('Sale Finder by /u/synergexrogue')

sub = r.get_subreddit('gamedeals')

lookList = open("LL.txt", 'r')
LL = lookList.readlines()
lookList.close()

blacklist = []

for i in LL:
    if i.strip().lower()[0] == "-":
        blacklist.append(i)

emmsg = ""

for post in sub.get_new():
    skip = False
    for i in blacklist:
        if i.strip().lower()[1:] in post.title.lower():
            skip = True
    if skip:
        continue
    for i in LL:
        if i.strip().lower()[0] == "-":
            continue
        if i.strip().lower() in post.title.lower():
            tmp = ""
            for j in post.title:
                if j.lower().strip() in "abcdefghijklmnopqrstuvwxyz1234567890-=`~!@#$%^&*()_+[]{}\\;:,./<>?":
                    tmp+=j
            emmsg+=(i.strip() + ": " + tmp + " : --> " + post.url + "\n")

OUT = open('FOUND.txt', 'w')

OUT.write(emmsg)

OUT.close()
