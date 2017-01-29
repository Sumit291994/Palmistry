import Tkinter
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
from socket import *
from thread import *
import sys,os
import time
import Tkinter as tk
from PIL import ImageTk, Image
import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


global filename1
filename1 = "No Image Selected"
global ratios
ratios=""
global luma
luma="0"

global data1
data1=""

def close_window(root):
    root.destroy()

class newWindow(Tkinter.Toplevel):
    def __init__(self):
        Tkinter.Toplevel.__init__(self)
        self.geometry("450x650")
        self.title("Add Person")

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        frame1=Tkinter.Frame()
        frame1.grid(row=0,column=0, sticky='W',pady=5,padx=5)
        frame2=Tkinter.Frame()
        frame2.grid(row=6,column=0, sticky='W',pady=5,padx=5)

        #frame 1 settings
        
        #Event List location label
        self.file1 = Tkinter.StringVar()
        file_loc1 = Tkinter.Entry(frame1,textvariable=self.file1,state="disabled",fg="black",bg="light pink",borderwidth=3,width="45",font=('Arial', 10))
        file_loc1.grid(column="0",row="1",columnspan=4,padx="10",sticky='W') 
        self.file1.set("  Enter the Hand Image Path Here ")
        
        #button 'Browse1'
        browse_button1 = Tkinter.Button(frame1,text=u"Browse",bg="light green",width="12",command=self.BrowseButton1)
        browse_button1.grid(column="4",row="1",columnspan=2,padx="10",sticky='W')
        
      
        #Option button 'Male' and 'Female'
        self.Category = Tkinter.StringVar()
        Category_label = Tkinter.Label(frame1,textvariable=self.Category,fg="brown",bg="light blue",relief="ridge",width="18",font=('Arial', 10,'bold'))
        Category_label.grid(column="0",row="2",columnspan=2,padx="10") 
        self.Category.set("Select Category")
        self.var=IntVar()
        Male_button = Tkinter.Radiobutton(frame1,text=u"Male",variable=self.var,value=1)
        Male_button.grid(column="2",row="2",padx="10",sticky='W')
        Female_button = Tkinter.Radiobutton(frame1,text=u"Female",variable=self.var,value=2)
        Female_button.grid(column="3",row="2",padx="10",sticky='W')
        self.var.set(1)

        #button 'Train'/'Update Model'
        button_train = Tkinter.Button(frame1,state="normal",text=u"Update Model Rules ",bg="light green",command=self.Train,width="17",font=('Arial', 10,"bold"))
        button_train.grid(column="0",row="3",columnspan=2,padx="10",pady="5",sticky='W')

        #button 'Test'/'Predict'
        button_test = Tkinter.Button(frame1,state="normal",text=u"Predict",bg="light green",command=self.Test,width="12",font=('Arial', 10,"bold"))
        button_test.grid(column="2",row="3",padx="10",columnspan=2,pady="5",sticky='W')

        #button 'Trend Button'
        button_trend = Tkinter.Button(frame1,state="normal",text=u"Check Trend",bg="light green",command=self.Trend,width="11",font=('Arial', 10,"bold"))
        button_trend.grid(column="4",row="3",padx="10",columnspan=2,pady="5",sticky='W')

