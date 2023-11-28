#!/usr/bin/python

import threading
import time
import csv
import spotifyy as child
import playlist as plChild
from csv import writer
ips = {}
accounts = {}
count = 0
with open('p.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=":")
    for row in reader:
      ips[count] = row[0]
      count += 1
# print(ips)
count = 0
with open('message.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=":")
    for row in reader:
      accounts[count] = row[0].split(':')
      count += 1
# print(accounts)
# Define a function for the thread

t = int(input("Enter the time in SEC: "))
url = input("please set complete url: ")
loop = int(input("How many times you want to  run (Total): "))
thread = int(input('How much thread you want to run at a time : '))
revisions = int(input('How many time you want to play from single account : '))
while int(loop) < int(thread):
   loop = input("How many times you want to  run : ")
   thread = input('how much thread you want to run at a time : ')

cat = input("Type P for playlist S for song: ")
# print(cat)
while 'p' != cat.lower() and 's' != cat.lower():
   print('You enter a wrong option.')
   cat = input("Type P for playlist S for song: ")

def wirteCSV(data):
   with open('faild.csv','a',newline='') as fd:
      newFileWriter = writer(fd)
      newFileWriter.writerow([data])
      # newFileWriter.writerow([data])

def run_thread( data, delay):
   # print(data['proxy'])
   # print('1')
   i = 0
   while i != data['revisions']:
      print(i, 'abc')
      obj = child.bot(data, delay)
      obj.login()

      try:
         obj.like()
      except:
         print('')
      try:
         print('follow')
         obj.follow()
         time.sleep(5)
      except Exception as e :
         print(e)
      i += 1

def run_thread_playlist( data, delay):
   i = 0
   while i != data['revisions']:
      # print('1')
      obj = plChild.bot(data, delay)
      obj.play()
      try:
         obj.song()
      except:
         wirteCSV(data['login'][0]+' , '+data['login'][1]+' ; '+data['proxy'][0]+' , '+data['proxy'][1])
         print(data['login'][0]+' , '+data['login'][1]+' ; '+data['proxy'][0]+' , '+data['proxy'][1])
      try:
         obj.like()
      except:
         print('')
      try:
         print('follow')
         obj.follow()
         time.sleep(10)
      except Exception as e :
         print(e)
      i += 1

i = 0
total = 0
while i != int(loop/thread):
   j = 0 
   my_threads = []

   while j != thread:
      data = {}
      data['login'] = accounts[total]
      data['proxy'] = ips[total]
      data['type'] = cat 
      data['threadName'] = "Thread-"+str(total)
      data['time'] = t
      data['url'] = url
      data['revisions'] = revisions
      try:
         # t = threading.Thread( run_thread, (data, 10, ) )
         if(cat == 's'):
            t = threading.Thread(target=run_thread, args=(data, t,))
            t.start()
            my_threads.append(t)
         if(cat == 'p'):
            t = threading.Thread(target=run_thread_playlist, args=(data, t,))
            t.start()
            my_threads.append(t)
         # print(data)
         total += 1
      except Exception as e:
         # print(e)
         print('error : '+str(i),j)
      j += 1
   for t in my_threads:
       t.join()
   i += 1




      

