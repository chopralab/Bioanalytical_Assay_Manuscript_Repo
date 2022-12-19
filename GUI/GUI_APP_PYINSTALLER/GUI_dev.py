import subprocess
import tkinter as tk
#from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import time 



class scorrer_box(tk.Frame):
    def __init__(self, parent, default_input):
        super().__init__(parent)
        self.default_input = default_input
        self.rowconfigure(0, weight=1)
        for iz in range(3):
            self.grid_rowconfigure(iz, weight=1)
            self.grid_columnconfigure(iz, weight=1)
        self.thresh_l = []
        self.score_vl = []
        for i in range(10):
            LV  = tk.StringVar()
            L = tk.Entry(self,textvariable = LV, width=5)
            self.thresh_l.append([L,LV])
        for i in range(11):
            SV  = tk.StringVar()
            S = tk.Entry(self,textvariable = SV, width=5)
            self.score_vl.append([S,SV])
        self.IT_button = tk.Button(self, text = "Increase\nThreshold",command = self.IT)
        self.DT_button = tk.Button(self, text = "Decrease\nThreshold",command = self.DT)
        #unpack_defaults
        self.title= tk.Label(self,text=self.default_input[0])
        self.t_l = tk.Label(self,text=self.default_input[1])
        self.lls = tk.Label(self,text=" < ")
        self.rls = tk.Label(self,text=" < ")
        self.s = tk.Label(self,text="Score: ")
        self.title.grid(row=0,columnspan=len(self.default_input[3])+2)
        self.t_l.grid(row=1,column=0)
        self.lls.grid(row=1,column=1)
        for i in range(len(self.default_input[2])):
            temL = self.thresh_l[i]
            temL[1].set(self.default_input[2][i])
            temL[0].grid(row=1,column=2+i)
        self.rls.grid(row=1,column=3+i)
        self.IT_button.grid(row=1,column=4+i)
        self.s.grid(row=2,column=0)
        self.in_i = i
        for j in range(len(self.default_input[3])):
            print(j)
            temS = self.score_vl[j]
            print(temS)
            print(self.default_input[3][j])
            temS[1].set(self.default_input[3][j])
            temS[0].grid(row=2,column=1+j)
            self.in_j = j
        self.DT_button.grid(row=2,column=i+4)
    def IT(self):
        if self.in_i < 9:
            self.t_l.grid(row=1,column=0)
            self.lls.grid(row=1,column=1)
            for i in range(self.in_i+1):
                temL = self.thresh_l[i]
                temL[0].grid(row=1,column=2+i)
            temL = self.thresh_l[i+1]
            self.in_i += 1
            temL[1].set("")
            temL[0].grid(row=1,column=3+i)
            self.rls.grid(row=1,column=4+i)
            self.IT_button.grid(row=1,column=5+i)
            self.s.grid(row=2,column=0)
            for j in range(self.in_j+1):
                temS = self.score_vl[j]
                temS[0].grid(row=2,column=1+j)
            temS = self.score_vl[j+1]
            self.in_j += 1
            temS[1].set("")
            temS[0].grid(row=2,column=2+j)
            self.DT_button.grid(row=2,column=i+5)
            self.title.grid_forget()
            self.title.grid(row=0,columnspan=i+5)
        else:
            tk.messagebox.showwarning("Threshold limit", "Thresholds cannot exceed 10",icon="warning")        
    def DT(self):
        if self.in_i > 1:
            self.t_l.grid(row=1,column=0)
            self.lls.grid(row=1,column=1)
            for i in range(self.in_i):
                print(i)
                temL = self.thresh_l[i]
                temL[0].grid(row=1,column=2+i)
            temL = self.thresh_l[i+1]
            temL[1].set("")
            temL[0].grid_forget()
            self.in_i -= 1
            self.rls.grid(row=1,column=3+i)
            self.IT_button.grid(row=1,column=5+i)
            self.s.grid(row=2,column=0)
            for j in range(self.in_j):
                temS = self.score_vl[j]
                temS[0].grid(row=2,column=1+j)
            temS = self.score_vl[j+1]
            temS[1].set("")
            temS[0].grid_forget()
            self.in_j -= 1
            self.DT_button.grid(row=2,column=i+5)
            self.title.grid_forget()
            self.title.grid(row=0,columnspan=i+5)
        else:
            tk.messagebox.showwarning("Threshold limit", "Thresholds must exceed 1",icon="warning")
            

    def default_meth(self):
        self.rls.grid_forget()
        self.DT_button.grid_forget()
        self.IT_button.grid_forget()
        self.title.grid(row=0,columnspan=len(self.default_input[3])+2)
        self.t_l.grid(row=1,column=0)
        self.lls.grid(row=1,column=1)
        for i in self.thresh_l:
            i[0].grid_forget()
        for i in range(len(self.default_input[2])):
            temL = self.thresh_l[i]
            temL[1].set(self.default_input[2][i])
            temL[0].grid(row=1,column=2+i)
        self.rls.grid(row=1,column=3+i)
        self.IT_button.grid(row=1,column=4+i)
        self.s.grid(row=2,column=0)
        self.in_i = i
        for j in self.score_vl:
            j[0].grid_forget()
        for j in range(len(self.default_input[3])):
            print(j)
            temS = self.score_vl[j]
            print(temS)
            print(self.default_input[3][j])
            temS[1].set(self.default_input[3][j])
            temS[0].grid(row=2,column=1+j)
            self.in_j = j
        self.DT_button.grid(row=2,column=i+4)

    def ret_vals(self):
        print('hi')
        tl = []
        for z in range(self.in_i+1):
            #should have error handeling for non float conversions 
            tv = self.thresh_l[z][0].get()
            tl.append(tv)
        sl = []
        for z in range(self.in_j+1):
            sv = self.score_vl[z][0].get()
            sl.append(sv)
        print(tl,sl)
        return(tl,sl)


class Step1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        shape_fill_frame = tk.Frame(self)
        self.parentc = parent
        #flabel = tk.Label(shape_fill_frame, text="File path:")
        #flabel.pack(side=tk.LEFT)
        self.fileE = tk.Entry(shape_fill_frame, text="", width=40,state="disabled",disabledforeground="black")
        self.lws = False
        header = tk.Label(self, text="Select raw plate file", bd=2, relief="groove",pady=5)
        header.pack(side="top", fill="x",pady=0)
        self.fileE.pack(pady=1)
        self.pbut = tk.Button(shape_fill_frame, text = 'Multi Plate Selection', command = self.fbd)
        self.pbut.pack(pady=1)
        shape_fill_frame.pack(pady=25)
        self.listbox = None

    def on_closing(self):
        self.lws = False
        self.lwindow.destroy()


    def fbd(self):
        self.fileE.config(state=tk.NORMAL)
        self.fileE.delete(0, tk.END)
        self.fileE.configure(state="disabled") 
        print(self.fileE.get())
        self.lwindow = tk.Toplevel(self)
        self.lwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.lws = True
        self.listbox = tk.Listbox(self.lwindow, width= 100, height= 8, bd = 1, activestyle = 'none', 
                                    disabledforeground='black', selectbackground = 'red', 
                                    selectmode= tk.MULTIPLE)
        self.phF = font.Font(family='TkCaptionFont', size=16, weight='bold')
        self.lwl = tk.Label(self.lwindow, font=self.phF, text="Plate File Lists", fg="#3392ed")
        self.lwl.pack()
        self.listbox.pack(fill='x')
        self.bf = tk.Frame(self.lwindow)
        self.lbut = tk.Button(self.bf, text = 'Select File(s)', command = self.bfil)
        self.lbut.grid(row=0,column=1)
        self.rmb = tk.Button(self.bf, text = 'Remove File(s)', command=lambda lb=self.listbox: self.listbox.delete(tk.ACTIVE))  
        self.rmb.grid(row=0,column=0)
        self.next_button = tk.Button(self.bf, text="Next >>", command=self.parentc.next)
        self.next_button.grid(row=0,column=5)
        self.bf.pack()

    def bfil(self):
        self.filez = tk.filedialog.askopenfilenames(parent=self.lwindow,title='Choose a file',
                                                    multiple=True, filetypes =[('all files','.*'),
                                                    ('text files', '.txt')] )
        #var = tk.splitlist(self.filez)
        for i in self.filez:
            self.listbox.insert(tk.END, i)
    
class Step2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.shape_fill_status = tk.StringVar()

        shape_fill_frame = tk.Frame(self)
        shape_fill_label = tk.Label(shape_fill_frame, text="Antigen in assay: ",  anchor="w")
        shape_fill_label.pack(side=tk.LEFT, padx = 10)
        shape_fill_false = tk.Radiobutton(shape_fill_frame, text = "No", variable = self.shape_fill_status, value = 0)
        shape_fill_true = tk.Radiobutton(shape_fill_frame, text = "Yes", variable = self.shape_fill_status, value = 1)
        self.shape_fill_status.set(2)
        shape_fill_false.pack(side=tk.LEFT, padx = 10)
        shape_fill_true.pack(side=tk.LEFT, padx = 10)
        
        header = tk.Label(self, text="Select antigen presense", bd=2, relief="groove",pady=5)
        header.pack(side="top", fill="x")
        shape_fill_frame.pack(pady=45)



class Step3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.shape_fill_status = tk.StringVar()

        shape_fill_frame = tk.Frame(self)
        shape_fill_label = tk.Label(shape_fill_frame, text="Format: ",  anchor="w")
        shape_fill_label.pack(side=tk.LEFT, padx = 10)
        shape_fill_false = tk.Radiobutton(shape_fill_frame, text = "Reverse", variable = self.shape_fill_status, value = 0)
        shape_fill_true = tk.Radiobutton(shape_fill_frame, text = "PK", variable = self.shape_fill_status, value = 1)
        self.shape_fill_status.set(2)
        shape_fill_false.pack(side=tk.LEFT, padx = 10)
        shape_fill_true.pack(side=tk.LEFT, padx = 10)
       
        self.header = tk.Label(self, text="Select assay format", bd=2, relief="groove",pady=5)
        self.header.pack(side="top", fill="x")
        shape_fill_frame.pack(pady=45)


