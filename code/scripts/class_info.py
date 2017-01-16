#class info

class ClassName(object):                 #this is a new style of class 
     def __init__(self,user,password):
        self.user=name    #You can use self.var1 through out the class in all fns
        self.password=password    #this is a instance variable
        
    def fn1(self):
        pass

    def fn2(self,self.var1):
        pass
    
    def fn3(var2):         #static or class method.. with no self, class will not pass '
        pass                #variable .. to access use ClassnName.var2

    ClassName.var1  # this is class variable
    a.var1     #this is object variable

#to call function



 a= ClassName("admin","ShoreTel")   
a.fn1()
    
    
#for 1 in xrange(n) --- better memory efficiency and fast
    
