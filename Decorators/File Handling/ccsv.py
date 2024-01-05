
import csv
# with open('mca.csv','w',newline='')as csvfile:
#      data=csv.writer(csvfile)
#      data.writerow(['id','name', 'mobile','email'])
#      data2=[
#         [1,'John',894574856,'john@gmail.com'],
#         [2,'Johne',894574856,'john1@gmail.com'],
#         [3,'Johnm',8894574856,'john2@gmail.com']
#      ]
#data.writerows(data2)
# with open('mca.csv','r') as csvfile:
#    data=csv.reader(csvfile)
#    for i in data:
#       print(i)
# with open('bca.csv','w',newline='') as csvfile:
#    feildnames=['id','name','mobile','email']
#    data=csv.DictWriter(csvfile,feildnames)
#    data.writeheader()
#    rows=[
#       {'id':1,'name':'ligitha','mobile':'987654236','email':'ligi@gmail.com'},
#       {'name':'anil','id':'05','mobile':'6362633985','email':'ani.l.ap.112@gmail.com'}
#    ]
#    data.writerows(rows)
with open('bca.csv','w',newline='') as csvfile:
   feildnames=['id','name','mobile','email']
   data=csv.DictWriter(csvfile,feildnames)
   data.writeheader()
   rows=[
       {'id':1,'name':'ligitha','mobile':'987654236','email':'ligi@gmail.com'},
       {'name':'anil','id':'05','mobile':'6362633985','email':'ani.l.ap.112@gmail.com'}
   ]
   data.writerows(rows)
with open('bca.csv','r')as csvfile:
   data=csv.DictReader(csvfile)
   for row in data:
      print(row['name'])