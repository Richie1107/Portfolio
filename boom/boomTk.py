
import tkinter as tk
import random
import tkinter.messagebox
import time


def _setnum():
    global entrY1,entrY2,num1,num2,lastNum,numX,numY
    num1=int(entrY1.get())
    num2=int(entrY2.get())
    lastNum=random.randint(num1, num2)
    numX=num1
    numY=num2
    entrY1.delete(0,'end')
    entrY2.delete(0,'end')
    listBox.insert(0,'範圍'+str(num1)+'~'+str(num2)+'\n'+'(請猜範圍內數字)')
    wiN1.destroy()
    
def _hit1():
    global num1,num2,entrY1,entrY2 ,wiN1
    wiN1=tk.Toplevel(wiN)
    wiN1.title("設定號碼範圍!!")
    wiN1.geometry("400x300+750+400")
    wiN1.configure(bg='red')
    lbL1 = tk.Label(wiN1,text='輸入開始號碼:',fg="black", font=("Arial", 12),\
                    width=15, height=2)
    lbL1.grid(row=1,column=0)
    entrY1=tk.Entry(wiN1,font=("Arial",12),bd=5)
    entrY1.grid(row=1,column=1) 
    
    lbL2 = tk.Label(wiN1,text='輸入結尾號碼:',fg="black", font=("Arial", 12),\
                    width=15, height=2)
    lbL2.grid(row=2,column=0)
    entrY2=tk.Entry(wiN1,font=("Arial",12),bd=5)
    entrY2.grid(row=2,column=1)
    btN1 = tk.Button(wiN1, text="返回", font=("Arial", 12), width=10,\
                     height=2, command=wiN1.destroy)
    btN1.grid(row=8,column=1) 
    btN2 = tk.Button(wiN1, text="設定!!", font=("Arial", 12),fg='red',\
                     width=10, height=2, command=_setnum)
    btN2.grid(row=6,column=1)
    
def _hit2():
    global num1,num2,lastNum,numX,numY
   
    try:         
        youNum=int(entrY.get())
    except:
        listBox.insert(0,'請輸入數字')
    
    if youNum<numX or youNum>numY:
        listBox.insert(0,'請輸入範圍內的數字'+str(numX)+'~'+str(numY))            
    elif youNum==lastNum:
        listBox.insert(0,'爆炸'+'\n'+'將於10秒後重新開始')
        wiN.update()
        _delay_time()
    elif youNum>lastNum:
        listBox.insert(0,str(numX)+'~'+str(youNum))
        numY=youNum
    elif youNum<lastNum:
        listBox.insert(0,str(youNum)+'~'+str(numY))
        numX=youNum        
    entrY.delete(0,'end')
    
def _hit3():
    global num1,num2,lastNum,numX,numY    
    lastNum=random.randint(num1,num2)
    numX=num1
    numY=num2
    listBox.delete(0,"end")
    listBox.insert(0,'範圍'+str(num1)+'~'+str(num2)+'\n'+'(請猜範圍內數字)')   
    
def _hit4():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()

def _delay_time():
    wiN.after(10000,_hit3())




    
#使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()
#3.設定視窗[標題]
wiN.title("終極密碼")
#設定視窗顯示位置的方法:700是X軸，300是Y軸
wiN.geometry("500x500+700+300")
#固定視窗大小的作法
wiN.resizable(width=False, height=False)
#設定背景
wiN.configure(bg='orange')
#設定圖標
wiN.iconbitmap('boom.ico')



entrY=tk.Entry(wiN,font=("Arial",16),bd=5)
entrY.pack() 


btN1 = tk.Button(wiN, text="設定號碼範圍",fg="red", font=("Arial", 16),\
                 width=10, height=2, command=_hit1)
btN1.pack()
btN2 = tk.Button(wiN, text="猜號碼!!",fg="green", font=("Arial", 16),\
                 width=10, height=2, command=_hit2)
btN2.pack()
btN3 = tk.Button(wiN, text="重玩!!",fg="brown", font=("Arial", 16),\
                 width=10, height=2, command=_hit3)
btN3.pack() 
btN4 = tk.Button(wiN, text="離開!!",fg="blue", font=("Arial", 16),\
                 width=10, height=2, command=_hit4)
btN4.pack(anchor='ne') 


sBar=tk.Scrollbar(wiN)
sBar.pack(side="right",fill="y")



listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set)
listBox.pack(side="bottom", fill="both")
sBar.config(command=listBox.yview)

wiN.mainloop()

