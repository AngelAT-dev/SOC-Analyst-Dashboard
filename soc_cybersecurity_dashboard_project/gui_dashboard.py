import tkinter as tk
from tkinter import scrolledtext
from modules.log_analyzer import analyze_logs
from modules.port_scanner import scan_ports

def run_log_analysis():
    result = analyze_logs("sample_logs.txt")
    output.delete(1.0, tk.END)
    output.insert(tk.END, result)

def run_port_scan():
    target = target_entry.get()
    result = scan_ports(target)
    output.delete(1.0, tk.END)
    output.insert(tk.END, result)

app = tk.Tk()
app.title("SOC Cybersecurity Dashboard")
app.geometry("700x500")

title = tk.Label(app, text="SOC Cybersecurity Dashboard", font=("Arial", 18))
title.pack(pady=10)

frame = tk.Frame(app)
frame.pack()

target_label = tk.Label(frame, text="Target IP:")
target_label.grid(row=0, column=0, padx=5)

target_entry = tk.Entry(frame)
target_entry.grid(row=0, column=1, padx=5)

scan_button = tk.Button(frame, text="Run Port Scan", command=run_port_scan)
scan_button.grid(row=0, column=2, padx=5)

log_button = tk.Button(app, text="Analyze Security Logs", command=run_log_analysis)
log_button.pack(pady=10)

output = scrolledtext.ScrolledText(app, width=80, height=20)
output.pack(pady=10)

app.mainloop()