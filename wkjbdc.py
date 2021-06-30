from tkinter import *

root=Tk()
root.title("sales")

root.geometry("700x700")
root.configure(background = 'snow')

Mon = Label(root, bg="white")
Prof = Label(root, bg="white")
MinProf = Label(root, bg="white")
MaxProf = Label(root, bg="white")

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
         "October", "November", "December") 

profits = (302273, 8475385,723407,7242850,87346,276590,3462837,87234629,23468,9749,28762523,2978947734)

Mon["text"]= "Months : " + str(month)
Prof["text"]= "Profits" + str(profits)

def profitfun():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)

    max_profit_month = month[max_profit_index]
    print("The Maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month))
    MaxProf["text"] = "The Maximum profit of " + str(max_profit) + " rupees was recorded in the month of " + str(max_profit_month)

    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)

    min_profit_month = month[min_profit_index]
    print("The Minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month))
    MinProf["text"] = "The Minimum profit of " + str(min_profit) + " rupees was recorded in the month of " + str(min_profit_month)
    
btn = Button(root, text="Show maximum and minimum profits", bg="blue", fg="white", command=profitfun)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

Mon.place(relx=0.5,rely=0.2,anchor=CENTER)
Prof.place(relx=0.5,rely=0.3,anchor=CENTER)
MaxProf.place(relx=0.5,rely=0.5,anchor=CENTER)
MinProf.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
