#EasyGen.py
 
import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter.colorchooser import askcolor
import time
import keyboard
from tkinter import messagebox
import config
from EasyGUI import * 

FileName = ''
Sep = '~'
Eq = '='
Typ = ''
IDx = ''
s = ''
Typ=''
Nam=''                     # name of the currently selected widget
NamInd=0                   # index of the currently selected widget  
Con=''
sw = 0
XMG = ''
Selected = 0
PageStore = ''
Choice = 0
RGB = ''

#Col = {'Black':'000000000','Maroon':'12800000', 'Green':'000128000', 'Olive':'128128000',  'Navy':'000000128', 'Purple':'128000128', 'Teal':'000128128', 'Gray':'128128128', 'Silver':'192192192', 'Red':'255000000', 'Lime':'000255000', 'Yellow':'255255000', 'Blue':'000000255', 'Fuschia':'255000255', 'Aqua':'000255255', 'White':'255255255'} 
#Jus = {'Center':'2', 'Left':'1', 'Right':'3'}
#Fnt = {'Normal':'0', 'Bold':'2', 'Underline':'4', 'Bold/Underline':'6', 'Italic':'8', 'Bold/Italic':'10', 'Underline/Italic':'12', 'Bold/Underline/Italic':'14'}
LST = ['', 'Button', 'Label', 'Edit', 'Memo', 'List', 'Combo', 'Check', 'Radio', 'Shape', 'Slider', 'Image', 'Web' ]
Defa = [
        [0,0,  0,  0],             # position and size defaults
        [0,0,500,200],             # for each Widget
        [0,0,500,200],
        [0,0,500,150],
        [0,0,500,500], 
        [0,0,500,500],
        [0,0,500,150], 
        [0,0,150,150],
        [0,0,150,150],
        [0,0,150,150],
        [0,0,150,150],
        [0,0,500,500],
        [0,0,500,500], 
       ]

Open(4000)

def hex_to_rgb(hex):
    if hex != None:
        hex = hex.lstrip('#')
        hlen = len(hex)
        return tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))

def BackClick():
    global RGB
    
    NewColor = askcolor(title="Select Background color")[1]
    NewColor = hex_to_rgb(NewColor)
    L = list(NewColor)
    RGB = ''
    for x in L:
        x = str(x)
        while len(x) < 3:
            x = x + '0'
        RGB = RGB + x
    Back.delete(0,tk.END)
    Back.insert(9,RGB)
    if ID.get().strip() == '' :
        Send('00=' + Page.get().strip() + Sep + 'Back' + Eq + RGB)
    else:    
        Send(Con + Sep + 'Back' + Eq + RGB)
#    Color.focus_set()
    
def ForeClick():
    global RGB
    
    NewColor = askcolor(title="Select Foreground color")[1]
    NewColor = hex_to_rgb(NewColor)
    L = list(NewColor)
    RGB =''
    for x in L:
        x = str(x)
        while len(x) < 3:
            x = x + '0'
        RGB = RGB + x
    Color.delete(0,tk.END)
    Color.insert(9,RGB)
    Send(Con + Sep + 'Color' + Eq + RGB)

def ShowChoice():
    global Choice
    
    Choice = v.get()
    
def key_pressed(event):
        global Nam
        global Choice
        
        L = [config.Keys['Left'],config.Keys['Up'],config.Keys['Right'],config.Keys['Down']]
       
        if event.keycode not in L:
            return
               
        if Choice == 3:
            if event.keycode == config.Keys['Right']:                       # Right
                t = int(Find(Nam,'Width'))
                t = t + 10
                Send(Con + Sep + 'Width' + Eq + str(t))
                Width.delete(0,tk.END)
                Width.insert(0, str(t)) 
            if event.keycode == config.Keys['Left']:                        # Left
                t = int(Find(Nam,'Width'))
                t = t - 10
                Send(Con + Sep + 'Width' + Eq + str(t))
                Width.delete(0,tk.END)
                Width.insert(0, str(t)) 
            if event.keycode == config.Keys['Down']:                        # Down
                t = int(Find(Nam,'Height'))
                t = t + 10
                Send(Con + Sep + 'Height' + Eq + str(t))
                Height.delete(0,tk.END)
                Height.insert(0, str(t)) 
            if event.keycode == config.Keys['Up']:                          # Up
                t = int(Find(Nam,'Height'))
                t = t - 10
                Send(Con + Sep + 'Height' + Eq + str(t))
                Height.delete(0,tk.END)
                Height.insert(0, str(t)) 
      
        if Choice == 2:
            root.focus_set()
            if Nam != '':
