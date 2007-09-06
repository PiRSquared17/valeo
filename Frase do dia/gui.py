#coding: utf-8

from Tkinter import *

class EditBoxWindow:
    def pressedOK(self):
        self.text = self.editbox.get('1.0', END)
        if type(self.text) == type(''):
            self.text = unicode(self.text, 'ascii')
        self.myParent.destroy()

    def __init__(self, parent = None):
        if parent == None:
            parent = Tk()
        self.myParent = parent

        self.top_frame = Frame(parent)

        scrollbar = Scrollbar(self.top_frame)
        self.editbox = Text(self.top_frame, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.editbox.yview)

        self.editbox.pack(anchor=CENTER, fill=BOTH)
        self.top_frame.pack(side=TOP)

        self.bottom_left_frame = Frame(parent)
        self.textfield = Entry(self.bottom_left_frame)
        self.textfield.pack(side=LEFT, fill=X, expand=1)

        buttonSearch = Button(self.bottom_left_frame, text='Find', command=self.find)
        buttonSearch.pack(side=RIGHT)
        self.bottom_left_frame.pack(side=LEFT, expand=1)

        self.bottom_right_frame = Frame(parent)

        buttonOK = Button(self.bottom_right_frame, text='OK', command=self.pressedOK)
        buttonCancel = Button(self.bottom_right_frame, text='Cancel', command=parent.destroy)
        buttonOK.pack(side=LEFT, fill=X)
        buttonCancel.pack(side=RIGHT, fill=X)
        self.bottom_right_frame.pack(side=RIGHT, expand=1)

    def edit(self, text, jumpIndex = None, highlight = None):
        self.text = None
        self.editbox.insert(END, text)
        self.editbox.tag_add('all', '1.0', END)
        self.editbox.tag_config('all', wrap = WORD)
        if highlight:
            self.textfield.insert(END, highlight)
            self.find()
        if jumpIndex:
            print jumpIndex
            line = text[:jumpIndex].count('\n') + 1
            column = jumpIndex - (text[:jumpIndex].rfind('\n') + 1)
            self.editbox.see('%d.%d' % (line, column))
        self.myParent.mainloop()
        return self.text 

    def find(self):
        self.editbox.tag_remove('found', '1.0', END)
        s = self.textfield.get()
        if s:
            idx = '1.0'
            while True:
                idx =self.editbox.search(s, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                lastidx = '%s+%dc' % (idx, len(s))
                self.editbox.tag_add('found', idx, lastidx)
                idx = lastidx
            self.editbox.tag_config('found', foreground='red')

class ListBoxWindow:
    def pressedOK(self):
        self.myParent.destroy()

    def __init__(self, parent = None):
        if parent == None:
            parent = Tk()
        self.myParent = parent

        self.listbox = Listbox(parent, selectmode=SINGLE)
        self.listbox.pack(anchor=CENTER, fill=BOTH)
        
        self.bottom_frame = Frame(parent)
        self.bottom_frame.pack(side=BOTTOM)

        buttonOK = Button(self.bottom_frame, text='OK', command=self.pressedOK)
        buttonOK.pack(side=LEFT, fill=X)

    def list(self, list):
        self.list = list
        laenge=len(list)
        maxbreite=0
        for i in range(laenge):
            if len(list[i])+len(str(i))>maxbreite:
                maxbreite=len(list[i])+len(str(i))
            self.listbox.insert(END, str(i)+ ' - '+ list[i])
        #set optimized height & width
        self.listbox.config(height=laenge, width=maxbreite+2)
        return self.list

if __name__=="__main__":
    root = Tk()
    myapp = EditBoxWindow(root)
    myapp.edit(u'Български')
