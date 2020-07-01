import shutil, random, os, sys

sys.path.insert(0,'..')

dirpath = 'real100k'
destDirectory = 'realTrain7k'

filenames = random.sample(os.listdir(dirpath), 7000)
for fname in filenames:
    srcpath = os.path.join(dirpath, fname)
    shutil.move(srcpath, destDirectory)
