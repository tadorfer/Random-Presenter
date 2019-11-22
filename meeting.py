try:
    import Tkinter as tk # Python 2.x
except ImportError:
    import tkinter as tk # Python 3.x
from PIL import ImageTk, Image
import math
import random


PRESENTER_NUM = 6
presenters = ['Presenter_'+str(num) for num in range(1, PRESENTER_NUM+1)]
pictures = [presenters[num]+'.jpg' for num in range(len(presenters))]

DELAY, HT, WD, TIME = 12, 700, 800, 6

CP_INCR = [round(random.uniform(0.8,1.6),4) for i in range(len(pictures))]

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))


class Pic():
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def boundaries(self):
        """ Return coords of rectangle surrounding circlular object. """
        return (self.x + self.radius*self.COS_0,   self.y + self.radius*self.SIN_270,
                self.x + self.radius*self.COS_180, self.y + self.radius*self.SIN_90)


def circular_path(x, y, radius, delta_ang, start_ang=0):
    """ Endlessly generate coords of a circular path every delta angle degrees. """
    ang = start_ang % 360
    while True:
        yield x + radius*cos(ang), y + radius*sin(ang)
        ang = (ang+delta_ang) % 360
        
def update_position(canvas, id, pic_obj, path_iter):
    if canvas.coords(id) != []:
        pic_obj.x, pic_obj.y = next(path_iter)
        x0, y0 = canvas.coords(id)
        oldx, oldy = x0 // 2, y0 // 2
        dx, dy = pic_obj.x - oldx, pic_obj.y - oldy
        canvas.move(id, dx, dy)
        canvas.after(DELAY, update_position, canvas, id, pic_obj, path_iter)
    
    
wdw = tk.Tk()
wdw.title('Next Presenter')

x_start, y_start = [], []
for i in range(len(pictures)):
   x_start.append(WD/4+round(random.uniform(-4, 4),2))
   y_start.append(HT/4+round(random.uniform(-4, 4),2))

canvas = tk.Canvas(wdw, bg='#FDF5E6', height=HT, width=WD)
canvas.pack()

logo_tmp = ImageTk.PhotoImage(Image.open('logo.png').resize((150, 95), Image.ANTIALIAS))
canvas.create_image(WD-5, HT-2, image=logo_tmp, anchor='se')
canvas.create_image(5, HT-5, image=logo_tmp, anchor='sw')

canvas.create_text(WD/2, HT/2, text = 'Company\nName\n', 
                   fill='silver', font=('Arial','25', 'bold'), justify='c')


img, img_obj, tmp = [], [], []
orbital_radius = []
for x in range(len(pictures)):
    orbital_radius.append(round(random.uniform(108,122),2))

for i in range(len(pictures)):
    img_obj.append(Pic(WD/4, HT/4, 50))
    tmp.append(ImageTk.PhotoImage(Image.open('/Users/thomasdorfer/Desktop/Projects/RandomPresenter/Photos/'+
                                             pictures[i]).resize((160, 200), Image.ANTIALIAS)))
    img.append(canvas.create_image(100, 200, image=tmp[i]))
        
    path_iter = circular_path(x_start[i], y_start[i], orbital_radius[i], CP_INCR[i])
    next(path_iter)
    wdw.after(DELAY, update_position, canvas, img[i], img_obj[i], path_iter)
    
def accel():
    for j in range(len(pictures)):
        path_iter = circular_path(x_start[j], y_start[j], orbital_radius[j], CP_INCR[j]*5)
        next(path_iter)
        wdw.after(DELAY, update_position, canvas, img[j], img_obj[j], path_iter)

def dec():
    ran = random.randrange(0,len(pictures))
    canvas.create_text(WD/2, HT/6, text='THE NEXT PRESENTER IS', fill='silver',
                       font=('Arial','35'), justify='c')
    canvas.create_text(WD/2, HT/1.25, text='%s' % presenters[ran].replace("_", " "), fill='#8B8B83',
                       font=('Arial','30', 'bold'), justify='c')
    tmp = Image.open('/Users/thomasdorfer/Desktop/Projects/RandomPresenter/Photos/'+
                     pictures[ran]).resize((250, 300), Image.ANTIALIAS)
    tmp1 = ImageTk.PhotoImage(tmp)
    canvas.create_image(WD/2, HT/2, image=tmp1)
    wdw.mainloop()

def ctd():
    global txt
    txt = canvas.create_text(WD/2, HT/2, text=TIME, fill='darkred', 
                             font=('Arial','150', 'bold'))
 
def tick():
    global TIME
    TIME -= 1
    canvas.itemconfigure(txt, text=TIME)
    if TIME == 0:
        None
    else:
        canvas.after(1000, tick)
        
def delete():
    for i in range(len(pictures)):
        canvas.delete(img[i])
        
def delay():
    wdw.after(DELAY, accel)
    wdw.after(5000, dec)
    wdw.after(1, ctd)
    wdw.after(1, tick)
    wdw.after(5000, delete)
    b1.config(state='disabled')
  
b1 = tk.Button(wdw, text='Start', width=10, height=3, command=delay,
              anchor='c', activeforeground='blue', font=('Arial','20'))
b1.pack(side='left', fill='both', expand=True, padx='20', pady='20')

ext = tk.Button(wdw, text='Close', width=10, height=3, command=wdw.destroy,
                anchor='c', activeforeground='blue', font=('Arial','20'))
ext.pack(side='left', fill='both', expand=True, padx='20', pady='20')

wdw.mainloop()