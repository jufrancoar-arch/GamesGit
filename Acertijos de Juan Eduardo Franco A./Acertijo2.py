import tkinter as tk
from tkinter import messagebox
import random

class JuegoTroll:
    def __init__(self, root):
        self.root = root
        root.title("Juego Troll 😈")
        root.geometry("500x300")
        root.resizable(False, False)

        self.pregunta_label = tk.Label(root, text="¿Quieres jugar un juego sencillo?", font=("Arial", 14))
        self.pregunta_label.pack(pady=20)

        self.btn_si = tk.Button(root, text="Sí", font=("Arial", 12), command=self.respuesta_si)
        self.btn_si.place(x=150, y=150)

        self.btn_no = tk.Button(root, text="No", font=("Arial", 12), command=self.respuesta_no)
        self.btn_no.place(x=250, y=150)

        # Hace que el botón NO huya
        self.btn_no.bind("<Enter>", self.huir)

    def huir(self, event):
        """El botón se mueve aleatoriamente cuando el mouse se acerca."""
        nuevo_x = random.randint(0, 450)
        nuevo_y = random.randint(50, 250)
        self.btn_no.place(x=nuevo_x, y=nuevo_y)

    def respuesta_si(self):
        messagebox.showinfo("Perfecto", "¡Genial! Ahora viene la primera pregunta troll 😈")
        self.pregunta_troll()

    def respuesta_no(self):
        # Nunca debería pasar porque el botón huye
        messagebox.showwarning("¿En serio?", "¿Cómo le diste click si el botón se mueve?")
        self.pregunta_troll()

    def pregunta_troll(self):
        self.pregunta_label.config(text="Pregunta 1:\n¿Cuánto es 2 + 2 * 0?")

        # Eliminar botones anteriores
        self.btn_si.destroy()
        self.btn_no.destroy()

        # Opciones troll
        opciones = [
            ("4", self.incorrecto),
            ("0", self.incorrecto),
            ("22", self.incorrecto),
            ("La respuesta es invisible", self.correcto_troll)
        ]

        y = 140
        for texto, comando in opciones:
            b = tk.Button(self.root, text=texto, font=("Arial", 12), command=comando, width=22)
            b.place(x=120, y=y)
            y += 40

    def incorrecto(self):
        messagebox.showerror("Incorrecto", "JAJAJA. Esa NO era.\nInténtalo hasta que pierdas la paciencia.")

    def correcto_troll(self):
        messagebox.showinfo("Correcto… creo", "Correcto… o tal vez no… quién sabe.\nSiguiente nivel troll.")
        self.final_troll()

    def final_troll(self):
        self.pregunta_label.config(text="Última pregunta:\n¿Eres un robot?")

        # Limpia todos los widgets previos
        for widget in self.root.place_slaves():
            widget.destroy()

        # Los botones hacen lo contrario de lo que dicen
        btn1 = tk.Button(self.root, text="Sí", font=("Arial", 12), command=self.final_no)
        btn2 = tk.Button(self.root, text="No", font=("Arial", 12), command=self.final_si)

        btn1.place(x=150, y=160)
        btn2.place(x=250, y=160)

    def final_si(self):
        messagebox.showinfo("Resultado", "Entonces eres un robot. Lo sabía 🤖.")
        self.root.destroy()

    def final_no(self):
        messagebox.showinfo("Resultado", "Entonces eres humano.\nPero igual perdiste el juego troll 😈.")
        self.root.destroy()


root = tk.Tk()
juego = JuegoTroll(root)
root.mainloop()
