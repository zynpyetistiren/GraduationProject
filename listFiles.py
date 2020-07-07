from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('data/realData/realTrain7k/') if isfile(join('data/realData/realTrain7k/', f))]


file = open("data/trainNew.txt","a")
for f in onlyfiles:
    file.write("realTrain7k/")
    file.write(f)
    file.write("\n")
    print(f)
file.close