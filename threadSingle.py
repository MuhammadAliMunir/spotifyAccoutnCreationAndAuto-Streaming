#!/usr/bin/python

import threading
import time
import csv
import spotifyySingle as child
from csv import writer
import random
ips = {}
accounts = {}
count = 0
with open('p.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
      ips[count] = row[0]
      count += 1
# print(ips)
count = 0
with open('message.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
      accounts[count] = row[0].split(':')
      count += 1
# print(accounts)
# exit()
# Define a function for the thread

t =  random.randint(25,35)
url = 'https://open.spotify.com/track/7sIVva9oRxs0vRJvVawcPe?si=oEpU3po3TjKD-e1Vk6p5bQ'
loop = int(input("How many times you want to  run (Total): "))
thread = int(input('How much thread you want to run at a time : '))
# revisions = int(input('How many time you want to play from single account : '))
revisions = 1
while int(loop) < int(thread):
   loop = input("How many times you want to  run : ")
   thread = input('how much thread you want to run at a time : ')


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
      data['threadName'] = "Thread-"+str(total)
      data['time'] = t
      data['url'] = url
      data['revisions'] = revisions
      try:
         # t = threading.Thread( run_thread, (data, 10, ) )
         t = threading.Thread(target=run_thread, args=(data, t,))
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




      

