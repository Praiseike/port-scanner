import tkinter as tk
from core.scanner import Scanner
from tkinter import ttk

class GUI():

	def __init__(self):
		self.window = tk.Tk();
		self.window.geometry('500x400');
		self.window.title("port scanner");

		self.frame = ttk.Frame();

		self.entry_label = ttk.Label(self.frame,text="Enter IP:");
		self.entry_label.grid(column=1,row=0)

		self.string_var = tk.StringVar()
		self.ip_entry = ttk.Entry(self.frame,text="hello",textvariable=self.string_var);
		self.ip_entry.grid(column=2,row=0,padx=30,ipadx=10,columnspan=3,sticky='w');


		self.entry_start_btn = ttk.Button(self.frame,text="start",command=self.start);
		self.entry_start_btn.grid(column=6,row=0)

		self.entry_stop_btn = ttk.Button(self.frame,text="stop",command=self.stop);
		self.entry_stop_btn.grid(column=7,padx=10,row=0)

		self.list_box = tk.Listbox(self.frame)
		self.list_box.grid(column=0,row=1,columnspan=8,ipadx=110,pady=20,ipady=60);


		self.status_label = ttk.Label(self.frame,text="status: idle");
		self.status_label.grid(column=7,row=2);

		self.frame.grid(padx=40,pady=30);

		self.window.mainloop();

	def put_result(self,data):
		port,protocol = data
		self.list_box.insert('end',f"{port} {protocol} is open")

	def start(self):
		self.status_label['text'] = "status: running";
		ip = self.string_var.get()


		scanner = Scanner()
		try:
			scanner.start_scan(ip,self.put_result)
		except Exception as e:
			print(e)
	def stop(self):
		self.status_label['text'] = "status: idle";
		pass
