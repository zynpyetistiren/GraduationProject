import shutil, random, os, sys

sys.path.insert(0,'..')

dirpath = 'anime33k'
destDirectory = 'animeTest3k'

filenames = random.sample(os.listdir(dirpath), 3000)
for fname in filenames:
    srcpath = os.path.join(dirpath, fname)
    shutil.move(srcpath, destDirectory)
