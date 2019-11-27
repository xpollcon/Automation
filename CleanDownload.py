from os import listdir
from os.path import isfile, join, splitext
path="/Users/xpollcon/Downloads"
for f in listdir(path):
    if isfile(join(path, f)):
        print splitext(f)[1]
