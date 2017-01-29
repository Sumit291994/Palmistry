n=4


for i in range (1,100):
    s = str(i)+".txt"
    f = open(s,"r")
    s1=str(n+i)+".txt"
    f1 = open(s1,'w')
    f1.write(f.readline())
    f1.write(f.readline())
    f1.write(f.readline())
    f.close()
    f1.close()
    

   
