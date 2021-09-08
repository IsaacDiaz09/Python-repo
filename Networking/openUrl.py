import urllib.request

data = urllib.request.urlopen("http://data.pr4e.org/intro.txt")

for line in data:
    print(line.decode().rstrip())