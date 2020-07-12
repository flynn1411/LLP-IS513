# -*- coding: utf-8 -*-
"""
    !Informal Token Reader (Analizador Léxico Informal Demostrativo)
    *Analizador Léxico para poder leer archivos python o ruby
    *Salida del programa será una tabla de lexemas y sus tokens
    @author Izaguirre
    @date 2020/07/12
    @version 0.2
"""

#sudo -H pip3 install tabulate
from tabulate import tabulate
import sys, re

class InformalTokenParser:

    def __init__(self): pass

    def help(self):

        print("")
        print("*"*80)
        print("*"*80) 
        print("\tInformal Token Reader (Analizador Léxico Informal Demostrativo) ")
        print("""
        \tPermite el reconocimiento de distintos tokes usando expresiones 
        \tregulares para un lenguajes de múltiples instrucciones por línea de código. 
        \tEste programa no posee lexema de palabras especiales, en su lugar, 
        \treconocerá identificadores de usuario, valores númericos, cadenas, 
        \tfin de instrucción y saltos de línea
        """)
        print("*"*80)
        print("*"*80)

    def read(self):
        #python3 lexicalAnalysis.py sample1.lng
        param = sys.argv[1:]

        if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")

        self.fileName = param[0]

        #Analiza que tipo de lenguaje se analizará
        if re.match(r"[A-Za-z0-9\_\-]+\.py", self.fileName):
            self.language = "Python"
        elif re.match(r"[A-Za-z0-9\_\-]+\.rb", self.fileName):
            self.language = "Ruby"

        else:
            self.language = "Unknown"

        #Lee la completidud del programa
        f = open(self.fileName,"r")
        self.text = f.read()
        f.close()

        return self

    def preprocess(self):

        text = self.text
        text = re.sub(r"="," = ", text)
        text = re.sub(r";"," ; ", text)
        text = re.sub(r"\(", " ( ", text)
        text = re.sub(r"\)", " ) ", text)
        text = re.sub(r":", " : ", text)
        text = re.sub(r"\+", " + ", text)
        text = re.sub(r"\-", " - ", text)
        text = re.sub(r"\\", " \ ", text)
        text = re.sub(r"\*", " * ", text)
        text = re.sub(r"\^", " ^ ", text)
        text = re.sub(r"\[", " [ ", text)
        text = re.sub(r"\]", " ] ", text)
        text = re.sub(r"<", " < ", text)
        text = re.sub(r">", " > ", text)
        text = re.sub(r">=", " >= ", text)
        text = re.sub(r"<=", " >= ", text)
        text = re.sub(r"==", " == ", text)
        text = re.sub(r"!=", " != ", text)
        text = re.sub(r"\"\"\"", " \"\"\" ", text)
        text = re.sub(r"#", " # ", text)
        text = re.sub(r"\n", " endl ", text)
        text = re.sub(r",", " , ", text)
        text = re.sub(r"\s+"," ", text)
        text = re.sub(r"%"," % ", text)
        text = re.sub(r" \"\" "," \"\" ", text)
        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text

        """
            Identifican si actualmente se encuentran en un:
                -Comentario para ignorar el texto entre el mismo
                -Cadena para ignorar su contenido
                -Parametros de fucnión para identificarlos
                -Declaraciónes de Clases o funciones para identificar sus partes
        """
        onComment = False
        onString = False
        onParameter = False
        onDeclaration = False

        #En caso de encontrarse una cadena:
        currentString="";

        tokens = re.split(r"\s",text)

        for token in tokens:

            token = ("%s".strip() % token).strip()
            if len(token) > 0:

                if onComment or onString:
                    currentString = "%s\s%s"%(currentString, token)

                elif onParameter:
                    pass

                elif onDeclaration:
                    pass

                else:
                    #Es una cadena
                    if re.match(r"^\"\"$", token):
                        if not onString:
                            onString = True
                        else:
                            result.append(["Se reconoce una cadena de texto: ","%s"%currentString])

                    #Es un identificador de usuario
                    elif re.match(r"^[a-zA-Z][a-zA-Z0-9\_\-]*$",token):
                        result += [["Se reconoce el identificador de usuario: ","%s"%token]]

                    #Es un operador de asignación
                    elif re.match(r"^=$",token):
                        result += [["Se reconoce el operador de asignación: ","%s"%token]]

                    #Es un número flotante
                    elif re.match(r"^\d+\.\d+$",token):
                        result += [["Se reconoce el número flotante: ","%s"%token]]

                    #Es un número entero
                    elif re.match(r"^\d+$",token):
                        result += [["Se reconoce el número entero: ","%s"%token]]

                    #Es un token desconcido
                    else:
                        quit(
                            "Error: \n\tSe ha encontrado un token desconocido en la línea '%d': '%s'\n\n" %(
                                self.searchTokenLine(token),
                                token
                            )
                        )
        return result


    def searchTokenLine(self, token):

        errorLine = 0

        f = open(self.fileName, "r")

        for line in f:
            #print("\t\tDebug: %s" % line)
            errorLine += 1
            
            if re.match(r"^.*%s.*$" % self.prevent(token), line):
                break

        f.close()

        return errorLine

    def prevent(self, token):

        if re.match(r"[\+\*\.\(\)\{\}\[\]]+",token):
            return "\\%s" % token
        return token



parser = (InformalTokenParser()).read().preprocess()
parser.help()

print("Programa encontrado:")
print ("\t%s\n" % parser.text)

lexicalAnalysis = parser.lexicalAnalysis()
print("El análisis léxico del software es:")
print(tabulate(lexicalAnalysis))