#                if (event.keycode > 37) and (event.keycode < 41):
                    if event.keycode == config.Keys['Right']:               # Right
                        t = int(Find(Nam,'Left'))
                        t = t + 10
                        Send(Con + Sep + 'Left' + Eq + str(t))
                        Left.delete(0,tk.END)
                        Left.insert(0, str(t)) 
                    if event.keycode == config.Keys['Left']:                 # Left
                        t = int(Find(Nam,'Left'))
                        t = t - 10
                        Send(Con + Sep + 'Left' + Eq + str(t))
                        Left.delete(0,tk.END)
                        Left.insert(0, str(t)) 
                    if event.keycode == config.Keys['Down']:                 # Down
                        t = int(Find(Nam,'Top'))
                        t = t + 10
                        Send(Con + Sep + 'Top' + Eq + str(t))
                        Top.delete(0,tk.END)
                        Top.insert(0, str(t)) 
                    if event.keycode == config.Keys['Up']:                   # Up
                        t = int(Find(Nam,'Top'))
                        t = t - 10
                        Send(Con + Sep + 'Top' + Eq + str(t))
                        Top.delete(0,tk.END)
                        Top.insert(0, str(t))
                        
def ClearClick():
    if messagebox.askyesno('        CLEAR ALL WIDGETS', 'Are you sure ?'):
        WidgetBox.delete(0,tk.END)
        for x in config.Lot:
            y = list(x)
            Send( '50' + Eq + 'Delete' + Sep + 'Text' + Eq + y[0])
            config.Lot = [{'Empty':'Empty'}]       # clear dictionary
        ID.delete(0,tk.END)                                   # clear ID
        Clear()
        
def DeleteClick():                         # deletes a Widget 
    global Nam
    global NamInd 
    
    WidgetBox.delete(NamInd)
    Send('50' + Eq + 'Delete' + Sep + 'Text' + Eq + Nam)
    i = -1
    for config.Row in config.Lot:
        i = i + 1 
        if Nam in config.Row:
            config.Lot.pop(i)             #***************************************************
            ID.delete(0,tk.END)
    Clear()
    SelectBox.focus_set()
     
def ReadClick():                                     # reads a Template from the Client Device   
     global FileName
     global Nam
  
     if FileName == '':
         print('\a')
         messagebox.showinfo("Warning", "File Name can not be blank")
         FilName.focus_set()
         return 
     else:
         WidgetBox.delete(0,tk.END)
         config.Lot = [{'Empty':'Empty'}]            # clear dictionary 
         GetForm(FileName)                           # read file from client and fill config.Lot
         config.Lot.pop(0)                           # remove empty dictionary
         for config.Row in config.Lot:               # get Widget Names
             x = config.Row.keys()                   # get all keys 
             y = list(x)
             Nam = y[0]
             if not 'Page' in Nam:
                 WidgetBox.insert(tk.END,Nam)
     
def WriteClick():                                    # writes a Template to the Client Device
     global FileName
     
     FileName = FilName.get().strip()
     if FileName == '':
         print('\a')
         messagebox.showinfo("Warning", "File Name can not be blank")
         FilName.focus_set()
     else:    
         Send('52' + Eq + 'Write' + Sep + 'Text' + Eq + FileName)
     
def on_closing():
    Send('Exit')
    root.destroy()     

def btnClickFunction():
        return         
     
def Clear():
     Left.delete(0, tk.END)
     Top.delete(0, tk.END)
     Width.delete(0,tk.END)
     Height.delete(0,tk.END)
     MyText.delete(1.0, tk.END)
     Just.delete(0,tk.END)
     Back.delete(0,tk.END)
     Color.delete(0,tk.END)
     Size.delete(0,tk.END)
     Style.delete(0,tk.END)
     Min.delete(0,tk.END) 
     Max.delete(0,tk.END)
     Pos.delete(0,tk.END) 

