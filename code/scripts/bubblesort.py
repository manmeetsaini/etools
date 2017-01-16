#Bubble Sort
x= [5,1,4,2,8,25,39,-100,10,12,-200,100]
for i in range(len(x)-3):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i],x[i+1] = x[i+1],x[i]
        print (x)    
print ("final sorted array: ", x)
