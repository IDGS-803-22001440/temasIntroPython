from io import open

texto="una line"
archivo=open("archivo.txt","w")
archivo.write(texto)
texto="\n una line nueva"
archivo.write(texto) 
archivo.close()