def SelectExit(event):
     global Typ
     global Selected
     
#     SM.set('Move Widgets with the Arrows')
     ID.delete(0,tk.END)                                   # clear ID
     index = SelectBox.curselection()[0]
     Typ = str(index+1)
     Typ = Typ.zfill(2)
     photo.config(file = Typ + '.gif')
     Selected = 1
     Clear()                                               # clear all
     Page.focus_set()
     
      
def WidgetExit(event):
    global Con   
    global sw
    global Nam 
    global NamInd
    global Typ

    sw = 0 
    if WidgetBox.size() == 0:
         print('\a')
         messagebox.showinfo("Warning", "You must select a Widget first from the Widget List !")
         SelectBox.focus_set()
         sw = 1 
         return False
         
    index = WidgetBox.curselection()[0]
    NamInd = index
    Nam = WidgetBox.get(index)
  
    for config.Row in config.Lot:
        if Nam in config.Row:
            x = config.Row.values()                   # get all values
            y = list(x)
            Typ = y[0] 
            photo.config(file = Typ + '.gif')
            break
    Con = Typ + Eq + Nam
    Clear()
    
    Page.delete(0,tk.END)
    Page.insert(0,'Page' + str(Find(Nam,'PageNo')))
    Send('00=Page' + PageStore + str(Find(Nam,'PageNo')))
    ID.delete(0,tk.END)
    ID.insert(0,Nam)
    Left.insert(0, Find(Nam,'Left'))               #fill from dictionary
    Top.insert(0, Find(Nam,'Top'))
    Width.insert(10, Find(Nam,'Width'))
    Height.insert(10, Find(Nam,'Height'))
    if Find(Nam,'Text') != None:
        MyText.insert(tk.END,Find(Nam,'Text'))   
    if Find(Nam,'Just') != None:
        Just.insert(10, Find(Nam,'Just'))
    if Find(Nam,'Back') != None:
        Back.insert(10, Find(Nam,'Back'))
    if Find(Nam,'Color') != None:
        Color.insert(10, Find(Nam,'Color'))
    if Find(Nam,'Size') != None:
        Size.insert(10,Find(Nam,'Size'))
    if Find(Nam,'Style') != None:
        Style.insert(10, Find(Nam,'Style'))
    if Find(Nam,'Min') != None:
        Min.insert(10,Find(Nam,'Min'))
    if Find(Nam,'Max') != None:    
        Max.insert(10,Find(Nam,'Max'))
    if Find(Nam,'Pos') != None:    
        Pos.insert(10,Find(Nam,'Pos'))
        
def IDExit(event):
        global Typ
        global Nam
        global Con
        global sw
        global Selected
        global PageStore
        
        if Selected == 0:                                   # no widget selected
            print('\a')
            messagebox.showinfo("Warning", "You must select a Widget first from the Select Type List !")
            ID.delete(0,tk.END)
            ID.insert(0,'Select Widget first')
            SelectBox.focus_set()
            return False
        sw = 0
        if ID.get().strip() == '':                          #empty ID
            print('\a')
            messagebox.showinfo("Warning", "The ID can not be blank !")
            ID.focus_set()
            sw = 1
            return False
        else:
            for config.Row in config.Lot:
                if ID.get().strip() in config.Row:
                    print('\a')                             #duplicate ID
                    messagebox.showinfo("Warning", "Duplicate ID ")
                    ID.focus_set()
                    ID.delete(0,tk.END)
                    sw = 1
                    return False
             
            Nam = ID.get().strip() 
            Con = Typ + Eq + Nam
            WidgetBox.insert(tk.END,Nam)
            
            Send(Typ + Eq + Nam)
            Left.insert(0,Defa[int(Typ)][0])     # display default values         
            Top.insert(0,Defa[int(Typ)][1])     
            Width.insert(10,Defa[int(Typ)][2])
            Height.insert(10,Defa[int(Typ)][3])
            Size.insert(3,14)
            Style.insert(2,0)
            Just.insert(2,2)
            Back.insert(9,'236236236')
            Color.insert(9,'000000000')
            Min.insert(6,0)
            Max.insert(6,0)
            Pos.insert(6,0)
            
            z = Con + Sep + 'Left'    + Eq + str(Defa[int(Typ)][0]) \
                    + Sep + 'Top'     + Eq + str(Defa[int(Typ)][1]) \
                    + Sep + 'Width'   + Eq + str(Defa[int(Typ)][2]) \
                    + Sep + 'Height'  + Eq + str(Defa[int(Typ)][3]) \
                    + Sep + 'Text'    + Eq + '' \
                    + Sep + 'Back'    + Eq + '236236236' \
                    + Sep + 'Color'   + Eq + '000000000' \
                    + Sep + 'Size'    + Eq + '14' \
                    + Sep + 'Style'   + Eq + '0' \
                    + Sep + 'Just'    + Eq + '2' \
                    + Sep + 'Min'     + Eq + '0' \
                    + Sep + 'Max'     + Eq + '0' \
                    + Sep + 'Pos'     + Eq + '0'
            Send(z)
            xx = PageStore
            PageStore = PageStore.replace('Page','')
            config.Row['PageNo'] = PageStore
                  
