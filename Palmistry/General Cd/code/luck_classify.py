
f = open("databases/index.txt","r")
n = int(f.read())
f.close()

x = []
ratios = []
for i in range (n-1):
    s = "databases/Luck/"+str(i+1)+".txt"
    f = open(s,"r")
    x.append(int(f.readline()))
    f.close()

    s = "databases/luma/"+str(i+1)+".txt"
    f = open(s,"r")
    a = float(f.readline())
    ratios.append(a)
    f.close()

maxx = 0
minn = 100
        
for i in range (n-1):
    if x[i] <=5 and maxx<ratios[i]:
        maxx=ratios[i]
    if x[i]>5 and minn>ratios[i]:
        minn=ratios[i]

print maxx
print minn

f = open("datarule/luck.txt","w")
f.write(str(maxx)+'\n')   
f.write(str(minn)+'\n')   
f.close()
    
