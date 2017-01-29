import os 


os.system('EdrawlineOnImage.py')
os.system('Ecroping.py')
os.system('EcountBluepixcels.py')

os.system('EdrawlineOnImage.py')
os.system('Ecroping.py')
os.system('EcountBluepixcels.py')

os.system('EdrawlineOnImage.py')
os.system('Ecroping.py')
os.system('EcountBluepixcels.py')


f = open('handshape.txt','r')
width = int(f.readline())
u = int(f.readline())
l = int(f.readline())
f.close()
r1 = u/float(width)
r2 = l/float(width)


# length equal
if (r1-r2)> -0.1 and (r1-r2) < 0.1:
    if(width < u):
        ff = open('Elements/earth.txt','r')
    else:
        ff = open('Elements/water.txt','r')

elif u > l :
     ff = open('Elements/air.txt','r')
elif l > u :
     ff = open('Elements/fire.txt','r')

data =  ff.read()
f = open('report.txt','w')
f.write(data)
f.close()
ff.close()
