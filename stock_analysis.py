import pandas as pd
import numpy as np

cols=['eq','initial','highest','lowest','closing','ltp','num','val','unknown','extra']
data=pd.read_csv('C:/High Frequency Data/BHAVCOPY/Jan/20130101.csv',sep='|',header=None,names=cols,index_col=1)
comps=data['eq']
#comps=['HDFC','APOLLOTYRE','BASF']
count=0
values=[]
j=0
while j<len(comps) :
    values.append([])
    j+=1

data.head()

for i in range(1,32):
    try:
        print 'C:/High Frequency Data/BHAVCOPY/Jan/201301'+str(i).zfill(2)+'.csv'
        data=pd.read_csv('C:/High Frequency Data/BHAVCOPY/Jan/201301'+str(i).zfill(2)+'.csv',sep='|',header=None,names=cols,index_col=0)
 #       print 'Hi'
        count+=1
        j=0
        while j<len(comps):
                if(type(data['highest'])==type(data['highest'][comps[j]])):
                    values[j].append(data['highest'][comps[j]][0])
                else:
                    values[j].append(data['highest'][comps[j]])
                j+=1
 #           print comps[j],data['highest'][comps[j]]
    except:
#        print 'no'
        continue
    

j=0
factor=[]
while j<len(comps):
    temp=np.array(values[j])
    factor.append([temp.std(),comps[j]])
    j+=1
factor.sort()
print factor

i=0
print 'Rank','Comp','Factor'
while i<len(factor):
    print i+1,factor[i][1],factor[i][0]
    i+=1
    
