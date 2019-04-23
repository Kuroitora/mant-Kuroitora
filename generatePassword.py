import random
import string

def generatePassword():
    longitud = random.randint(4,16)
    clave = "".join([random.choice( 
                        string.ascii_letters + string.digits + string.punctuation) 
                        for x in range(longitud)]) 
    print("La contraseña generada es "+clave+" con una longitud de "+str(longitud))

generatePassword()
