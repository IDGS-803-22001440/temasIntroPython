from io import open
import os

class Dic:
    espaniol=""
    ingles=""
    texto=""
    idioma=0
    archivo=open("archivo.txt","r")

    def __init__(self):
        self.espaniol
        self.ingles
        self.texto
        self.idioma
        self.archivo


    def Agregar(self,a,b):
        archivo=open("Diccionario.txt","a")
        self.espaniol=a
        self.ingles=b
        texto="{}:{}\n".format(a,b)
        archivo.write(texto)
        print("Las palabras se guardaron correctamente")
        input()
        archivo.close()

    
    def Buscar(self, palabra, idioma):
        with open("Diccionario.txt", "r") as archivo:
            datos = archivo.readlines()
        for linea in datos: 
            texto = linea.strip().split(":")
            if idioma == 1 and texto[0].lower() == palabra.lower():
                print(f"La palabra en inglés es: {texto[1]}")
                input()
            if idioma == 2 and texto[1].lower() == palabra.lower():
                print(f"La palabra en español es: {texto[0]}")
                input()
                break
            elif texto[0].lower() != palabra.lower() and texto[1].lower() == palabra.lower():
                print("Palabra no encontrada.")
                input()
    archivo.close()


def main():
    obj = Dic()
    x=1
    while x <= 1:
        os.system('cls')
        print("Menu de opciones")
        print("1.-Buscar palabra")
        print("2.-Agregar palabra")
        print("3.-Salir del sistema")
        opcion = int(input("Dame una opcion: "))
        if opcion == 1:
            os.system('cls')
            print("Buscar")
            print("1.-Español")
            print("2.-Ingles")
            dic = int(input("Dame una opcion: "))
            if dic == 1:
                txt = input("Escribe la palabra: ")
                num = 1
                obj.Buscar(txt,num)
            if dic == 2:
                txt = input("Escribe la palabra: ")
                num = 2
                obj.Buscar(txt,num)
        if opcion == 2:
            os.system('cls')
            print("Escribe la palabra que vas a agregar")
            pal1 = input("Español: ")
            pal2 = input("Ingles: ")
            obj.Agregar(pal1,pal2)
        if opcion == 3:
            x = 10
            print("Saliste del sistema")

if __name__=="__main__":
    main()