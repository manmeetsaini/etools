'''Sorted Search -  [A,B,C,D]  -- compare A>B ,A>C>A>D , B>C ,B>D -- replace values'''

x=[5,8,1,60,20,10,1,90,-100,10 , -200]

minvalue = x[0]
print ("MinValue: ",minvalue)

for i in range(len(x)):
    j=i+1
    for j in range(i+1,len(x)):
        
        print ("i: ",i,"j: ",j,"x: ",x)
        if x[i] > x[j]:
            x[j],x[i] = x[i],x[j]
            
print("Final Sorted result: " , x)    



# Reverse Sort

minvalue = x[0]
print ("MinValue: ",minvalue)

for i in range(len(x)):
    j=i+1
    for j in range(i+1,len(x)):
        
        print ("i: ",i,"j: ",j,"x: ",x)
        if x[i] < x[j]:
            x[j],x[i] = x[i],x[j]
            
print("Final Reverse Sort result: " , x)  
