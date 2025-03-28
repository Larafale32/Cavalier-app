from sys import platform
import os


class Utilitaire:
    @staticmethod
    def clear_screen():
        print("Texte", platform)
        if platform == "linux" or platform == "linux2":
            # linux
            os.system("clear")  # linux
        elif platform == "darwin":
            os.environ["TERM"] = "xterm"
            # OS X
            os.system("clear")  # linux
        elif platform == "win32":
            # Windows...
            os.system("cls")
