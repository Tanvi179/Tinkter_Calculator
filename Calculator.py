import tkinter

#mounts the root for our calculator
root=tkinter.Tk()
root.title("Calculator")#provides title for root
root.geometry("300x500")#provides specified length and breadth for root
root.resizable(0,0)#providing zero disable the resizable option for root window
data=tkinter.StringVar()#declaring datatype for data
val=""#for storing the values
op=""#for storing operators

#functions for calling numbers
#button1
def btn1isclick():
	global val
	val=val+"1"
	data.set(val)
#button2
def btn2isclick():
	global val
	val=val+"2"
	data.set(val)
#button3
def btn3isclick():
	global val
	val=val+"3"
	data.set(val)
#button4
def btn4isclick():
	global val
	val=val+"4"
	data.set(val)
#button5
def btn5isclick():
	global val
	val=val+"5"
	data.set(val)
#button6
def btn6isclick():
	global val
	val=val+"6"
	data.set(val)
#button7
def btn7isclick():
	global val
	val=val+"7"
	data.set(val)
#button8
def btn8isclick():
	global val
	val=val+"8"
	data.set(val)
#button9
def btn9isclick():
	global val
	val=val+"9"
	data.set(val)	
#button0
def btn0isclick():
	global val
	val=val+"0"
	data.set(val)


#funtions for operators
#plus operator
def btnplusisclick():
	global val
	global op
	op="+"
	val=val+"+"
	data.set(val)
#minus operaator
def btnminusisclick():
	global val
	global op
	op="-"
	val=val+"-"
	data.set(val)
#multiplication opertor
def btnmulisclick():
	global val
	global op
	op="*"
	val=val+"*"
	data.set(val)
#division operator
def btndivisclick():
	global val
	global op
	op="/"
	val=val+"/"
	data.set(val)	

#clear function
def btnclearisclick():
	global val
	global op
	op=" "
	val=" "
	data.set(val)		

#equals function
def btnequalsisclick():
	global val
	if op=="+":
		x,y=val.split('+')
		a=int(x)
		b=int(y)
		c=a+b
		data.set(c)		

	if op=="-":
		x,y=val.split('-')
		a=int(x)
		b=int(y)
		c=a-b
		data.set(c)	
		
	if op=="*":
		x,y=val.split('*')
		a=int(x)
		b=int(y)
		c=a*b
		data.set(c)	
		
	if op=="/":
		x,y=val.split('/')
		a=int(x)
		b=int(y)
		c=a/b
		data.set(c)				

#mounting frames on root
#frame1
f1=tkinter.Frame(root)
f1.pack(expand="True",fill="both")

#frame2
f2=tkinter.Frame(root)
f2.pack(expand="True",fill="both")

#frame3
f3=tkinter.Frame(root)
f3.pack(expand="True",fill="both")

#frame4
f4=tkinter.Frame(root)
f4.pack(expand="True",fill="both")

#frame5
f5=tkinter.Frame(root)
f5.pack(expand="True",fill="both")

#mounting label on frame1 for output
l=tkinter.Label(f1,font=("Times New Roman",20),textvariable=data)
l.pack(expand="True",fill="both")

#mounting buttons on frames
#buttons on frame2
b1=tkinter.Button(f2,text="1",font=("Times New Roman",20),command=btn1isclick)
b1.pack(side="left",expand="True",fill="both")

b2=tkinter.Button(f2,text="2",font=("Times New Roman",20),command=btn2isclick)
b2.pack(side="left",expand="True",fill="both")

b3=tkinter.Button(f2,text="3",font=("Times New Roman",20),command=btn3isclick)
b3.pack(side="left",expand="True",fill="both")

bplus=tkinter.Button(f2,text="+",font=("Times New Roman",20),command=btnplusisclick)
bplus.pack(side="left",expand="True",fill="both")

#buttons on frame3
b4=tkinter.Button(f3,text="4",font=("Times New Roman",20),command=btn4isclick)
b4.pack(side="left",expand="True",fill="both")

b5=tkinter.Button(f3,text="5",font=("Times New Roman",20),command=btn5isclick)
b5.pack(side="left",expand="True",fill="both")

b6=tkinter.Button(f3,text="6",font=("Times New Roman",20),command=btn6isclick)
b6.pack(side="left",expand="True",fill="both")

bminus=tkinter.Button(f3,text="-",font=("Times New Roman",20),command=btnminusisclick)
bminus.pack(side="left",expand="True",fill="both")

#buttons on frame4
b7=tkinter.Button(f4,text="7",font=("Times New Roman",20),command=btn7isclick)
b7.pack(side="left",expand="True",fill="both")

b8=tkinter.Button(f4,text="8",font=("Times New Roman",20),command=btn8isclick)
b8.pack(side="left",expand="True",fill="both")

b9=tkinter.Button(f4,text="9",font=("Times New Roman",20),command=btn9isclick)
b9.pack(side="left",expand="True",fill="both")

bmul=tkinter.Button(f4,text="*",font=("Times New Roman",20),command=btnmulisclick)
bmul.pack(side="left",expand="True",fill="both")

#buttons on frame5
bequals=tkinter.Button(f5,text="=",font=("Times New Roman",20),command=btnequalsisclick)
bequals.pack(side="left",expand="True",fill="both")

b0=tkinter.Button(f5,text="0",font=("Times New Roman",20),command=btn0isclick)
b0.pack(side="left",expand="True",fill="both")

bclear=tkinter.Button(f5,text="C",font=("Times New Roman",20),command=btnclearisclick)
bclear.pack(side="left",expand="True",fill="both")

bdiv=tkinter.Button(f5,text="/",font=("Times New Roman",20),command=btndivisclick)
bdiv.pack(side="left",expand="True",fill="both")
root.mainloop()