def PageExit(event):
        global PageStore
        
        x = Page.get().strip() 
        if sw == 0:
            Send('00=' + x)
            PageStore = x
            
def LeftExit(event):
        global sw
        
        x = Left.get().strip()
        if sw == 0:
            Send(Con + Sep + 'Left' + Eq + x)
        
def TopExit(event):
        x = Top.get().strip()
        Send(Con + Sep + 'Top' + Eq + x)
        
def WidthExit(event):
        x = Width.get().strip()
        Send(Con + Sep + 'Width' + Eq + x)
        
def HeightExit(event):
        x = Height.get().strip()
        Send(Con + Sep + 'Height' + Eq + x)

def SizeExit(event):
        x = Size.get().strip()
        Send(Con + Sep + 'Size' + Eq + x)
        
def StyleExit(event):        
        x = Style.get().strip() 
        Send(Con + Sep + 'Style' + Eq + x)        
        
def MinExit(event):
        x = Min.get().strip()
        Send(Con + Sep + 'Min' + Eq + x)
        
def MaxExit(event):
        x = Max.get().strip()
        Send(Con + Sep + 'Max' + Eq + x)
        
def PosExit(event):
        x = Pos.get().strip() 
        Send(Con + Sep + 'Pos' + Eq + x)
        
def MyTextExit(event):
        x = MyText.get("1.0", tk.END).strip()
        Send(Con + Sep + 'Text' + Eq + x)
        
def JustExit(event):        
        x = Just.get().strip()
        Send(Con + Sep + 'Just' + Eq + x)
 
def FilNameExit(event):
        global FileName
        FileName = FilName.get().strip()
        
def callback(input):
    if (input.isdigit()) or (input == ''):
        return True
    else:
        return False        
#---------------------------------------------------------------------------------------
    
root = Tk()

w = 1020
h = 580

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#root.geometry('1020x580')
v = tk.IntVar()
v.set(1)  # initializing the choice
 
