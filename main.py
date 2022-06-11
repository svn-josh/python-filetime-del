import os
import datetime
import glob
import sys

#del_time = int(sys.argv[2]) 
#path = sys.argv[1] 
logging_path='C:/Users/yoshi/OneDrive/Desktop/FiFdel/logs/'

if not os.path.isdir(logging_path):
    os.mkdir(logging_path)
    print("Directory created")
else:
    print("Directory already exists")

today = datetime.datetime.today()
file=open(logging_path+datetime.datetime.today().strftime('%d-%m-%Y')+'.txt','a')


f = open('config.txt', 'r', encoding="utf-8")
for line in f:
    sections = line.split()
    path, del_time = sections
    os.chdir(path)
    for root,directories,files in os.walk(path):
        for name in files:
            t = os.stat(os.path.join(root, name))[8]
            filetime = datetime.datetime.fromtimestamp(t) - today
            #print(filetime.days)
            #print(del_time)
            if filetime.days <= int(del_time):
                print(os.path.join(root, name), filetime.days)
                file.write(os.path.join(root, name)+'\n')
                os.remove(os.path.join(root, name))
        break