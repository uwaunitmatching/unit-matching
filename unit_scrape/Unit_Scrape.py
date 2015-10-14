#
#basic GUI
#author : Adrian Sasse
#

#build in functions
import re
import sys
import threading
import tkinter as tk
import tkinter.ttk as ttk
import pymysql
import unittest

#my functions
import downTools
import DBconfig
import Test

class Unit_Scrape_tk(tk.Frame):

    recursive = False

    #initialize
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.create_panel()
        


    def create_panel(self):
        panel = tk.Frame(self, name="frame")
        panel.pack(side="top")
        nb = ttk.Notebook(panel, name="notebook")
        nb.pack(side="bottom")
        self.create_units_tab(nb)
        self.create_database_tab(nb)


### UNITS PANEL STARTS HERE

    def create_units_tab(self, nb):
        units_frame = tk.Frame(nb, name="units")
        self.create_url_input_text(units_frame)
        self.create_output_textbox(units_frame)
        self.create_recursive_checkbox(units_frame)
        self.create_test_button(units_frame)
        nb.add(units_frame, text="Units")

    #callbacks
    def get_check_box_callback(self):
        self.recursive = not self.recursive
        if (self.recursive):
            print("Recursive On")
        else:
            print("Recursive Off")
    
    def get_url_callback(self):
       try:
           threading.Thread(target=confirm_input, args=(self.url_in.get(), self.recursive)).start()
       except:
           print ("Error: unable to start thread")

    def run_test_callback(self):
        print("running unit tests!")
        sys.stdout.write = null_redir
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(unittest.makeSuite(Test.Tester))
        sys.stdout.write = redirector

    def clear_log_callback(self):
        self.text_out.delete("1.0",'end')
        
    #input
    def create_url_input_text(self, units_frame):
        label = tk.Label(units_frame, text="Enter Url")
        self.url_in = tk.Entry(units_frame, width=150)
        self.url_in.focus_set()
        self.url_in.delete(0)
        self.url_in.insert(0, "insert url here")
        get_button = tk.Button(units_frame, text="get", width=10, command=self.get_url_callback)
        get_button.pack(side="bottom", anchor="se")
        clear_button = tk.Button(units_frame, text="clear log", width=10, command=self.clear_log_callback)
        clear_button.pack(side="bottom", anchor="se")
        self.url_in.pack(side="bottom")
        label.pack(side="bottom")

    def create_recursive_checkbox(self, units_frame):
        self.check_box = tk.Checkbutton(units_frame, text="Enable Recursive", command=self.get_check_box_callback)
        self.check_box.pack(side="bottom")
        
    #output
    def create_output_textbox(self, units_frame):
        self.text_out = tk.Text(units_frame, width=150)
        self.text_out.pack(side="bottom")

    def create_test_button(self, units_frame):
        test_button = tk.Button(units_frame, text="run tests", width=10, command=self.run_test_callback)
        test_button.pack(anchor="ne")
    
### DATABASE PANEL STARTS HERE

    #callbacks
    def get_db_update_callback(self):
        db.setIP(self.IP_in.get())
        db.setUser(self.user_in.get())
        db.setPW(self.password_in.get())
        db.setDBname(self.database_name_in.get())

    def test_connect_callback(self):
        try:
            database = pymysql.connect(db.getIP(), db.getUser(), db.getPW(), db.getDBname() )
            self.test_label.delete(0, 'end')
            self.test_label.insert(0, "connection OK!")
            database.close()

        except:
            self.test_label.delete(0, 'end')
            self.test_label.insert(0, "connection failed!")

        
    #input/output
    
    def create_database_tab(self, nb):
        db_frame = tk.Frame(nb, name="database")
        #boxes
        self.IP_in = tk.Entry(db_frame, width=100)
        self.IP_in.delete(0)
        self.IP_in.insert(0, db.getIP())
        self.user_in = tk.Entry(db_frame, width=100)
        self.user_in.delete(0)
        self.user_in.insert(0, db.getUser())
        self.password_in = tk.Entry(db_frame, width=100)
        self.password_in.delete(0)
        self.password_in.insert(0, db.getPW())
        self.database_name_in = tk.Entry(db_frame, width=100)
        self.database_name_in.delete(0)
        self.database_name_in.insert(0, db.getDBname())
        #labels
        IP_label = tk.Label(db_frame, text="IP or web address of database")
        user_label = tk.Label(db_frame, text="username")
        password_label = tk.Label(db_frame, text="password")
        database_label = tk.Label(db_frame, text="database name")
        #pack
        IP_label.pack(side="top")
        self.IP_in.pack(side="top")
        user_label.pack(side="top")
        self.user_in.pack(side="top")
        password_label.pack(side="top")
        self.password_in.pack(side="top")
        database_label.pack(side="top")
        self.database_name_in.pack(side="top")
        nb.add(db_frame, text="database")
        #update button
        update_button = tk.Button(db_frame, text="update", width=10, command=self.get_db_update_callback)
        
        #test_button
        self.test_label = tk.Entry(db_frame, width = 30)
        self.test_label.delete(0)
        self.test_label.insert(0, "untested")
        test_button = tk.Button(db_frame, text="test connection", width=15, command=self.test_connect_callback)
        self.test_label.pack(side="bottom")
        test_button.pack(side="bottom")
        update_button.pack(side="bottom")



## RUN PROGRAM

db = DBconfig.DBconfig()
root = tk.Tk()
root.title("Unit Scrape")
app = Unit_Scrape_tk(master=root)

def redirector(inputStr):
    app.text_out.insert(tk.INSERT, inputStr)

def null_redir(inputStr):
    pass

def confirm_input(url, recursive):
    a = re.compile("^http://", re.IGNORECASE)
    if (not a.match(url)):
        print("Input does not appear to be a valid url (hint: http://)")
    elif (recursive):
        dom = url.split('/')[2]
        print("current domain is " + dom)
        downTools.recursiveload(url, dom, db) 
    elif (not recursive):
        dom = url.split('/')[2]
        print("current domain is " + dom)
        downTools.loadUrl(url, 0, db)


sys.stdout.write = redirector
sys.stderr.write = redirector
app.mainloop()



