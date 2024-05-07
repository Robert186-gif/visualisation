import tkinter as tk
from tkinter import filedialog
from dataManager import *

class Window:
    def __init__(self, root):
        self.root = root
        root.title("Visualisation des données")

        self.plot_types = ['Line Plot', 'Bar Plot']
        self.plot_type_var = tk.StringVar(value=self.plot_types[0])
        plot_menu = tk.OptionMenu(self.root, self.plot_type_var, *self.plot_types, command=self.miseAjour)
        plot_menu.pack(padx=10, pady=10)

        load_btn = tk.Button(self.root, text="Charger Fichier CSV", command=self.chargerFichierCSV)
        load_btn.pack(padx=10, pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(padx=10, pady=10)
        self.dataManager = None

    def chargerFichierCSV(self):
        chemin = filedialog.askopenfilename()
        if chemin:
            self.dataManager = DataManager(chemin)
            print(self.dataManager.fichier)

    def miseAjour(self, event=None):
        plot_type = self.plot_type_var.get()
        self.ax.clear()
        if plot_type == 'Line Plot':
            self.dataManager.visualize(self.ax)

        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    window = Window(root)
    root.mainloop()
