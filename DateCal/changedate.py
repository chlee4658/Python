from tkinter import *
from datetime import *
from dateutil.relativedelta import relativedelta

root = Tk()
root.title("Change Date")
root.geometry("380x240+700+800")

# def cal_date():
#     entry_date = datetime.strptime(str(entry), "%Y%m%d")
#     print("10일 뒤")
#     print(entry_date + timedelta(days=10))

def day_calc(event):
    btn_button.focus_set()
    date = datetime.strptime(Entry.get(idate), "%Y%m%d").date()
    intv = Entry.get(interval)

    calc_days = date + timedelta(days=int(intv)) # days calculate
    lbl_rst = Label(rst_frame, text=calc_days)
    lbl_rst.grid(row=0, column=1)

    calc_weeks = date + timedelta(weeks=int(intv)) # weeks calculate
    lbl_rst = Label(rst_frame, text=calc_weeks)
    lbl_rst.grid(row=1, column=1)

    calc_months = date + relativedelta(months=int(intv)) # months calculate
    lbl_rst = Label(rst_frame, text=calc_months)
    lbl_rst.grid(row=2, column=1)

# Date frame
date_frame = LabelFrame(root, text="Date")
date_frame.pack(fill="x",padx=5, pady=5, ipady=2)

# Label and input date/interval
lbl_idate = Label(date_frame, text="Input data to change from")
lbl_idate.grid(row=0, column=0, sticky="w")

idate = Entry(date_frame, fg="gray", bg="snow", bd=3, width=10)
idate.grid(row=0, column=1)

lbl_interval = Label(date_frame, text="Input interval")
lbl_interval.grid(row=1, column=0, sticky="w")

interval = Entry(date_frame, fg="grey", bd=3, width=10)
interval.grid(row=1, column=1, sticky="w")

# Button for Calculation
# image = PhotoImage(file="Calculate.png") - change image if get a good image
btn_button = Button(date_frame, text="Calculate",width=9, height=3, pady=2,activeforeground="red",
disabledforeground="dark blue")
btn_button.grid(row=0, column=3, rowspan=2, sticky="W")
# Left click or Enter key event
btn_button.bind('<Return>', day_calc)
btn_button.bind('<Button-1>', day_calc)

# Space Frame
space_frame = Frame(root, height=30, relief="flat")
space_frame.pack()

# Result frame
rst_frame = LabelFrame(root, text="Calculated date")
rst_frame.pack(fill="x", padx=5, pady=5, ipady=2)

lbl_daylater = Label(rst_frame, text="Days Later")
lbl_daylater.grid(row=0, column=0)

lbl_wklater = Label(rst_frame, text="Weeks Later")
lbl_wklater.grid(row=1, column=0)

lbl_mthlater = Label(rst_frame, text="Months Later")
lbl_mthlater.grid(row=2, column=0)







root.mainloop()

