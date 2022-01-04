
import csv
import math
with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

totalMarks=0
totalEnteries=len(file_data)

for marks in file_data:
    totalMarks+=float(marks[0])
mean=totalMarks/totalEnteries
print('mean is',mean)

square_list=[]
for number in file_data:
    a=int(number[0])-mean
    a=a**2
    square_list.append(a)
sum=0
for i in square_list:
    sum+=i
result=sum/totalEnteries
sd=math.sqrt(result)
print ('standard deviation is',sd)