#        edu = Tkinter.Button(frame1,state="normal",text=u"Education ",bg="light grey",command=self.EducationLine,width="11",font=('Arial', 10,"bold"))
 #       edu.grid(column="0",row="4",padx="15",columnspan=4,pady="5",sticky='W')

  #      heart = Tkinter.Button(frame1,state="normal",text=u"Heart Line",bg="light grey",command=self.HeartLine,width="11",font=('Arial', 10,"bold"))
   #     heart.grid(column="1",row="4",padx="10",columnspan=2,pady="5",sticky='W')

    #    health = Tkinter.Button(frame1,state="normal",text=u"Health Line",bg="light grey",command=self.HealthLine,width="11",font=('Arial', 10,"bold"))
     #   health.grid(column="2",row="4",padx="10",columnspan=2,pady="5",sticky='W')

        
        marriage = Tkinter.Button(frame1,state="normal",text=u"Marriage Line",bg="light grey",command=self.MarriageLine,width="11",font=('Arial', 10,"bold"))
        marriage.grid(column="3",row="4",padx="10",columnspan=2,pady="5",sticky='W')

        luck = Tkinter.Button(frame1,state="normal",text=u"Luck Line",bg="light grey",command=self.LuckLine,width="11",font=('Arial', 10,"bold"))
        luck.grid(column="1",row="4",padx="10",columnspan=2,pady="5",sticky='W')

        #button 'Add New Person Data'
        button_update = Tkinter.Button(frame1,state="normal",text=u" Add New Person ",bg="light green",command=self.addPerson,width="15",font=('Arial', 10,"bold"))
        button_update.grid(column="2",row="5",padx="10",columnspan=4,pady="5",sticky='W')

        #button 'Element Finder'
        button_element = Tkinter.Button(frame1,state="normal",text=u" Element Finder",bg="light green",command=self.element,width="15",font=('Arial', 10,"bold"))
        button_element.grid(column="0",row="5",padx="10",columnspan=4,pady="5",sticky='W')

        #frame2 settings
        #Report label
        self.Report = Tkinter.StringVar()
        Report_label = Tkinter.Label(frame2,textvariable=self.Report,fg="brown",bg="light blue",relief="ridge",borderwidth=3,width="53",font=('Arial', 10,'bold'))
        Report_label.grid(column="0",row="0",padx="10") 
        self.Report.set("Report")
        
        #Activity Log
        self.act = Tkinter.StringVar()
        act_log = Tkinter.Label(frame2,textvariable=self.act,anchor="nw",bg="light yellow",fg="black",justify="left",relief="ridge",borderwidth=3,font=('Arial', 10),width="55",height="24")
        act_log.grid(column="0",row="1",sticky='W',padx="10",rowspan="6") 
        self.act.set("")
        
        #screen
        self.geometry("480x600")
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())


    def MarriageLine(self):
        print "Marriage"
        os.system('rotateMarriage.py')
        os.system('croping1.py')
        os.system('countWhitepixcels1.py')
        f = open('LineLength.txt','r')
        width = int(f.readline())
        f.close()
        f = open('MarriageLineLength.txt','r')
        l = int(f.readline())
        f.close()

        r1 = l/float(width)
        if r1>1:
            r1=2-r1
        print r1
       
    #    f = open('lumaLineLength.txt','a')
    #    abc="\n"
     #   f.write(abc)
      #  f.write(str(r1))
       # f.close()

    #    f = open('lumaLineLength.txt','r')
   ##     r2 = int(f.readline())
   #     f.close()
        global data1
        data1 = data1 + "\nLuck : "
        f = open("datarule/luck.txt","r")
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        f.close()

        global luma
        r2 = int(luma)
        
        if(float(r2)<=float(a)):
            data1 = data1 + "Great Luck Factor\n"
            f1 = open('databases/lucklong.txt','r')
            data1 = data1 + f1.readline()
            f1.close()
        elif float(r2)>=float(b):
            data1 = data1 + "Poor Luck Factor\n"
            f1 = open('databases/luckshort.txt','r')
            data1 = data1 + f1.readline()
            f1.close()
        else:
            data1 = data1 + "Average condition \n"

        data1=data1+"\n"
        
        data1 = data1+"\nMarriage : "
        f = open("datarule/marriage.txt","r")
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        f.close()

        if(float(r1)<=float(a)):
            data1 = data1 + "Stable Marriage\n"
            f1 = open('databases/marriagelong.txt','r')
            data1 = data1 + f1.readline()
            f1.close()
        elif float(r1)>=float(b):
            data1 = data1 + "Unstable Marriage\n"
            f1 = open('databases/marriageshort.txt','r')
            data1 = data1 + f1.readline()
            f1.close()
        else:
            data1 = data1 + "Average condition \n"
        data1 = data1+"\n"
        self.act.set(data1)

    def LuckLine(self):
        print "Luck"
        os.system('rotateLuck.py')
        os.system('croping1.py')
        os.system('countWhitepixcels2.py')
        f = open('LineLength.txt','r')
        width = int(f.readline())
        f.close()
        f = open('MarriageLineLength.txt','r')
        l = int(f.readline())
        f.close()

        r = l/float(width)
        if r>1:
            r=2-r
        
        print r
        global luma
        luma = r
        f = open('lumaLineLength.txt','w')
        f.write(str(r))
        f.close()
            
    def BrowseButton1(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        global filename1
        filename1 = askopenfilename()# show an "Open" dialog box and return the path to the selected file
        print(filename1)
        self.file1.set(filename1)

        
    def Train(self):
        data = "Work On Progress train"
        self.act.set(data)
        execfile('UpdateRule.py')
        f = open("datarule/Education.txt","r")
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        f.close()
        data = "Education:\n"+"<= "+a+"                \t \t Poor condition\n"+"> "+a+" and "+"< "+b+"  \t Average\n"+">= "+b+" \t \t \t Good condition\n"
        data = data + "--------------------------------------------------------\n"

        f = open("datarule/Emotion.txt","r")
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        data = data+ "Emotionally:\n" + "Below "+a+"\t \t \t Emotionally Stable\n"+"B/W "+a+" and "+b+" \t Average\n"+"Upper "+b+" \t \t \t Emotionally Weak\n"
        data = data + "--------------------------------------------------------\n"

        f = open("datarule/Health.txt","r")
        a = str(float(f.readline()))
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        data = data + "Health:\n"+"<= "+a+"                \t \t Poor condition\n"+"> "+a+" and "+"< "+b+"  \t Average\n"+">= "+b+" \t \t \t Good condition\n"
        data = data + "--------------------------------------------------------\n"

        f = open("datarule/luck.txt","r")
        b = str(float(f.readline()))
        a = str(float(f.readline()))
        f.close()
        data = data+"Luck:\n"+"<= "+a+"                \t \t Poor Luck Factor\n"+"> "+a+" and "+"< "+b+"  \t Average\n"+">= "+b+" \t \t \t Great Luck Factor\n"
        data = data + "--------------------------------------------------------\n"

        f = open("datarule/marriage.txt","r")
        b = str(float(f.readline()))
        a = str(float(f.readline()))
        f.close()
        data = data+"Marriage:\n"+"<= "+a+"           \t  \t   \t \t Unstable Marriage\n"+"> "+a+" and "+"< "+b+" \t\t \t Average Condition\n"+">= "+b+" \t\t \t \t Stable Marriage\n"
        data = data + "--------------------------------------------------------\n"


        self.act.set(data)

    def Test(self):
        data = "Predicting...."
        self.act.set(data)
        global filename1
        img = cv2.imread(filename1)
        edges = cv2.Canny(img,70,90)
        cv2.imwrite('edge.jpg',edges)
        
        execfile('run.py')
        f = open('LineLength.txt','r')
        width = int(f.readline())
        l1 = int(f.readline())
        l2 = int(f.readline())
        l3 = int(f.readline())

        r1 = l1/float(width)
        r2 = l2/float(width)
        r3 = l3/float(width)

        if(r1 > 1 ):
            r1= 2-r1
        if r2>1:
            r2=2-r2
        if r3>1:
            r3=2-r3

        global ratios
        ratios=str(r1)+"\n"+str(r2)+"\n"+str(r3)+"\n"

        data = "Ratios:   \nLine1: "+str(r1)+"   \nLine2: "+str(r2)+"   \nLine3: "+str(r3)+"\n"
      #  data = data + "--------------------------------------------------------\n"
        data = data + "\nPrediction\n--------------------------------------------------------\n"
        data = data + "Education : "
        f = open("datarule/Education.txt","r")
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        f.close()

        if(float(r1)<=float(a)):
            data = data + "Poor condition\nSince Education line is poor , so we can say that the person \n is poor in Education field , he should not persue higher study.\n"
        elif float(r1)>=float(b):
            data = data + "Good condition\nSince Education line is good , so we can say that the person \n is good in Education field , he should persue higher study.\n"
        else:
            data = data + "Average condition\nRatio is average,fairly strong education. \n "


        data = data + "\nEmotion : "
        f = open("datarule/Emotion.txt","r")
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        f.close()

        if(float(r2)<=float(a)):
            data = data + "Emotionally Stabled\n"
        elif float(r2)>=float(b):
            data = data + "Emotionally Weak\n"
        else:
            data = data + "Average condition : Emotionally stable and weak\n"

        data = data + "\nHealth Life : "
        f = open("datarule/Health.txt","r")
        a = str(float(f.readline()))
        a = str(float(f.readline()))
        b = str(float(f.readline()))
        f.close()

        if(float(r3)<=float(a)):
            data = data + "Poor Health\n"
        elif float(r3)>=float(b):
            data = data + "Good Health\n"
        else:
            data = data + "Average Health Condition\n"

        global data1
        data1=data
        self.act.set(data)
        

    def Trend(self):
        data = "Edge Detected ...."
        self.act.set(data)
        #execfile('checktrend.py')
        global filename1
        img = cv2.imread(filename1)
        edges = cv2.Canny(img,70,90)
        cv2.imwrite('edge.jpg',edges)

        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()


    def element(self):
         
         data = "Element Finder ...."
         self.act.set(data)
         global filename1
         img = cv2.imread(filename1)
         edges = cv2.Canny(img,70,90)
         cv2.imwrite('edge.jpg',edges)
         execfile('runElement.py')
         f = open('report.txt','r')
         data = f.read()
         self.act.set(data)
         f.close()
       
    def addPerson(self):
        Person = newWindow()
        #toplevel = Toplevel()
        self.handimage = StringVar()
        self.per = StringVar()
        self.gender=StringVar()
        self.age=StringVar()
      #  self.edu=StringVar()
        self.tw=StringVar()
        self.ug=StringVar()
        self.pg=StringVar()
       # self.brain=StringVar()
        self.emo=StringVar()
        #self.med=StringVar()
        self.age1=StringVar()
        self.age2=StringVar()
        self.age3=StringVar()
        self.luck=StringVar()
        self.marriage=StringVar()

        global filename1
        self.handimage.set(filename1)
      
       # Label(Person, text=" ").pack(fill=X)
        
        Label(Person, text="Hand Image",bg="light green").pack(fill=X)
        Entry(Person,textvariable=self.handimage,state="disabled").pack(fill=X)
        Entry(Person,textvariable=self.act,bg="light yellow").pack(fill=X)
        path = self.handimage.get()
        
        
  #      Label(Person, text=" ").pack(fill=X)
 #       Label(Person, text="Name" , bg="light green").pack(fill=X)
 #       Entry(Person,textvariable=self.per,bg="light yellow").pack(fill=X)
     #   Label(Person, text="M/F").pack()
      #  Entry(Person,textvariable=self.gender,bg="light yellow").pack(fill=X)
 #       Label(Person, text="Age").pack()
  #      Entry(Person,textvariable=self.age,bg="light yellow").pack(fill=X)

   #     Label(Person, text=" ").pack(fill=X)
        Label(Person, text="Education Life",bg="light green").pack(fill=X)
        Label(Person, text="12th:").pack()
        Entry(Person,textvariable=self.tw,bg="light yellow").pack(fill=X)
        Label(Person, text="UG:").pack()
        Entry(Person,textvariable=self.ug,bg="light yellow").pack(fill=X)
        Label(Person, text="PG:").pack()
        Entry(Person,textvariable=self.pg,bg="light yellow").pack(fill=X)

      #  Label(Person, text=" ").pack(fill=X)
        Label(Person, text="Emotional Stability ",bg="light green").pack(fill=X)
        Label(Person, text="1.Stable/2.Average/3.Weak ").pack(fill=X) 
        Entry(Person,textvariable=self.emo,bg="light yellow").pack(fill=X)

        Label(Person, text=" ").pack(fill=X)
        Label(Person, text="Marriage Stability ",bg="light green").pack(fill=X)
        Label(Person, text="1.Stable/2.Average/3.Weak ").pack(fill=X) 
        Entry(Person,textvariable=self.marriage,bg="light yellow").pack(fill=X)

        Label(Person, text=" ").pack(fill=X)
        Label(Person, text="Luck Factor ",bg="light green").pack(fill=X)
        Label(Person, text="Rate between 0-10 ").pack(fill=X) 
        Entry(Person,textvariable=self.luck,bg="light yellow").pack(fill=X)

        Label(Person, text=" ").pack(fill=X)
        Label(Person, text="Health Life  ",bg="light green").pack(fill=X)
        Label(Person, text="Rate between 0-10 ").pack(fill=X)
        Label(Person, text="Age 0-25 ").pack(fill=X)
        Entry(Person,textvariable=self.age1,bg="light yellow").pack(fill=X)
        Label(Person, text="Age 25-50 ").pack(fill=X)
        Entry(Person,textvariable=self.age2,bg="light yellow").pack(fill=X)
        Label(Person, text="Age 50-75 ").pack(fill=X)
        Entry(Person,textvariable=self.age3,bg="light yellow").pack(fill=X)

       # Label(Person, text=" ").pack(fill=X)
        handler = lambda: self.callback()
        b = Button(Person, text="save", bg="pink", width=15, command=handler).pack(fill=X)
        Person.mainloop()
    def callback(self):
        
        f=open("databases/index.txt","r")
        ind = int(f.read())
        f.close()

        global filename1
        img = cv2.imread(filename1)
        edges = cv2.Canny(img,70,90)
        path = "databases/Images/"+str(ind)+".jpg"
        cv2.imwrite(path,edges)
        
        s = "databases/Ratios/" + str(ind) + ".txt"
        ff=open(s,"w")
        global ratios
        ff.write(ratios)
        ff.close()

        s = "databases/Education/" + str(ind) + ".txt"
        ff=open(s,"w")
        s = self.tw.get()+"\n"+self.ug.get()+"\n"+self.pg.get()+"\n"
        ff.write(s)
        ff.close()
        
        s = "databases/Emotion/" + str(ind) + ".txt"
        ff=open(s,"w")
        s = self.emo.get()+"\n"
        ff.write(s)
        ff.close()

        s = "databases/Health/" + str(ind) + ".txt"
        ff=open(s,"w")
        s = self.age1.get()+"\n"+self.age2.get()+"\n"+self.age3.get()+"\n"
        ff.write(s)
        ff.close()

        s = "databases/Luck/" + str(ind) + ".txt"
        ff=open(s,"w")
        s = self.luck.get()+"\n"
        ff.write(s)
        ff.close()

        s = "databases/Marriage/" + str(ind) + ".txt"
        ff=open(s,"w")
        s = self.marriage.get()+"\n"
        ff.write(s)
        ff.close()

        f=open("databases/index.txt","w")
        ind = ind +1
        ss = str(ind)
        f.write(ss)
        f.close()

        #toplevel.destroy()

    
        
        
if __name__ == "__main__":
    client="Palmistry : Version 1.2"
    app = simpleapp_tk(None)
    app.title(client)
    app.mainloop()
