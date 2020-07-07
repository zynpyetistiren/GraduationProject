import os

for count, filename in enumerate(os.listdir("realTest3k/")):
    dst = "P" + filename
    src = 'realTest3k/' + filename
    dst = 'realTest3k/' + dst

    # rename() function will
    # rename all the files
    os.rename(src, dst)
