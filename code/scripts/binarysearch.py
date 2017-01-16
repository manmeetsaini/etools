''' Binary tree - find median and compare median with target
if target < media , then high = median
if target > median ,then low = median 
'''
def binarySearch():
     #1A = [50 , 60 , 40 , 20 , 100 , 10 , 30 , 5 , 1,9 , 15]
     #B = sorted(A)
     B = [1,5,9,10,15,20,30,40,50,60,100]
     print (B)
     target = input("Select Number from List:  ")
     target= int(target)
     print (target)
     low = 0
     high = len(B)-1
     flag = False
     print ("values are low:%s and high:%s" % (low,high))
     while low <= high and flag==False:
          mid = int((low+high)/2)
          if B[mid] < target:
               low = mid+1
               print ("in if loop-low:","low is: ",B[low],"high: ", B[high])
               
                    
          elif B[mid] > target:
               high = mid
               print ("in elif loop- Low:",B[low],"high:",B[high])
          else:
               flag = True
               print ("I'm in else loop")
     if flag:
          print ("number is",B[mid], "at position",mid )
     else:
          print ("No. not in list")

userinput = "y"
while userinput == "y":
     binarySearch()
     userinput=input("continue - y or no:  ")
     if userinput == "no":
          break
