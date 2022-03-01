from tkinter import Tk, Entry, Label
from tkinter import ttk
from typing import Tuple


# from functions import get_tires_w, example
def get_tires_w(lg, wg, w_in, v) -> Tuple[float, float]:
    """
    Calculate the number of tires needed to fit the width of the vehicle
    :param l: length of the vehicle(cm)
    :param wg: width of the vehicle(cm)
    :param w_in: radius of the tire
    :param v: speed of the vehicle(m/s)
    
    :return: angular velocity of the tires(rad/s)
    """

    tanx = math.tan(math.radians(w_in))
    sinx = math.sin(math.radians(w_in))

    R1 = wg / 2 + (lg / tanx)

    tanx2 = lg/(R1+wg/2)

    w_out = math.degrees(math.atan(tanx2))
    sinx2 = math.sin(math.radians(w_out))

    R_in = lg / sinx
    R_out = lg / sinx2

    print("R_in:", R_in, "R_out:", R_out)

    R_in_m = R_in / 1000
    R_out_m = R_out / 1000

    Win = math.degrees(v / R_in_m)
    Wout = math.degrees(v / R_out_m)

    print("Win:", Win, "Wout:", Wout)

    rate_in_out = Win / Wout

    return Win, Wout

gui = Tk()
gui.title("OPENEDIF ::Angular Velocity Calculator for Electronic Differential")
gui.geometry("600x400")

frm = ttk.Frame(gui, padding=40)
frm.grid()


lbl1 = ttk.Label(frm, text="lenght")
lbl1.grid(column=0, row=0)
entry1 = Entry(frm, width=10)
entry1.grid(column=1, row=0)

lbl2 = ttk.Label(frm, text="width")
lbl2.grid(column=0, row=1)
entry2 = Entry(frm, width=10)
entry2.grid(column=1, row=1)

lbl3 = ttk.Label(frm, text="radius of tire in")
lbl3.grid(column=0, row=2)
entry3 = Entry(frm, width=10)
entry3.grid(column=1, row=2)

lbl4 = ttk.Label(frm, text="speed")
lbl4.grid(column=0, row=3)
entry4 = Entry(frm, width=10)
entry4.grid(column=1, row=3)


def calculate():
    lg = float(entry1.get())
    wg = float(entry2.get())
    w = float(entry3.get())
    v = float(entry4.get())
    text = "".join(["Win: ", str(get_tires_w(lg, wg, w, v)[0]), "\n",
                    "Wout: ", str(get_tires_w(lg, wg, w, v)[1])])
    lbl5 = ttk.Label(frm, text=text)
    lbl5.grid(column=1, row=6)

ttk.Button(frm, text="calculate", command=calculate).grid(column=1, row=5)
ttk.Button(frm, text="Quit", command=gui.destroy).grid(column=2, row=5)


if __name__ == '__main__':
    gui.mainloop()
