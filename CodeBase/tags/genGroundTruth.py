
from os import listdir
from os.path import isfile, join
import sys
import subprocess

def main():
    onlyfiles1 = [ f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1],f)) ]
    onlyfiles2 = [ f for f in listdir(sys.argv[2]) if isfile(join(sys.argv[2],f)) ]

    list1 = sorted(onlyfiles1)
    list2 = sorted(onlyfiles2)

    for index in range(len(list1)):
        path1 = sys.argv[1]+list1[index]
        path2 = sys.argv[2]+list2[index]
        param1 = "--database1="+str(path1)
        param2 = "--database2="+str(path2)
        subprocess.call(["python", "tags/measure_tag_agility.py", param1, param2])

if __name__ == "__main__":main()
