
f = open("databases/index.txt","r")
n = int(f.read())
f.close()

x = []
ratios = []
for i in range (n-1):
    s = "databases/Emotion/"+str(i+1)+".txt"
    f = open(s,"r")
    x.append(int(f.readline()))
    f.close()

    s = "databases/Ratios/"+str(i+1)+".txt"
    f = open(s,"r")
    a = float(f.readline())
    ratios.append(float(f.readline()))
    f.close()

maxx = 0
minn = 100
        
for i in range (n-1):
    if x[i] ==1 and maxx<ratios[i]:
        maxx=ratios[i]
    if x[i]==3 and minn>ratios[i]:
        minn=ratios[i]

print maxx
print minn

f = open("datarule/Emotion.txt","w")
f.write(str(maxx)+'\n')   
f.write(str(minn)+'\n')   
f.close()
    
