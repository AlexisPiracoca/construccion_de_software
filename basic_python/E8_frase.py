# Se cuenta con el siguiente string txt = "Hi, my name is Mary. I like zebras and xylophones." 
# se debe remplazar todas las vocales minusculas por mayusculas y debe desaparecer las letras xy
# Author: Jhon Alexis Piracoca Arcos

string = "Hi, my name is Mary. I like zebras and xylophones."

def processString5(string):
    transTable = string.maketrans("aeiou", "AEIOU", "xyz")
    string = string.translate(transTable)
    print(string)
processString5(string)