x = config.IP.split('.')
ThisIP = x[3]
PRT = str(config.Port).zfill(5)
root.title('GUIfyGen - ' + ThisIP + PRT)
#---------------------------------------------------------------------------------------
Label(root, text='SELECT TYPE', font=('arial', 15, 'normal')).place(x= 55, y=3)
SelectBox=Listbox(root, name='listboxone', font=('arial', 12, 'normal'), width=20, height=0)
SelectBox.insert(tk.END, 'Button')
SelectBox.insert(tk.END, 'Label')
SelectBox.insert(tk.END, 'Edit')
SelectBox.insert(tk.END, 'Memo') 
SelectBox.insert(tk.END, 'List')
SelectBox.insert(tk.END, 'Combo')
SelectBox.insert(tk.END, 'Check')
SelectBox.insert(tk.END, 'Radio')
SelectBox.insert(tk.END, 'Shape') 
SelectBox.insert(tk.END, 'Slider')
SelectBox.insert(tk.END, 'Image') 
SelectBox.insert(tk.END, 'Web')
SelectBox.place(x=30, y=30)
SelectBox.bind('<ButtonRelease-1>', SelectExit)
#---------------------------------------------------------------------------------------
Label(root, text='VALUES', font=('arial', 15, 'normal')).place(x=330, y=3)
#---------------------------------------------------------------------------------------
Label(root, text='Page', fg='red', font=('arial', 12, 'normal')).place(x=252, y=30)
Page=Entry(root, fg='red')
Page.place(x=300, y=30, width=60)
Page.insert(tk.END, 'Page0')
Page.bind("<FocusOut>", PageExit)
#---------------------------------------------------------------------------------------
Label(root, text='ID', font=('arial', 12, 'normal')).place(x=275, y=56)
ID=Entry(root)
ID.place(x=300, y=56)
#reg = root.register(callback)
#ID.config(validate="key", validatecommand=(reg, '%P'))
ID.bind("<FocusOut>", IDExit)
#---------------------------------------------------------------------------------------
Label(root, text='Left', font=('arial', 12, 'normal')).place(x=265, y=82)
Left=Entry(root)
Left.place(x=300, y=82, width=50)
reg = root.register(callback)
Left.config(validate="key", validatecommand=(reg, '%P'))
Left.bind("<FocusOut>", LeftExit)
#---------------------------------------------------------------------------------------
Label(root, text='Top', font=('arial', 12, 'normal')).place(x=265, y=108)
Top=Entry(root)
Top.place(x=300, y=108, width=50)
reg = root.register(callback)
Top.config(validate="key", validatecommand=(reg, '%P'))
Top.bind("<FocusOut>", TopExit)#onFocusout_Top)
#---------------------------------------------------------------------------------------
Label(root, text='Width', font=('arial', 12, 'normal')).place(x=250, y=134)
Width=Entry(root)
Width.place(x=300, y=134, width=50)
reg = root.register(callback)
Width.config(validate="key", validatecommand=(reg, '%P'))
Width.bind("<FocusOut>", WidthExit)#onFocusout_Width)
#---------------------------------------------------------------------------------------
Label(root, text='Height', font=('arial', 12, 'normal')).place(x=245, y=160)
Height=Entry(root)
Height.place(x=300, y=160, width=50)
reg = root.register(callback)
Height.config(validate="key", validatecommand=(reg, '%P'))
Height.bind("<FocusOut>", HeightExit)#onFocusout_Height)
#---------------------------------------------------------------------------------------
Label(root, text='Text', font=('arial', 12, 'normal')).place(x=260, y=250)
MyText = tk.Text(root)
MyText.place(x=300, y=186,w = 170,h = 150) 
MyText.bind("<FocusOut>", MyTextExit) #onFocusout_MyText)
#---------------------------------------------------------------------------------------
Label(root, text='Just', font=('arial', 12, 'normal')).place(x=260, y=338)
Just= Entry(root) 
Just.place(x=300, y=338, width = 50)
reg = root.register(callback)
Just.config(validate="key", validatecommand=(reg, '%P'))
Just.bind("<FocusOut>", JustExit) #onFocusout_Just)
#---------------------------------------------------------------------------------------
Label(root, text='Back', font=('arial', 12, 'normal')).place(x=255, y=364)
Back=Entry(root)
Back.place(x=300, y=364, width = 80)
reg = root.register(callback)
#---------------------------------------------------------------------------------------
Button(root, text='', command=BackClick).place(x=390, y=364, w = 30, h = 25)
#---------------------------------------------------------------------------------------
Label(root, text='Color', font=('arial', 12, 'normal')).place(x=255, y=390)
Color=Entry(root)
Color.place(x=300, y=390, width = 80)
reg = root.register(callback)
#---------------------------------------------------------------------------------------
Button(root, text='', command=ForeClick).place(x=390, y=390, w = 30, h = 25)
#---------------------------------------------------------------------------------------
Label(root, text='Font Size', font=('arial', 12, 'normal')).place(x=225, y=416)
Size=Entry(root)
Size.place(x=300, y=416, width=50)
reg = root.register(callback)
Size.config(validate="key", validatecommand=(reg, '%P'))
Size.bind("<FocusOut>", SizeExit) #onFocusout_Size)
#-------------------------------------------------------------------------------
Label(root, text='Font Style', font=('arial', 12, 'normal')).place(x=222, y=442)
Style=Entry(root) 
Style.place(x=300, y=442, width=50)
reg = root.register(callback)
Style.config(validate="key", validatecommand=(reg, '%P'))
Style.bind("<FocusOut>", StyleExit) #onFocusout_Style)
#-------------------------------------------------------------------------------
Label(root, text='Min', font=('arial', 12, 'normal')).place(x=264, y=468)
Min=Entry(root)
Min.place(x=300, y=468, width=50)
reg = root.register(callback)
Min.config(validate="key", validatecommand=(reg, '%P'))
Min.bind("<FocusOut>", MinExit) #onFocusout_Min)
#---------------------------------------------------------------------------------------
Label(root, text='Max', font=('arial', 12, 'normal')).place(x=264, y=494)
Max=Entry(root)
Max.place(x=300, y=494, width=50)  
reg = root.register(callback)
Max.config(validate="key", validatecommand=(reg, '%P'))
Max.bind("<FocusOut>", MaxExit) #onFocusout_Max)
#---------------------------------------------------------------------------------------
Label(root, text='Pos', font=('arial', 12, 'normal')).place(x=264, y=520)
Pos=Entry(root) 
Pos.place(x=300, y=520, width=50)  
reg = root.register(callback)
Pos.config(validate="key", validatecommand=(reg, '%P'))
Pos.bind("<FocusOut>", PosExit) #onFocusout_Pos)
#-------------------------------------------------------------------------------
Label(root, text='File Name',fg='blue', font=('arial', 12, 'normal')).place(x=82, y=315)
FilName=Entry(root)
FilName.place(x=40, y=340)
#FilName.bind("<FocusOut>", FilNameExit)
FilName.bind("<Leave>", FilNameExit)
Button(root, text='Load Template', fg='blue', font=('arial', 12, 'bold'), command=ReadClick).place( x=53, y=370, w = 130, h = 30)
Button(root, text='Save Template', fg='blue', font=('arial', 12, 'bold'), command=WriteClick).place(x=53, y=410, w = 130, h = 30)
Button(root, text='Clear All', fg='red', font=('arial', 12, 'bold'), command=ClearClick).place(x=53, y=450, w = 130, h = 30)
#-------------------------------------------------------------------------------
Label(root, text='WIDGETS', font=('arial', 14, 'normal')).place(x=525, y=3)
WidgetBox=Listbox(root, font=('arial', 10, 'normal'), width=22, height=28)
WidgetBox.place(x=483, y=30)
WidgetBox.bind('<ButtonRelease-1>', WidgetExit)
#---------------------------------------------------------------------------------------
photo = PhotoImage(file = XMG) 
Button(root, text='',image = photo , fg='red', font=('arial', 12, 'bold'), command=btnClickFunction).place(x=650, y=30, w = 360, h = 300)
#---------------------------------------------------------------------------------------
Button(root, text='Delete Widget', fg='black', font=('arial', 12, 'bold'), command=DeleteClick).place(x=495, y=515, w = 130, h = 30)
#---------------------------------------------------------------------------------------
Label(root, text='Input fields will only be sent after TAB is pressed (Ctrl + Tab for Text)',  fg='red',  font=('arial', 12, 'bold')).place(x=60, y=550)
#---------------------------------------------------------------------------------------
tk.Radiobutton(root, text="NONE", fg='black', font=('arial', 14, 'bold'), variable=v, value=1,command=ShowChoice).place(x=770, y=350)
tk.Radiobutton(root, text="MOVE", fg='red', font=('arial', 14, 'bold'), variable=v, value=2,command=ShowChoice).place(x=770, y=380)
tk.Radiobutton(root, text="SIZE", fg='red', font=('arial', 14, 'bold'), variable=v, value=3,command=ShowChoice).place(x=770, y=410)
#---------------------------------------------------------------------------------------
MoveLab=Label(root,text='Move/Size widgets with the arrow keys'  , bg='#F0F0F0', fg='red',  font=('arial', 12, 'bold')).place(x=670, y=450)
#---------------------------------------------------------------------------------------

root.bind("<Key>",key_pressed)
#config.Keys = GetGlobal(config.Keys)
#root.bind("<Key>",key_released)
#---------------------------------------------------------------------------------------
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

