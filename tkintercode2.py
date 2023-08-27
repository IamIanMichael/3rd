from tkinter import *
root = Tk()
logo = PhotoImage(file="/home/pi/Downloads/BDM_logo.gif")

w1 = Label(root, root.title("BDM Publications"), 
image=logo).pack(side="right")
content = """ From its humble beginnings in 2004, 
the BDM brand quickly grew from a single publication 
produced by a team of just two to one of the biggest 
names in global bookazine publishing, for two simple 
reasons. Our passion and commitment to deliver the 
very best product each and every volume. While 
the company has grown with a portfolio of over 250 
publications delivered by our international staff, 
the foundation that it has been built upon remains 
the same, which is why we believe BDM isn’t just 
the first choice it’s the only choice for the smart 
consumer. """
w2 = Label(root, 
 justify=LEFT,
 padx = 10, 
 text=content).pack(side="left")
root.mainloop()