class Step4(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parentc = parent

        shape_fill_frame = tk.Frame(self)
        self.small_font = font.Font(family='TkDefaultFont', size=12, weight='normal')
        content_frame_c = parent.content_frame
        shape_fill_status = tk.StringVar()

        
        self.shape_fill_frame1 = tk.Frame(self)
        self.con1_label = tk.Label(self.shape_fill_frame1,font= self.small_font, text="Concentration, {0} #1".format(""),  anchor="w")
        self.E1 = tk.Entry(self.shape_fill_frame1, width=8)
        self.shape_fill_frame2 = tk.Frame(self)
        self.con2_label = tk.Label(self.shape_fill_frame2, font= self.small_font, text="Concentration, {0} #2".format(""),  anchor="w")
        self.E2 = tk.Entry(self.shape_fill_frame2, width=8)
        self.shape_fill_frame3 = tk.Frame(self)
        self.con3_label = tk.Label(self.shape_fill_frame3, font= self.small_font, text="Concentration, {0} #3".format(""),  anchor="w")
        self.E3 = tk.Entry(self.shape_fill_frame3, width=8)

        self.con1_label.pack(side=tk.LEFT)
        self.E1.pack(side=tk.LEFT)

        self.conA_label = tk.Label(self.shape_fill_frame1, font=self.small_font, text="Concentration,\n Soluble Antigen")
        self.E4 = tk.Entry(self.shape_fill_frame1, width=8)
        self.fval = tk.StringVar()
        self.fval.set('Select Format')
        self.fmen = tk.OptionMenu(self.shape_fill_frame2, self.fval,'Format 1','Format 2','Format 3','Format 4','Format 5','Format 6')
        self.fbut = tk.Button(self.shape_fill_frame3, text = 'Format Help', command = self.fhelp)
        self.pbut = tk.Button(self.shape_fill_frame3, text = 'Plate', command = self.phelp)
        self.header = tk.Label(self, text='', bd=2, relief="groove",pady=5)
        
   
    def init2(self):
        #self.pack_forget()
        
        #self.parentc = parent

        self.shape_fill_frame1.pack_forget()   
        self.shape_fill_frame2.pack_forget()   
        self.shape_fill_frame3.pack_forget()  
        self.E4.pack_forget()
        self.conA_label.pack_forget()
        self.fbut.pack_forget()
        self.fmen.pack_forget()
        self.pbut.pack_forget()

        shape_fill_frame = tk.Frame(self)

        #content_frame_c = parent.content_frame
        shape_fill_status = tk.StringVar()

        AF = self.parentc.s4()

        if str(AF[1]) == '1':
            cstr = "Drug"
        else:
            cstr = "Anti-ID"

        self.con1_label.config(text="Concentration, {0} #1".format(cstr))
        self.con2_label.config(text="Concentration, {0} #2".format(cstr))
        self.con3_label.config(text="Concentration, {0} #3".format(cstr))

        self.con1_label.pack(side=tk.LEFT,fill="x",padx=5)
        self.E1.pack(side=tk.LEFT,padx=5)

        
        if str(AF[0]) == '1':
            #self.conA_label = tk.Label(self.shape_fill_frame1, text="Conc. Ant.: ")
            #self.E4 = tk.Entry(self.shape_fill_frame1, width=5)
            self.E4.pack(side=tk.RIGHT,padx=3)
            self.conA_label.pack(side=tk.RIGHT,fill="x",padx=5)

        self.con2_label.pack(side=tk.LEFT,padx=5)
        self.E2.pack(side=tk.LEFT,padx=5)
        if str(AF[1]) == '1' and not self.parentc.MP:
            #self.fval = tk.StringVar()
            #self.fval.set('Select Format')
            #self.fmen = tk.OptionMenu(self.shape_fill_frame2, self.fval,'Format 1','Format 2','Format 3','Format 4','Format 5','Format 6')
            self.fmen.pack(side=tk.RIGHT,padx=5)
        self.con3_label.pack(side=tk.LEFT,padx=5)
        self.E3.pack(side=tk.LEFT,padx=5)
        self.pbut.pack(side=tk.RIGHT,padx=5)
        if str(AF[1]) == '1' and not self.parentc.MP:
            #self.fbut = tk.Button(self.shape_fill_frame3, text = 'Format Help', command = self.fhelp)
            self.fbut.pack(side=tk.RIGHT,padx=3)
        

        if str(AF[1]) == '1':
            htext = 'Denote concentrations (i.e. "10 ng/mL") & Format'
        else:
            htext = 'Denote concentrations (i.e. "10 ng/mL")'


        self.header.config(text=htext)
        self.header.pack(side="top", fill="x")

        self.shape_fill_frame1.pack(pady=4,fill="x")
        self.shape_fill_frame2.pack(pady=4,fill="x")
        self.shape_fill_frame3.pack(pady=4,fill="x")
    def fhelp(self):
        print(self.parentc.s4())
        fhwindow = tk.Toplevel(self)
        #fhwindow.tk.call('tk', 'scaling', '-displayof', '.', 50)
        img = ImageTk.PhotoImage(Image.open('Formats.jpg'))
        panel = tk.Label(fhwindow, image = img)
        panel.pack()
        fhwindow.mainloop()
    def phelp(self):
        try:
            self.pwindow.destroy()
        except:
            pass
        self.pwindow = tk.Toplevel(self)
        AF = self.parentc.s4()
        if AF[0] == '1' and AF[1] == '0':
            img = ImageTk.PhotoImage(Image.open('AF00.png'))
            panel = tk.Label(self.pwindow, image = img)
            panel.pack()
            self.pwindow.mainloop()
        if AF[0] == '1' and AF[1] == '1':
            img = ImageTk.PhotoImage(Image.open('AF01.png'))
            panel = tk.Label(self.pwindow, image = img)
            panel.pack()
            self.pwindow.mainloop()
        if AF[0] == '0' and AF[1] == '1':
            img = ImageTk.PhotoImage(Image.open('AF11.png'))
            panel = tk.Label(self.pwindow, image = img)
            panel.pack()
            self.pwindow.mainloop()
        if AF[0] == '0' and AF[1] == '0':
            img = ImageTk.PhotoImage(Image.open('AF10.png'))
            panel = tk.Label(self.pwindow, image = img)
            panel.pack()
            self.pwindow.mainloop()




class Step5(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parentc = parent
        content_frame2 = parent.content_frame
        self.sfs = parent.assayt
        print(self.sfs)
        print(type(self.sfs))

        shape_fill_frame = tk.Frame(self)
  
        self.w_button = tk.Button(shape_fill_frame, text = "Assignment Window",command = self.window_open)
        self.w_button.pack(pady=30)


        header = tk.Label(self, text="Assign IDs", bd=2, relief="groove",pady=5)
        header.pack(side="top", fill="x")
        shape_fill_frame.pack(pady=15)

    def window_open(self):
        try:
            if 'normal' == self.parentc.newwindow.state():
                pass
        except:
            self.parentc.id_assing()


class Step6(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parentc = parent
        #self.varbt 
        self.phF = font.Font(family='TkCaptionFont', size=16, weight='bold')
        content_frame2 = parent.content_frame
        self.sfs = parent.assayt
        print(self.sfs)
        print(type(self.sfs))
        self.sar = None
        shape_fill_frame = tk.Frame(self)
  
        self.w_button = tk.Button(shape_fill_frame, text = "Score Window",command = self.window_open)
        self.w_button.pack(pady=30)


        header = tk.Label(self, text="Assign Scoring Thresholds", bd=2, relief="groove",pady=5)
        header.pack(side="top", fill="x")
        shape_fill_frame.pack(pady=15)
    
    def window_open(self):
        try:
            if 'normal' == self.swindow.state():
                pass
        except:
            self.s_window()
    def s_window(self):
        self.swindow = tk.Toplevel(self)
        #self.swindow.tk.call('tk', 'scaling', '-displayof', '.', 50)
        #self.swindow.rowconfigure(0, weight=1)
        self.L = tk.Label(self.swindow,text="Score Formating", font=self.phF, fg="#3392ed", anchor='n')
        self.L.pack(fill=tk.BOTH, expand=1)
        self.sv_t = None
        self.sv_v = None
        self.sar=None
        #self.loading_window 

        if self.parentc.varbt[0] == 'r':
            if self.parentc.varbt[1] == '2':
                print(self.parentc.varbt)
                self.blank_matrix = scorrer_box(self.swindow,["Matrix Interference", '% dif.',[10,20], [2,1,0]])
                self.blank_matrix.pack(fill=tk.BOTH, expand=1)
            else:
                self.blank_matrix = scorrer_box(self.swindow,["Matrix Interference", '% dif.',[10,20], [2,1,0]])
                self.blank_matrix.pack(fill=tk.BOTH, expand=1)
                self.blank_buffer = scorrer_box(self.swindow,["Buffer Interference", '% dif.',[10,20], [2,1,0]])
                self.blank_buffer.pack(fill=tk.BOTH, expand=1)  
                self.ant_matrix = scorrer_box(self.swindow,["Soluble Antigen in Matrix Interference", '% dif. due to\nsol. ant. int.',[10,20], [2,1,0]])
                self.ant_matrix.pack(fill=tk.BOTH, expand=1)
                self.ant_buffer = scorrer_box(self.swindow,["Soluble Antigen in Buffer Interference", '% dif. due to\nsol. ant. int.',[10,20], [2,1,0]])
                self.ant_buffer.pack(fill=tk.BOTH, expand=1)
        else:
            self.background = scorrer_box(self.swindow,["Background", 'Absolut Counts.',[200,750], [0,-1,-2]])
            self.background.pack(fill=tk.BOTH, expand=1)
            self.S2N = scorrer_box(self.swindow,["Signal to Noise\n(LLT/background)", '% dif.',[3,5,10], [0,1,2,3]])
            self.S2N.pack(fill=tk.BOTH, expand=1)  
            self.LLT = scorrer_box(self.swindow,["Sensitivity (LLT)", 'LLT-Background\n(absolut counts)',[500,1000], [0,1,2]])
            self.LLT.pack(fill=tk.BOTH, expand=1)
            self.ULT = scorrer_box(self.swindow,["Sensitivity (ULT)", 'ULT-Background\n(absolut counts)',[65000,100000], [0,1,2]])
            self.ULT.pack(fill=tk.BOTH, expand=1)
            if self.parentc.varbt[1] == '1':
                self.ANT = scorrer_box(self.swindow,["Soluble Antigen Interference", '% dif. due to\nsol. ant. int.',[10,20,30], [2,1,0,-2]])
                self.ANT.pack(fill=tk.BOTH, expand=1)                        

        self.BL = tk.Frame(self.swindow)
        self.legend_button = tk.Button(self.BL,text="Legend", command=self.legend_f)
        self.legend_button.pack(fill=tk.BOTH, expand=1,side='left')
        self.wu_button = tk.Button(self.BL, text = "Update",command = self.sup)
        self.wu_button.pack(fill=tk.BOTH, expand=1,side="right")
        self.wd_button = tk.Button(self.BL, text = "Default",command = self.defs)
        self.wd_button.pack(fill=tk.BOTH, expand=1,side="left")
        self.BL.pack(fill=tk.BOTH, expand=1,side = "bottom")

    def legend_f(self):
        self.fwindow = tk.Toplevel(self)
        legend_text = tk.Label(self.fwindow, text="this is some text")
        legend_text.pack()

    def sup(self):
        vp = True
        if self.parentc.varbt == "r2":
            self.sv_t = [self.blank_matrix.ret_vals()[0]]
            self.sv_v = [self.blank_matrix.ret_vals()[1]]
        elif self.parentc.varbt == "r1":
            self.sv_t = [self.blank_matrix.ret_vals()[0],self.blank_buffer.ret_vals()[0],
                         self.ant_matrix.ret_vals()[0],self.ant_buffer.ret_vals()[0]]
            self.sv_v = [self.blank_matrix.ret_vals()[1],self.blank_buffer.ret_vals()[1],
                         self.ant_matrix.ret_vals()[1],self.ant_buffer.ret_vals()[1]]
        elif self.parentc.varbt == "p2":
            self.sv_t = [self.background.ret_vals()[0],self.S2N.ret_vals()[0],self.LLT.ret_vals()[0],
                         self.ULT.ret_vals()[0]]
            self.sv_v = [self.background.ret_vals()[1],self.S2N.ret_vals()[1],self.LLT.ret_vals()[1],
                         self.ULT.ret_vals()[1]]        
        else:
            self.sv_t = [self.background.ret_vals()[0],self.S2N.ret_vals()[0],self.LLT.ret_vals()[0],
                         self.ULT.ret_vals()[0],self.ANT.ret_vals()[0]]
            self.sv_v = [self.background.ret_vals()[1],self.S2N.ret_vals()[1],self.LLT.ret_vals()[1],
                         self.ULT.ret_vals()[1],self.ANT.ret_vals()[1]]  
                
        if self.sv_t != None:
            vl = []
            for i in self.sv_t:
                if "" not in i:
                    vl.append(i)
                    print(i)
                    for j in i:
                        try:
                            float(j)
                        except:
                            vp = False
                            tk.messagebox.showwarning("Entry Error", "Threshold Values must be numeric",icon="warning")
                            break
                    if not all(float(y) < float(z) for y, z in zip(i, i[1:])):
                        vp = False
                        tk.messagebox.showwarning("Entry Error", "Threshold values must increase in order",icon="warning")                        
                else:
                    vp = False
                    tk.messagebox.showwarning("Entry Error", "Complete scorring before updating",icon="warning")
                    break
            if vp:
                vl2 = []
                for i in self.sv_v:
                    if "" not in i:
                        vl2.append(i)
                        try:
                            float(j)
                        except:
                            vp = False
                            tk.messagebox.showwarning("Entry Error", "Score values must be numeric",icon="warning")
                            break
                    else:
                        vp = False
                        tk.messagebox.showwarning("Entry Error", "Complete scorring before updating",icon="warning")
                        break
        else:
            vp = False
            tk.messagebox.showwarning("Entry Error", "Complete scorring before updating",icon="warning")
            
        if vp:
            self.sar = [vl,vl2]
            self.swindow.destroy()
        
    def defs(self):
        if self.parentc.varbt == 'r2':
            self.blank_matrix.default_meth()
        if self.parentc.varbt == 'r1':
            self.blank_matrix.default_meth()
            self.blank_buffer.default_meth()
            self.ant_matrix.default_meth()
            self.ant_buffer.default_meth()
        if self.parentc.varbt == 'p2':
            self.background.default_meth()
            self.S2N.default_meth()
            self.LLT.default_meth()
            self.ULT.default_meth()
        if self.parentc.varbt == 'p1':
            self.background.default_meth()
            self.S2N.default_meth()
            self.LLT.default_meth()
            self.ULT.default_meth()
            self.ANT.default_meth()

class Step7(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parentc = parent
        #self.varbt 
        self.phF = font.Font(family='TkCaptionFont', size=16, weight='bold')
        content_frame2 = parent.content_frame
        self.sfs = parent.assayt
        print(self.sfs)
        print(type(self.sfs))


        shape_fill_frame = tk.Frame(self)
  
        self.w_button = tk.Button(shape_fill_frame, text = "Review Window",command = self.window_open)
        self.w_button.pack(pady=0)


        header = tk.Label(self, text="Review inputs and create sheet", bd=2, relief="groove",pady=5)
        header.pack(side="top", fill="x")
        shape_fill_frame.pack(pady=45)
    
    def window_open(self):
        try:
            if 'normal' == self.rwindow.state():
                pass
        except:
            if self.parentc.MP:
                self.MP_CV = 0
                self.r_window_MP(MP_C=self.MP_CV)
            else:
                self.r_window()

    def make_sheet(self):
        file = self.file.get()
        if self.AssayFrame["text"] == "Anti-ID Screen":
            file1 = file.replace(" ", "\ ")
            file_2 = file.replace(".txt","_scripted.xlsx")
            l = ""
            l = self.exp_1.name()
            l = l + self.exp_2.name()
            l = l + self.exp_3.name()
            l = l + self.exp_4.name()
            l = l + self.exp_5.name()
            l = l + self.exp_6.name()
            process = subprocess.run(["python", "plate_2_score.py", "-d", f"{file}", "-x", f"{file_2}", "-l", l])
        else:
            file1 = file.replace(" ", "\ ")
            file_2 = file.replace(".txt","_scripted.xlsx")
            l = ""
            l = self.exp_1.name()
            l = l + self.exp_2.name()
            l = l + self.exp_3.name()
            l = l + self.exp_4.name()
            process = subprocess.run(["python", "reverse_screen.py", "-d", f"{file}", "-x", f"{file_2}", "-l", l])


    def r_window_MP(self,MP_C=None):
        print('hi')
        
        ant = "No"
        form = "Reverse"
        if self.parentc.steps[1].shape_fill_status.get() == '1':
            ant = "Yes"
        if self.parentc.steps[2].shape_fill_status.get() == '1':
            form = "PK"


        con1 = self.parentc.steps[3].E1.get()
        con2 = self.parentc.steps[3].E2.get()
        con3 = self.parentc.steps[3].E3.get()

        id_labels = self.parentc.id_ased_L[MP_C]
        if self.parentc.varbt[0] == 'p':
            idc  = self.parentc.id_asedc_L[MP_C]

        score_values = self.parentc.steps[5].sar

        s0 = score_values[0]
        print(s0)
        s1 = score_values[1]
        print(s1)


        self.rwindow = tk.Toplevel(self)
        #self.rwindow.state('zoomed')
        #self.rwindow.tk.call('tk', 'scaling', '-displayof', '.', 50)
        L = tk.Label(self.rwindow,text="Input Review", font=self.phF, fg="#3392ed", anchor='n')
        L.grid(columnspan=6)
        fn = tk.Label(self.rwindow,text="File path:{0}".format(self.parentc.tlvs[MP_C])).grid(columnspan=6)
        ft = ""
        if self.parentc.varbt[0] == 'p':
            ft = self.parentc.MP_FL[MP_C]

        ffm = tk.Label(self.rwindow,text="Antigen: {0}        Format: {1}".format(ant,form)+ft).grid(columnspan=6,row=2)

        ctext = "Concentrations:  #1:{0}  #2:{1}  #3:{2}".format(con1,con2,con3)
        if self.parentc.varbt[1] == '1':
            ctext = ctext + "  Ant:{0}".format(self.parentc.steps[3].E4.get())
        conl = tk.Label(self.rwindow,text=ctext).grid(columnspan=6,row=3)
        self.sth =[]
        self.sts =[]
        if self.parentc.varbt == 'r2':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            for i in range(0,4):
                idt = tk.Label(self.rwindow,text="ID {0}: {1}".format(i+1,id_labels[i])).grid(column=1+i,row=5)
            for i in range(0,4):
                idt =  tk.Label(self.rwindow,text="ID {0}: {1}".format(i+5,id_labels[i+4])).grid(column=1+i,row=6)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=7,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Blank Matrix:").grid(row=8,column=2)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=9,columnspan=3,column=2)
        if self.parentc.varbt == 'r1':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            for i in range(0,4):
                idt = tk.Label(self.rwindow,text="ID {0}: {1}".format(i+1,id_labels[i])).grid(column=1+i,row=5)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=7,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Blank Matrix:").grid(row=8,column=0)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=9,columnspan=3,column=0)
            sl = tk.Label(self.rwindow,text="Blank Buffer:").grid(row=8,column = 3)
            #####
            tv2 = s0[1]
            ###
            tv2a = s1[1]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=9,columnspan=3,column=3)
            sl = tk.Label(self.rwindow,text="Antigen in Matrix:").grid(row=10,column = 0)
            
            sl = tk.Label(self.rwindow,text="Antigen in Buffer:").grid(row=10,column = 3)
            #####
            tv2 = s0[2]
            ###
            tv2a = s1[2]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=0)

            #####
            tv2 = s0[3]
            ###
            tv2a = s1[3]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=3)
        if self.parentc.varbt == 'p2':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            idt = tk.Label(self.rwindow,text="ID-Biotin 1: {0} [{1}]".format(id_labels[6],idc[6])).grid(columnspan=6,row=5)
            for i in range(0,6):
                idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1} [{2}]".format(i+1,id_labels[i],idc[i])).grid(column=i,row=6)
            idt = tk.Label(self.rwindow,text="ID-Biotin 2: {0}".format(id_labels[-1],idc[-1])).grid(columnspan=6,row=7)
            for i in range(7,13):
                idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1} [{2}]".format(i,id_labels[i],idc[i])).grid(column=i-7,row=8)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=9,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Background:").grid(row=10,column=0)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=0)

            sl = tk.Label(self.rwindow,text="Signal to Noise:").grid(row=10,column = 3)
            #####
            tv2 = s0[1]
            ###
            tv2a = s1[1]
            self.sth.append(tv2)
            self.sts.append(tv2a)        
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=3)


            sl = tk.Label(self.rwindow,text="Sensitivity (LLT):").grid(row=12,column = 0)
            sl = tk.Label(self.rwindow,text="Sensitivity (ULT):").grid(row=12,column = 3)

            #####
            tv2 = s0[2]
            ###
            tv2a = s1[2]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=0)

            #####
            tv2 = s0[3]
            ###
            tv2a = s1[3]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=3)
        if self.parentc.varbt == 'p1':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            idt = tk.Label(self.rwindow,text="ID-Biotin 1: {0} [{1}]".format(id_labels[6],idc[6])).grid(columnspan=6,row=5)
            for i in range(0,6):
                idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1} [{2}]".format(i+1,id_labels[i],idc[i])).grid(column=i,row=6)
            #idt = tk.Label(self.rwindow,text="ID-Biotin 2: {0}".format(id_labels[-1])).grid(columnspan=6,row=7)
            #for i in range(7,13):
            #    idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1}".format(i,id_labels[i])).grid(column=i-7,row=8)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=9-2,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Background:").grid(row=10-2,column=0)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11-2,columnspan=3,column=0)

            sl = tk.Label(self.rwindow,text="Signal to Noise:").grid(row=10-2,column = 3)
            #####
            tv2 = s0[1]
            ###
            tv2a = s1[1]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11-2,columnspan=3,column=3)


            sl = tk.Label(self.rwindow,text="Sensitivity (LLT):").grid(row=12-2,column = 0)
            sl = tk.Label(self.rwindow,text="Sensitivity (ULT):").grid(row=12-2,column = 3)

            #####
            tv2 = s0[2]
            ###
            tv2a = s1[2]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=0)

            #####
            tv2 = s0[3]
            ###
            tv2a = s1[3]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=3)

            #####
            tv2 = s0[4]
            ###
            tv2a = s1[4]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]
            sl = tk.Label(self.rwindow,text="Antigen in Matrix:").grid(row=14,column = 2,columnspan=2)    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=15,columnspan=2,column=2)
        self.new_file_f = tk.Frame(self.rwindow)
        #self.new_file_handle = tk.StringVar()

        if MP_C == 0:
            self.nfe = tk.Entry(self.new_file_f, state="disabled", width = 50 )
        else:
            text4nfe = self.nfev
            self.nfe = tk.Entry(self.new_file_f, width = 50 )
            self.nfe.insert(0, text4nfe)
            self.nfe.config(state="disabled")

        self.nfel = tk.Label(self.new_file_f, text="Save to:")
        self.nfb = tk.Button(self.new_file_f, text="Browse Directory", command = self.browser )
        self.nfel.pack(side="left")
        self.nfe.pack(side="left")
        self.nfb.pack(side="left")
        self.nhel = tk.Label(self.new_file_f, text="Save as:")
        self.nhel.pack(side="left")
        self.nhe = tk.Entry(self.new_file_f, width = 25 )
        self.nhe.pack(side="left")
        self.new_file_f.grid(columnspan=6)
        #self.MP_CV = None
        #if self.parentc.MP:
        #    self.MP_CV = 0
        self.sb = tk.Button(self.rwindow,text="Save",command=self.saver)
        self.sb.grid(column=6)


    def r_window(self):
        print('hi')
        
        ant = "No"
        form = "Reverse"
        if self.parentc.steps[1].shape_fill_status.get() == '1':
            ant = "Yes"
        if self.parentc.steps[2].shape_fill_status.get() == '1':
            form = "PK"


        con1 = self.parentc.steps[3].E1.get()
        con2 = self.parentc.steps[3].E2.get()
        con3 = self.parentc.steps[3].E3.get()

        id_labels = self.parentc.id_ased
        if self.parentc.varbt[0] == 'p':
            idc  = self.parentc.id_asedc

        score_values = self.parentc.steps[5].sar

        s0 = score_values[0]
        print(s0)
        s1 = score_values[1]
        print(s1)


        self.rwindow = tk.Toplevel(self)
        #self.rwindow.state('zoomed')
        #self.rwindow.tk.call('tk', 'scaling', '-displayof', '.', 50)
        L = tk.Label(self.rwindow,text="Input Review", font=self.phF, fg="#3392ed", anchor='n')
        L.grid(columnspan=6)
        fn = tk.Label(self.rwindow,text="File path:{0}".format(self.parentc.steps[0].fileE.get())).grid(columnspan=6)
        ft = ""
        if self.parentc.varbt[0] == 'p':
            ft = self.parentc.steps[3].fval.get()

        ffm = tk.Label(self.rwindow,text="Antigen: {0}        Format: {1}".format(ant,form)+ft).grid(columnspan=6,row=2)

        ctext = "Concentrations:  #1:{0}  #2:{1}  #3:{2}".format(con1,con2,con3)
        if self.parentc.varbt[1] == '1':
            ctext = ctext + "  Ant:{0}".format(self.parentc.steps[3].E4.get())
        conl = tk.Label(self.rwindow,text=ctext).grid(columnspan=6,row=3)
        self.sth =[]
        self.sts =[]
        if self.parentc.varbt == 'r2':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            for i in range(0,4):
                idt = tk.Label(self.rwindow,text="ID {0}: {1}".format(i+1,id_labels[i])).grid(column=1+i,row=5)
            for i in range(0,4):
                idt =  tk.Label(self.rwindow,text="ID {0}: {1}".format(i+5,id_labels[i+4])).grid(column=1+i,row=6)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=7,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Blank Matrix:").grid(row=8,column=2)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=9,columnspan=3,column=2)
        if self.parentc.varbt == 'r1':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            for i in range(0,4):
                idt = tk.Label(self.rwindow,text="ID {0}: {1}".format(i+1,id_labels[i])).grid(column=1+i,row=5)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=7,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Blank Matrix:").grid(row=8,column=0)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=9,columnspan=3,column=0)
            sl = tk.Label(self.rwindow,text="Blank Buffer:").grid(row=8,column = 3)
            #####
            tv2 = s0[1]
            ###
            tv2a = s1[1]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=9,columnspan=3,column=3)
            sl = tk.Label(self.rwindow,text="Antigen in Matrix:").grid(row=10,column = 0)
            
            sl = tk.Label(self.rwindow,text="Antigen in Buffer:").grid(row=10,column = 3)
            #####
            tv2 = s0[2]
            ###
            tv2a = s1[2]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=0)

            #####
            tv2 = s0[3]
            ###
            tv2a = s1[3]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=3)
        if self.parentc.varbt == 'p2':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            idt = tk.Label(self.rwindow,text="ID-Biotin 1: {0} [{1}]".format(id_labels[6],idc[6])).grid(columnspan=6,row=5)
            for i in range(0,6):
                idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1} [{2}]".format(i+1,id_labels[i],idc[i])).grid(column=i,row=6)
            idt = tk.Label(self.rwindow,text="ID-Biotin 2: {0}".format(id_labels[-1],idc[-1])).grid(columnspan=6,row=7)
            for i in range(7,13):
                idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1} [{2}]".format(i,id_labels[i],idc[i])).grid(column=i-7,row=8)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=9,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Background:").grid(row=10,column=0)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=0)

            sl = tk.Label(self.rwindow,text="Signal to Noise:").grid(row=10,column = 3)
            #####
            tv2 = s0[1]
            ###
            tv2a = s1[1]
            self.sth.append(tv2)
            self.sts.append(tv2a)        
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11,columnspan=3,column=3)


            sl = tk.Label(self.rwindow,text="Sensitivity (LLT):").grid(row=12,column = 0)
            sl = tk.Label(self.rwindow,text="Sensitivity (ULT):").grid(row=12,column = 3)

            #####
            tv2 = s0[2]
            ###
            tv2a = s1[2]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=0)

            #####
            tv2 = s0[3]
            ###
            tv2a = s1[3]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=3)
        if self.parentc.varbt == 'p1':
            idl = tk.Label(self.rwindow,text="IDs:").grid()
            idt = tk.Label(self.rwindow,text="ID-Biotin 1: {0} [{1}]".format(id_labels[6],idc[6])).grid(columnspan=6,row=5)
            for i in range(0,6):
                idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1} [{2}]".format(i+1,id_labels[i],idc[i])).grid(column=i,row=6)
            #idt = tk.Label(self.rwindow,text="ID-Biotin 2: {0}".format(id_labels[-1])).grid(columnspan=6,row=7)
            #for i in range(7,13):
            #    idt = tk.Label(self.rwindow,text="ID-Tag {0}: {1}".format(i,id_labels[i])).grid(column=i-7,row=8)
            slf = tk.Frame(self.rwindow,bd=2,relief=tk.RIDGE,width=300)
            slf.grid(row=9-2,columnspan=6)
            sl = tk.Label(master=slf,text="                                         Scoring Format                                         ")
            sl.pack(fill='x',expand = False, padx=2,pady=1)
            sl2 = tk.Label(self.rwindow,text="Background:").grid(row=10-2,column=0)
            #####
            tv2 = s0[0]
            ###
            tv2a = s1[0]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11-2,columnspan=3,column=0)

            sl = tk.Label(self.rwindow,text="Signal to Noise:").grid(row=10-2,column = 3)
            #####
            tv2 = s0[1]
            ###
            tv2a = s1[1]
            self.sth.append(tv2)
            self.sts.append(tv2a)
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=11-2,columnspan=3,column=3)


            sl = tk.Label(self.rwindow,text="Sensitivity (LLOQ):").grid(row=12-2,column = 0)
            sl = tk.Label(self.rwindow,text="Sensitivity (ULOQ):").grid(row=12-2,column = 3)

            #####
            tv2 = s0[2]
            ###
            tv2a = s1[2]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=0)

            #####
            tv2 = s0[3]
            ###
            tv2a = s1[3]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=13,columnspan=3,column=3)

            #####
            tv2 = s0[4]
            ###
            tv2a = s1[4]
            self.sth.append(tv2)
            self.sts.append(tv2a)    
            text =""
            for i in range(len(tv2)):
                text = text+"<"+tv2[i]+" – "+tv2a[i]+"\n"  
            text = text+">"+tv2[-1]+" – "+tv2a[-1]
            sl = tk.Label(self.rwindow,text="Antigen in Matrix:").grid(row=14,column = 2,columnspan=2)    
            tvl2 = tk.Label(self.rwindow,text=text).grid(row=15,columnspan=2,column=2)
        self.new_file_f = tk.Frame(self.rwindow)
        #self.new_file_handle = tk.StringVar()


        self.nfel = tk.Label(self.new_file_f, text="Save to:")
        self.nfe = tk.Entry(self.new_file_f, state="disabled", width = 50 )
        self.nfb = tk.Button(self.new_file_f, text="Browse Directory", command = self.browser )
        self.nfel.pack(side="left")
        self.nfe.pack(side="left")
        self.nfb.pack(side="left")
        self.nhel = tk.Label(self.new_file_f, text="Save as:")
        self.nhel.pack(side="left")
        self.nhe = tk.Entry(self.new_file_f, width = 25 )
        self.nhe.pack(side="left")
        self.new_file_f.grid(columnspan=6)
        #self.MP_CV = None
        self.sb = tk.Button(self.rwindow,text="Save",command=self.saver)
        self.sb.grid(column=6)

    def browser(self):
        self.nfe.config(state="normal")
        directory = filedialog.askdirectory(title = "Select Directory")
        self.nfe.delete(0, tk.END)
        self.nfe.insert(0, str(directory)+"/")
        self.nfe.config(state="disabled")

    def on_closing(self):
        pass

    def saver(self):

        print("testing runner")
        self.running = tk.Toplevel(self)
        self.running.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.running_l = tk.Label(self.running, text="Running Plate Writer",font=self.phF)
        self.running_l.pack()
        self.running.update()
        self.sb.config(state="disabled")
        self.nfb.config(state="disabled")
        self.nhe.config(state="disabled")

        self.nfev = self.nfe.get()
        dirr = self.nfe.get()
        filn = self.nhe.get()
        if dirr == "" and filn == "":
            tk.messagebox.showwarning("Entry Error", "Provide Directory and File Name",icon="warning")
        elif dirr == "" and filn != "":
            tk.messagebox.showwarning("Entry Error", "Provide Directory",icon="warning")
        elif dirr != "" and filn == "":
            tk.messagebox.showwarning("Entry Error", "Provide File Name",icon="warning")
        else:
            if self.parentc.MP:
                file_t = self.parentc.tlvs[self.MP_CV]
            else:
                file_t = self.parentc.steps[0].fileE.get()
            file_t = file_t.replace(" ", "\ ")
            con1 = self.parentc.steps[3].E1.get()
            con2 = self.parentc.steps[3].E2.get()
            con3 = self.parentc.steps[3].E3.get()
            c = [str(con1),str(con2),str(con3)]
            if self.parentc.MP:
                id_labels = self.parentc.id_ased_L[self.MP_CV]
            else:
                id_labels = self.parentc.id_ased
            file_2 = dirr + filn + ".xlsx" #needs a checker
            print('this is the thresh')
            print(self.sth)
            print("this is the scores")
            print(self.sts)
            if not self.parentc.MP:
                if self.parentc.varbt[0] == 'r':
                    if self.parentc.varbt[1] == '1':#with antigen
                        print("reverse")
                        con4 = self.parentc.steps[3].E4.get()
                        c.append(str(con4))
                        process = subprocess.run(["python", "reverse_screen.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts)])
                    else:
                        process = subprocess.run(["python", "reverse_screen.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts)])
                else:
                    form = self.parentc.steps[3].fval.get()
                    id_cons = self.parentc.id_asedc   
                    print(id_cons)
                    print(str(self.parentc.steps[3].fval.get()))
                    print(c)
                    if self.parentc.varbt[1] == '1':#with antigen
                        con4 = self.parentc.steps[3].E4.get()
                        c.append(str(con4))
                        process = subprocess.run(["python", "plate_2_score.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts), "-f", str(self.parentc.steps[3].fval.get()), "-i", str(id_cons)])
                    else:
                        print("PK")
                        process = subprocess.run(["python", "plate_2_score.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts), "-f", str(self.parentc.steps[3].fval.get()), "-i", str(id_cons)])
                
                runningL = True
                while runningL:
                    if process.returncode == None:
                        time.sleep(2)
                        print("sleeping")
                    else:
                        self.running.destroy()
                        runningL = False
                self.rwindow.destroy()
            else:
                if self.parentc.varbt[0] == 'r':
                    if self.parentc.varbt[1] == '1':#with antigen
                        print("reverse")
                        con4 = self.parentc.steps[3].E4.get()
                        c.append(str(con4))
                        process = subprocess.run(["python", "reverse_screen.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts)])
                    else:
                        process = subprocess.run(["python", "reverse_screen.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts)])
                else:
                    if self.parentc.MP:
                        form = self.parentc.MP_FL[self.MP_CV]
                        id_cons = self.parentc.id_asedc_L[self.MP_CV]
                    else:
                        form = self.parentc.steps[3].fval.get()
                        id_cons = self.parentc.id_asedc  
                
                    if self.parentc.varbt[1] == '1':#with antigen
                        con4 = self.parentc.steps[3].E4.get()
                        c.append(str(con4))
                        process = subprocess.run(["python", "plate_2_score.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts), "-f", str(self.parentc.steps[3].fval.get()), "-i", str(id_cons)])
                    else:
                        print("PK")
                        process = subprocess.run(["python", "plate_2_score.py", "-d", f"{file_t}", "-x", f"{file_2}", "-l", str(id_labels), "-c",
                                                str(c), "-t", str(self.sth), "-s", str(self.sts), "-f", str(self.parentc.steps[3].fval.get()), "-i", str(id_cons)])
                
                runningL = True
                while runningL:
                    if process.returncode == None:
                        time.sleep(2)
                        print("sleeping")
                    else:
                        self.running.destroy()
                        runningL = False
                self.MP_CV += 1
                if self.MP_CV != len(self.parentc.tlvs):
                    self.rwindow.destroy()
                    self.r_window_MP(MP_C=self.MP_CV)

        

class Wizard(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.step_in = False
        #self.state('zoomed')
        self.id_ased = None
        self.varbs = None
        self.varbt = None
        self.sar = None
        self.phF = font.Font(family='TkCaptionFont', size=16, weight='bold')
        self.phF2 = font.Font(family='TkCaptionFont', size=12, weight='bold')
        self.minsize(654,194)
        self.maxsize(654,194)
        self.assayt = 2
        self.MP = False
        self.winfo_toplevel().title("WAND")

        '''
        self.img = ImageTk.PhotoImage(Image.open('logo.png'))
        self.panel = tk.Label(self, image = self.img)
        self.panel.place(anchor="ne",bordermode=tk.INSIDE,height=10)
        self.panel.pack()
        '''

        self.ph = tk.Frame(self)
        self.ph_text = tk.Label(self.ph,text="Plate Wizard", font=self.phF, fg="#3392ed", anchor='n')
        
        #self.iff.place(anchor="ne")
        self.ph_text.pack(side="top",pady=0)


        self.listbox = tk.Listbox(self.ph, width= 20, height= 7, bd = 1, activestyle = 'underline', 
                                  disabledforeground='black', selectbackground = 'red', 
                                  selectmode= tk.MULTIPLE)

        self.listbox.pack(side="left")
        p_text = [ ' File Selection',' Soluble Antigen',' Reverse/PK',' Experimental Details',
                  ' ID Entry',' Scorring',' Review & Sheet Generation']
        for i in p_text:
            self.listbox.insert(tk.END, i)
        
        self.ph.pack(side="left")

        self.button_frame = tk.Frame(self,bg = '#f5f5f5', bd=1, relief="raised",height=24,width=372)
        self.content_frame = tk.Frame(self, width=500, height = 5)


        

        self.current_step = None
        self.steps = [Step1(self), Step2(self), Step3(self),Step4(self),Step5(self),Step6(self),Step7(self)]
        self.step_in = True
        self.back_button = tk.Button(self.button_frame, text="<< Back", command=self.back)
        self.next_button = tk.Button(self.button_frame, text="Next >>", command=self.next)
        self.finish_button = tk.Button(self.button_frame, text="Finish", command=self.finish)

        self.b_button = tk.Button(self.button_frame, text = "Browse File",command = self.fileDialog)

        
        self.content_frame.pack(side="top", fill="both", expand=False,pady=7)
        self.button_frame.pack(side=tk.BOTTOM, fill="x",expand=False)
        self.listbox.activate(1)
        self.listbox.itemconfig(0,bg='#006cd2')
        self.listbox.bind("<1>", self.no_op)
        self.listbox.bind("<Double-1>", self.no_op)
        print('this is a test')
        self.show_step(0)
        #self.button_frame.maxsize(10000,24)
        
    def s4(self):
        if self.step_in:
            return(self.steps[1].shape_fill_status.get() ,self.steps[2].shape_fill_status.get() )
            g = [self.steps[1].shape_fill_status.get() ,self.steps[2].shape_fill_status.get()]
            print("s4 val")
            print(g)
        else:
            return("","")

    def no_op(self, event):
        return "break"
    
    
    def show_step(self, step):

        self.sl = False

        for i in range(len(self.steps)):
            self.listbox.itemconfig(i,bg='SystemButtonFace')
        
        self.listbox.itemconfig(step,bg='#006cd2')

        print('current step is {0}'.format(step))

        if self.current_step is not None:
            # remove current step
            current_step = self.steps[self.current_step]
            current_step.pack_forget()

        self.current_step = step

        new_step = self.steps[step]
        new_step.pack(fill="both", expand=True)

        if step == 0:
            # first step
            #self.listbox.activate(0)
            self.back_button.pack_forget()
            self.next_button.pack(side="right")
            self.finish_button.pack_forget()
            self.b_button.pack(side="right",padx=150,pady=0)
            print(self.button_frame.winfo_height())



        elif step == 3:
            #if self.current_step != Step5:
            #    self.assayt = new_step.assay_t()
            #    print(self.assayt)
            self.back_button.pack(side="left")
            self.next_button.pack(side="right")
            new_step.init2()
            self.finish_button.pack_forget()

        elif step == 4:
            #if self.current_step != Step5:
            #    self.assayt = new_step.assay_t()
            #    print(self.assayt)
            self.back_button.pack(side="left")
            self.next_button.pack(side="right")
            if self.MP:
                self.id_asedc_L = []
                self.id_ased_L = []
                self.MP_FL = []
                self.MP_CV = 0
                self.id_assing(MP_C=self.MP_CV)
            else:
                self.id_assing()
            try:
                self.steps[0].lwindow.destroy()
            except:
                pass
            self.finish_button.pack_forget()
        
        elif step == 5:
            self.finish_button.pack_forget()
            self.back_button.pack(side="left")
            self.next_button.pack(side="right")
            self.steps[5].s_window()
            

        elif step == len(self.steps)-1:
            # last step
            print('last step')
            self.back_button.pack(side="left")
            self.next_button.pack_forget()
            self.finish_button.pack(side="right")


        else:
            # all other steps
            self.back_button.pack(side="left")
            self.next_button.pack(side="right")
            self.finish_button.pack_forget()
            self.b_button.pack_forget()
            print(self.button_frame.winfo_height())
            print(self.button_frame.winfo_width())

    def nfl(self):
        nfl_ml = True
        if self.current_step == 0:
            if self.steps[0].fileE.get() == "":
                self.tlvs = []
                ns1l = True
                self.MP = False
                if self.steps[0].listbox != None:
                    try:
                        self.tlvs = self.steps[0].listbox.get(0,tk.END)
                    except:
                        tk.messagebox.showwarning("Entry Error", "Select plate reading file paths",icon="warning")
                        ns1l = False
                if len(self.tlvs) < 2 and self.steps[0].lws:
                    if ns1l:
                        tk.messagebox.showwarning("Entry Error", "Select multiple plate reading file paths",icon="warning")
                    nfl_ml = False
                elif not self.steps[0].lws:
                    if ns1l:
                        tk.messagebox.showwarning("Entry Error", "Select plate reading file path",icon="warning")
                    nfl_ml = False
                elif len(self.tlvs) > 1:
                    print(self.tlvs)
                    self.MP = True
        elif self.current_step == 1:
            if self.steps[1].shape_fill_status.get() == '2':
                tk.messagebox.showwarning("Entry Error", "Select antigen presence",icon="warning")
                nfl_ml = False
        elif self.current_step == 2:
            if self.steps[2].shape_fill_status.get() == '2':
                tk.messagebox.showwarning("Entry Error", "Select plate format",icon="warning")
                nfl_ml = False
        elif self.current_step == 3:
            nfl_l = False
            AF = self.s4()
            print(AF)
            if self.steps[3].E1.get() != "":
                if self.steps[3].E2.get() != "":
                    if self.steps[3].E3.get() != "":
                        if AF[0] == '1':
                            if self.steps[3].E4.get() != "":
                                if AF[1] == '1' and not self.MP:
                                    if self.steps[3].fval.get() != 'Select Format':
                                        nfl_l = True
                                else:
                                    nfl_l = True

                        else:
                            if AF[1] == '1' and not self.MP:
                                if self.steps[3].fval.get() != 'Select Format': 
                                    nfl_l = True
                                    
                            else:
                                nfl_l = True
            if nfl_l != True:
                tk.messagebox.showwarning("Entry Error", "Enter concentrations/format",icon="warning")
                nfl_ml = False
        elif self.current_step == 4:
            if self.id_ased == None:
                tk.messagebox.showwarning("Entry Error", "Fill all label names and update",icon="warning")
                nfl_ml = False
            if self.MP and nfl_ml:
                if len(self.id_ased_L) != len(self.tlvs):
                    tk.messagebox.showwarning("Entry Error", "Complete entry for each plate.\nClick 'Assignment Window' to continue.",icon="warning")
                    nfl_ml = False  
        elif self.current_step == 5:
            if self.steps[5].sar == None:
                tk.messagebox.showwarning("Entry Error", "Fill all scoring values and update",icon="warning")
                nfl_ml = False
        if nfl_ml:
            self.sl = True
            


    def next(self):
        self.nfl()
        print(self.sl)
        if self.sl:
            self.show_step(self.current_step + 1)

    def back(self):
        print(self.current_step)
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.swindow.destroy()
        except:
            pass
        self.show_step(self.current_step - 1)

    def update(self):
        ###button function for ID entry 
        vp = True
        if self.varbt == "r2":
            self.varbs = [self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.t6.get(),self.t7.get(),self.t8.get()]
            print(self.t2.get())
            print(type(self.t2.get()))
        elif self.varbt == "r1":
            self.varbs = [self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get()]
        elif self.varbt == "p1":
            self.varbs = [self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.t6.get(),self.t7.get()]
            self.varbsc = [self.t1a.get(),self.t2a.get(),self.t3a.get(),self.t4a.get(),self.t5a.get(),self.t6a.get(),self.t7a.get()]
        else:
            self.varbs = [self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.t6.get(),self.t7.get(),
                          self.t8.get(),self.t9.get(),self.t10.get(),self.t11.get(),self.t12.get(),self.t13.get(),self.t14.get()]
            self.varbsc = [self.t1a.get(),self.t2a.get(),self.t3a.get(),self.t4a.get(),self.t5a.get(),self.t6a.get(),self.t7a.get(),
                          self.t8a.get(),self.t9a.get(),self.t10a.get(),self.t11a.get(),self.t12a.get(),self.t13a.get(),self.t14a.get()]
        if self.varbs != None:
            vl = []
            for i in self.varbs:
                if type(i) == str:
                    if i != "":
                        vl.append(i)
                    else:
                        vp = False
                        tk.messagebox.showwarning("Entry Error", "Fill all label names",icon="warning")
                        break
                else:
                    vp = False
                    tk.messagebox.showwarning("Entry Error", "Fill all label names",icon="warning")
                    break
        else:
            vp = False
            tk.messagebox.showwarning("Entry Error", "Fill all label names",icon="warning")
        if self.varbt[0] == 'p':
            vlc = []
            for i in self.varbsc:
                if type(i) == str:
                    if i != "":
                        vlc.append(i)
                    else:
                        vp = False
                        tk.messagebox.showwarning("Entry Error", "Fill all concentrations",icon="warning")
                        break
                else:
                    vp = False
                    tk.messagebox.showwarning("Entry Error", "Fill all concentrations",icon="warning")
                    break
        if self.MP and self.varbt[0] =='p':
            mpflt = self.MPmen_val.get()
            if mpflt == 'Select Format':
                vp = False
                tk.messagebox.showwarning("Entry Error", "Select Format",icon="warning")
        if vp:
            self.id_ased = vl
            if self.MP:
                self.id_ased_L.append(vl)
            if self.varbt[0] == 'p':
                self.id_asedc = vlc
                if self.MP:
                    self.id_asedc_L.append(vlc)
                    self.MP_FL.append(mpflt)
            self.newwindow.destroy()
            if self.MP and self.MP_CV != len(self.tlvs)-1:
                self.MP_CV += 1 
                self.id_assing(MP_C=self.MP_CV)



    def fileDialog(self): 
        filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetypes =
        [('all files','.*') , ('text files', '.txt')] )
        self.steps[0].fileE.configure(state="normal")
        self.steps[0].fileE.delete(0, tk.END)
        self.steps[0].fileE.insert(0, str(filename))
        self.steps[0].fileE.configure(state="disabled")
        self.MP = False 

    def fhelp(self):
        fhwindow = tk.Toplevel(self)
        #fhwindow.tk.call('tk', 'scaling', '-displayof', '.', 50)
        img = ImageTk.PhotoImage(Image.open('Formats.jpg'))
        panel = tk.Label(fhwindow, image = img)
        panel.pack()
        fhwindow.mainloop()

    def id_assing(self,MP_C=0):
        id_c = [""]
        if self.MP:
            id_c = self.tlvs
                
        self.id_ased = None  
        self.varbt = None
        self.MP_update_status = True
        self.newwindow = tk.Toplevel(self)
        #self.newwindow.state('zoomed')
        self.L = tk.Label(self.newwindow,text="ID assignment{0}".format(": \n"+id_c[MP_C]), font=self.phF, fg="#3392ed", anchor='n')
        self.L.pack(side="top")
        self.varbs = None
        A = self.steps[1].shape_fill_status.get()
        F = self.steps[2].shape_fill_status.get()
        if F == '0':
            #if the format is reverse screen
            if A == '1':
                #if there is an antigin
                # normal IDs (4 total) format
                self.varbt = 'r1'
                self.t1 = tk.StringVar() 
                idf1 = tk.Frame(self.newwindow)
                id1l = tk.Label(idf1, text="ID #1: ",  anchor="w")
                id1e = tk.Entry(idf1, textvariable = self.t1, width=10)
                id1l.pack(side="left")
                id1e.pack(side="left")
                idf1.pack()

                self.t2 = tk.StringVar()
                idf2 = tk.Frame(self.newwindow)
                id2l = tk.Label(idf2, text="ID #2: ",  anchor="w")
                id2e = tk.Entry(idf2, textvariable = self.t2, width=10)
                id2l.pack(side="left")
                id2e.pack(side="left")
                idf2.pack()

                self.t3 = tk.StringVar()
                idf3 = tk.Frame(self.newwindow)
                id3l = tk.Label(idf3, text="ID #3: ",  anchor="w")
                id3e = tk.Entry(idf3, textvariable = self.t3, width=10)
                id3l.pack(side="left")
                id3e.pack(side="left")
                idf3.pack()       
                
                self.t4  = tk.StringVar()
                idf4 = tk.Frame(self.newwindow)
                id4l = tk.Label(idf4, text="ID #4: ",  anchor="w")
                id4e = tk.Entry(idf4, textvariable = self.t4, width=10)
                id4l.pack(side="left")
                id4e.pack(side="left")
                idf4.pack()
            else:
                # 2x IDs (8 total) format
                self.varbt = 'r2'
                self.t1 = tk.StringVar() 
                idf1 = tk.Frame(self.newwindow)
                id1l = tk.Label(idf1, text="ID #1: ",  anchor="w")
                id1e = tk.Entry(idf1, textvariable = self.t1, width=10)
                id1l.pack(side="left")
                id1e.pack(side="left")
                idf1.pack()

                self.t2 = tk.StringVar()
                idf2 = tk.Frame(self.newwindow)
                id2l = tk.Label(idf2, text="ID #2: ",  anchor="w")
                id2e = tk.Entry(idf2, textvariable = self.t2, width=10)
                id2l.pack(side="left")
                id2e.pack(side="left")
                idf2.pack()

                self.t3 = tk.StringVar()
                idf3 = tk.Frame(self.newwindow)
                id3l = tk.Label(idf3, text="ID #3: ",  anchor="w")
                id3e = tk.Entry(idf3, textvariable = self.t3, width=10)
                id3l.pack(side="left")
                id3e.pack(side="left")
                idf3.pack()       
                
                self.t4  = tk.StringVar()
                idf4 = tk.Frame(self.newwindow)
                id4l = tk.Label(idf4, text="ID #4: ",  anchor="w")
                id4e = tk.Entry(idf4, textvariable = self.t4, width=10)
                id4l.pack(side="left")
                id4e.pack(side="left")
                idf4.pack()

                self.t5 = tk.StringVar()
                idf5 = tk.Frame(self.newwindow)
                id5l = tk.Label(idf5, text="ID #5: ",  anchor="w")
                id5e = tk.Entry(idf5, textvariable=self.t5, width=10)
                id5l.pack(side="left")
                id5e.pack(side="left")
                idf5.pack()

                self.t6 = tk.StringVar()
                idf6 = tk.Frame(self.newwindow)
                id6l = tk.Label(idf6, text="ID #6: ",  anchor="w")
                id6e = tk.Entry(idf6, textvariable=self.t6, width=10)
                id6l.pack(side="left")
                id6e.pack(side="left")
                idf6.pack()   

                self.t7 = tk.StringVar()
                idf7 = tk.Frame(self.newwindow)
                id7l = tk.Label(idf7, text="ID #7: ",  anchor="w")
                id7e = tk.Entry(idf7, textvariable=self.t7, width=10)
                id7l.pack(side="left")
                id7e.pack(side="left")
                idf7.pack()
                
                self.t8 = tk.StringVar()
                idf8 = tk.Frame(self.newwindow)
                id8l = tk.Label(idf8, text="ID #8: ",  anchor="w")
                id8e = tk.Entry(idf8, textvariable=self.t8, width=10)
                id8l.pack(side="left")
                id8e.pack(side="left")
                idf8.pack()  

        else:
            #if the format is PK
            if A == '1':
                #if there is an antigen
                # normal IDs (6 tag + 1 biotin) format
                self.varbt = 'p1'
                self.t1 = tk.StringVar() 
                self.t1a = tk.StringVar() 
                idf1 = tk.Frame(self.newwindow)
                id1l = tk.Label(idf1, text="ID-Tag #1: ",  anchor="w")
                id1e = tk.Entry(idf1, textvariable = self.t1, width=10)
                id1la = tk.Label(idf1, text="Concentration: ")
                id1ea = tk.Entry(idf1, textvariable = self.t1a, width=10)
                id1l.pack(side="left")
                id1e.pack(side="left")
                id1la.pack(side="left")
                id1ea.pack(side="left")
                idf1.pack()

                self.t2 = tk.StringVar()
                self.t2a = tk.StringVar()
                idf2 = tk.Frame(self.newwindow)
                id2l = tk.Label(idf2, text="ID-Tag #2: ",  anchor="w")
                id2e = tk.Entry(idf2, textvariable = self.t2, width=10)
                id2la = tk.Label(idf2, text="Concentration: ")
                id2ea = tk.Entry(idf2, textvariable = self.t2a, width=10)
                id2l.pack(side="left")
                id2e.pack(side="left")
                id2la.pack(side="left")
                id2ea.pack(side="left")
                idf2.pack()

                self.t3 = tk.StringVar()
                self.t3a = tk.StringVar()
                idf3 = tk.Frame(self.newwindow)
                id3l = tk.Label(idf3, text="ID-Tag #3: ",  anchor="w")
                id3e = tk.Entry(idf3, textvariable = self.t3, width=10)
                id3la = tk.Label(idf3, text="Concentration: ")
                id3ea = tk.Entry(idf3, textvariable = self.t3a, width=10)
                id3l.pack(side="left")
                id3e.pack(side="left")
                id3la.pack(side="left")
                id3ea.pack(side="left")
                idf3.pack()       
                
                self.t4  = tk.StringVar()
                self.t4a  = tk.StringVar()
                idf4 = tk.Frame(self.newwindow)
                id4l = tk.Label(idf4, text="ID-Tag #4: ",  anchor="w")
                id4e = tk.Entry(idf4, textvariable = self.t4, width=10)
                id4la = tk.Label(idf4, text="Concentration: ")
                id4ea = tk.Entry(idf4, textvariable = self.t4a, width=10)
                id4l.pack(side="left")
                id4e.pack(side="left")
                id4la.pack(side="left")
                id4ea.pack(side="left")
                idf4.pack()

                self.t5 = tk.StringVar()
                self.t5a  = tk.StringVar()
                idf5 = tk.Frame(self.newwindow)
                id5l = tk.Label(idf5, text="ID-Tag #5: ",  anchor="w")
                id5e = tk.Entry(idf5, textvariable=self.t5, width=10)
                id5la = tk.Label(idf5, text="Concentration: ")
                id5ea = tk.Entry(idf5, textvariable = self.t5a, width=10)
                id5l.pack(side="left")
                id5e.pack(side="left")
                id5la.pack(side="left")
                id5ea.pack(side="left")
                idf5.pack()

                self.t6 = tk.StringVar()
                self.t6a = tk.StringVar()
                idf6 = tk.Frame(self.newwindow)
                id6l = tk.Label(idf6, text="ID-Tag #6: ",  anchor="w")
                id6e = tk.Entry(idf6, textvariable=self.t6, width=10)
                id6la = tk.Label(idf6, text="Concentration: ")
                id6ea = tk.Entry(idf6, textvariable = self.t6a, width=10)
                id6l.pack(side="left")
                id6e.pack(side="left")
                id6la.pack(side="left")
                id6ea.pack(side="left")
                idf6.pack()   

                self.t7 = tk.StringVar()
                self.t7a = tk.StringVar()
                idf7 = tk.Frame(self.newwindow)
                id7l = tk.Label(idf7, text="   Biotin:    ",  anchor="w")
                id7e = tk.Entry(idf7, textvariable=self.t7, width=10)
                id7la = tk.Label(idf7, text="Concentration: ")
                id7ea = tk.Entry(idf7, textvariable = self.t7a, width=10)
                id7l.pack(side="left")
                id7e.pack(side="left")
                id7la.pack(side="left")
                id7ea.pack(side="left")
                idf7.pack()
            else:
                #if there isnt an antigen
                self.varbt = 'p2'
                self.t1 = tk.StringVar() 
                self.t1a = tk.StringVar() 
                idf1 = tk.Frame(self.newwindow)
                id1l = tk.Label(idf1, text=" ID-Tag #1: ",  anchor="w")
                id1e = tk.Entry(idf1, textvariable = self.t1, width=10)
                id1la = tk.Label(idf1, text="Concentration: ")
                id1ea = tk.Entry(idf1, textvariable = self.t1a, width=10)
                id1l.pack(side="left")
                id1e.pack(side="left")
                id1la.pack(side="left")
                id1ea.pack(side="left")
                idf1.pack()

                self.t2 = tk.StringVar()
                self.t2a = tk.StringVar()
                idf2 = tk.Frame(self.newwindow)
                id2l = tk.Label(idf2, text=" ID-Tag #2: ",  anchor="w")
                id2e = tk.Entry(idf2, textvariable = self.t2, width=10)
                id2la = tk.Label(idf2, text="Concentration: ")
                id2ea = tk.Entry(idf2, textvariable = self.t2a, width=10)
                id2l.pack(side="left")
                id2e.pack(side="left")
                id2la.pack(side="left")
                id2ea.pack(side="left")
                idf2.pack()

                self.t3 = tk.StringVar()
                self.t3a = tk.StringVar()
                idf3 = tk.Frame(self.newwindow)
                id3l = tk.Label(idf3, text=" ID-Tag #3: ",  anchor="w")
                id3e = tk.Entry(idf3, textvariable = self.t3, width=10)
                id3la = tk.Label(idf3, text="Concentration: ")
                id3ea = tk.Entry(idf3, textvariable = self.t3a, width=10)
                id3l.pack(side="left")
                id3e.pack(side="left")
                id3la.pack(side="left")
                id3ea.pack(side="left")
                idf3.pack()       
                
                self.t4  = tk.StringVar()
                self.t4a  = tk.StringVar()
                idf4 = tk.Frame(self.newwindow)
                id4l = tk.Label(idf4, text=" ID-Tag #4: ",  anchor="w")
                id4e = tk.Entry(idf4, textvariable = self.t4, width=10)
                id4la = tk.Label(idf4, text="Concentration: ")
                id4ea = tk.Entry(idf4, textvariable = self.t4a, width=10)
                id4l.pack(side="left")
                id4e.pack(side="left")
                id4la.pack(side="left")
                id4ea.pack(side="left")
                idf4.pack()

                self.t5 = tk.StringVar()
                self.t5a  = tk.StringVar()
                idf5 = tk.Frame(self.newwindow)
                id5l = tk.Label(idf5, text=" ID-Tag #5: ",  anchor="w")
                id5e = tk.Entry(idf5, textvariable=self.t5, width=10)
                id5la = tk.Label(idf5, text="Concentration: ")
                id5ea = tk.Entry(idf5, textvariable = self.t5a, width=10)
                id5l.pack(side="left")
                id5e.pack(side="left")
                id5la.pack(side="left")
                id5ea.pack(side="left")
                idf5.pack()

                self.t6 = tk.StringVar()
                self.t6a = tk.StringVar()
                idf6 = tk.Frame(self.newwindow)
                id6l = tk.Label(idf6, text=" ID-Tag #6: ",  anchor="w")
                id6e = tk.Entry(idf6, textvariable=self.t6, width=10)
                id6la = tk.Label(idf6, text="Concentration: ")
                id6ea = tk.Entry(idf6, textvariable = self.t6a, width=10)
                id6l.pack(side="left")
                id6e.pack(side="left")
                id6la.pack(side="left")
                id6ea.pack(side="left")
                idf6.pack()   

                self.t7 = tk.StringVar()
                self.t7a = tk.StringVar()
                idf7 = tk.Frame(self.newwindow)
                id7l = tk.Label(idf7, text="  Biotin #1: ",  anchor="w")
                id7e = tk.Entry(idf7, textvariable=self.t7, width=10)
                id7la = tk.Label(idf7, text="Concentration: ")
                id7ea = tk.Entry(idf7, textvariable = self.t7a, width=10)
                id7l.pack(side="left")
                id7e.pack(side="left")
                id7la.pack(side="left")
                id7ea.pack(side="left")
                idf7.pack()
                #########

                self.t8 = tk.StringVar() 
                self.t8a = tk.StringVar() 
                idf8 = tk.Frame(self.newwindow)
                id8l = tk.Label(idf8, text=" ID-Tag #7: ",  anchor="w")
                id8e = tk.Entry(idf8, textvariable = self.t8, width=10)
                id8la = tk.Label(idf8, text="Concentration: ")
                id8ea = tk.Entry(idf8, textvariable = self.t8a, width=10)
                id8l.pack(side="left")
                id8e.pack(side="left")
                id8la.pack(side="left")
                id8ea.pack(side="left")
                idf8.pack()

                self.t9 = tk.StringVar()
                self.t9a = tk.StringVar()
                idf9 = tk.Frame(self.newwindow)
                id9l = tk.Label(idf9, text=" ID-Tag #8: ",  anchor="w")
                id9e = tk.Entry(idf9, textvariable = self.t9, width=10)
                id9la = tk.Label(idf9, text="Concentration: ")
                id9ea = tk.Entry(idf9, textvariable = self.t9a, width=10)
                id9l.pack(side="left")
                id9e.pack(side="left")
                id9la.pack(side="left")
                id9ea.pack(side="left")
                idf9.pack()

                self.t10 = tk.StringVar()
                self.t10a = tk.StringVar()
                idf10 = tk.Frame(self.newwindow)
                id10l = tk.Label(idf10, text=" ID-Tag #9: ",  anchor="w")
                id10e = tk.Entry(idf10, textvariable = self.t10, width=10)
                id10la = tk.Label(idf10, text="Concentration: ")
                id10ea = tk.Entry(idf10, textvariable = self.t10a, width=10)
                id10l.pack(side="left")
                id10e.pack(side="left")
                id10la.pack(side="left")
                id10ea.pack(side="left")
                idf10.pack()       
                
                self.t11  = tk.StringVar()
                self.t11a  = tk.StringVar()
                idf11 = tk.Frame(self.newwindow)
                id11l = tk.Label(idf11, text="ID-Tag #10:",  anchor="w")
                id11e = tk.Entry(idf11, textvariable = self.t11, width=10)
                id11la = tk.Label(idf11, text="Concentration: ")
                id11ea = tk.Entry(idf11, textvariable = self.t11a, width=10)
                id11l.pack(side="left")
                id11e.pack(side="left")
                id11la.pack(side="left")
                id11ea.pack(side="left")
                idf11.pack()

                self.t12 = tk.StringVar()
                self.t12a  = tk.StringVar()
                idf12 = tk.Frame(self.newwindow)
                id12l = tk.Label(idf12, text="ID-Tag #11:",  anchor="w")
                id12e = tk.Entry(idf12, textvariable=self.t12, width=10)
                id12la = tk.Label(idf12, text="Concentration: ")
                id12ea = tk.Entry(idf12, textvariable = self.t12a, width=10)
                id12l.pack(side="left")
                id12e.pack(side="left")
                id12la.pack(side="left")
                id12ea.pack(side="left")
                idf12.pack()

                self.t13 = tk.StringVar()
                self.t13a = tk.StringVar()
                idf13 = tk.Frame(self.newwindow)
                id13l = tk.Label(idf13, text="ID-Tag #12:",  anchor="w")
                id13e = tk.Entry(idf13, textvariable=self.t13, width=10)
                id13la = tk.Label(idf13, text="Concentration: ")
                id13ea = tk.Entry(idf13, textvariable = self.t13a, width=10)
                id13l.pack(side="left")
                id13e.pack(side="left")
                id13la.pack(side="left")
                id13ea.pack(side="left")
                idf13.pack()   

                self.t14 = tk.StringVar()
                self.t14a = tk.StringVar()
                idf14 = tk.Frame(self.newwindow)
                id14l = tk.Label(idf14, text="  Biotin #2: ",  anchor="w")
                id14e = tk.Entry(idf14, textvariable=self.t14, width=10)
                id14la = tk.Label(idf14, text="Concentration: ")
                id14ea = tk.Entry(idf14, textvariable = self.t14a, width=10)
                id14l.pack(side="left")
                id14e.pack(side="left")
                id14la.pack(side="left")
                id14ea.pack(side="left")
                idf14.pack()                                   
        if self.MP and self.varbt[0] == 'p':
            self.mf = tk.Frame(self.newwindow)
            #format help
            self.MPmen_val = tk.StringVar()
            self.MPmen_val.set('Select Format')
            self.MPmen = tk.OptionMenu(self.mf, self.MPmen_val,'Format 1','Format 2','Format 3','Format 4','Format 5','Format 6')
            self.MPmen.grid(row=0,column=1)
            self.fbut = tk.Button(self.mf, text = 'Format Help', command = self.fhelp)        
            self.fbut.grid(row=0,column=2)     

            
            self.mf.pack()
        button_frame = tk.Frame(self.newwindow)
        u_button = tk.Button(button_frame, text="Update", command=self.update)
        #legend_button = tk.Button(button_frame,text="Legend", command=self.legend_f)
        #legend_button.pack(side='left')
        u_button.pack()
        button_frame.pack()
    
    def legend_f(self):
        self.fwindow = tk.Toplevel(self)
        legend_text = tk.Label(self.fwindow, text="this is some text")
        legend_test.pack()


            


    def finish():
        self.destroy()


if __name__ == "__main__":
    app =  Wizard()
    #app.tk.call('tk', 'scaling', '-displayof', '.', 50)
    #app.state('zoomed')
    app.mainloop()


