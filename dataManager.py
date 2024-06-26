import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Data:
    """
        class Data : Classe qui va separer les differentes colonnes
    """
    def __init__(self, temps, acc_x, acc_y, acc_z, absAcc):
        self.temps = temps
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z
        self.absAcc = absAcc

class DataManager:
    """
        Class DataManager : Classe qui permet de recuperer des données d'Un fichier CSV pour mieux les traiter
        param[in] : fichier csv a passer en parametres, String
    """
    def __init__(self, fichier) -> None:
        if isinstance(fichier, str):
            self.fichier = fichier
        else: 
            self.fichier = ""
        #lire le fichier csv
        df = self.__lireFichier()

        #On cree la classe Data
        global data
        data = Data(df["Time (s)"], df["Acceleration x (m/s^2)"], df["Acceleration y (m/s^2)"], df["Acceleration z (m/s^2)"], df["Absolute acceleration (m/s^2)"])

    def __lireFichier(self):
       df = pd.read_csv(self.fichier) 
       return df

    def visualize(self, axe):
        axe.plot(data.temps, data.acc_x)
        #axe.plot.show()
