from textwrap import fill
from tkinter import Frame, Tk, Canvas
from random import choice
from typing_extensions import Self

class Matrix(Frame):
    def __init__(self,master):
        super().__init__(master)


        self.canvas = Canvas(master,bg = 'black')
        self.canvas.place(relx=0, relwidth=1, relheight=1)

        self.velocidad = [i for i in range(0,30,5)]
        self.pos = [i for i in range(-200,200,20)]
        self.letters = []
        self.green = 0
        self.caracteres = [
                    "a","k","u","u","u","N","4"
                    "a","k","u","u","u","N","4"
                    "a","k","u","u","u","N","4"
                    "a","k","u","u","u","N","4"
                    "a","k","u","u","u","N","4"
                    "a","k","u","u","u","N","4"
                    "a","k","u","u","u","N","4"
                    "a","9","r","G","u","N","4"
                    "a","5","u","K","N","g","4"
                    "a","k","u","8","d","4","4"
                    "a","2","9","g","u","N","4"
                    "a","4","j","t","4","n","4"


                  ];  

        self.draw()
        self.update()

    def draw(self):
        for x in range(0,1600,20):
            y = choice(self.pos)
            for j in range(0, choice[180,220,280],20):
                self.obj = self.canvas.create_text(20+x, -200+y+j, text = choice(self.caracteres),fill = '_green2_',font=("Arial", 14))
                self.letters.append(self.obj)


    def update(self):

        for letter in self.letters:
            v = choice(self.velocidad)
            self.green +=5
            color = '#{:02x}{:02x}{:02x}'.format(0,self.green,0)
            self.canvas.itemconfig(letter, fill = color)
            self.canvas.move(letter,0,v)

            y = self.canvas.coords(self.obj)

            if self.green >= 250:
                self.green = 0


            if y[1] >= 800:
                self.draw()

                if y[1]>= 1200:
                    self.letters.clear()
                    self.canvas.delete('all')


        self.canvas.after(80, self.update)


if __name__== '__main__':
             root=Tk()
             root.title('Matrix Animation')
             root.config(bg = 'black')
             root.attributes('-fullscreen', True)
             app = Matrix(root)
             app.mainloop()         