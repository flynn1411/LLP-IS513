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
import sys, re, json

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
        text = re.sub(r"\n", " newLine ", text)
        text = re.sub(r",", " , ", text)
        text = re.sub(r"\s+"," ", text)
        text = re.sub(r"%"," % ", text)
        text = re.sub(r" \"\" "," \"\" ", text)
        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text

        f = open("TokenLibrary/%s/%sTokens.json"%(self.language, self.language),"r")
        tokenLibrary = json.load(f)
        f.close()

        """
            Identifican si actualmente se encuentran en un:
                -Comentario para ignorar el texto entre el mismo
                -Cadena para ignorar su contenido
                -Parametros de fucnión para identificarlos
                -Declaraciónes de Clases o funciones para identificar sus partes
        """
        onLineComment = False
        onMultiLinesComment = False
        onString = False
        onParameter = False
        onFuncDeclaration = False
        onClassDeclaration = False

        #En caso de encontrarse una cadena:
        currentString="";

        functions = {}
        currentFuncName="";
        currentClassName="";

        tokens = re.split(r"\s",text)

        for token in tokens:

            token = ("%s".strip() % token).strip()
            if len(token) > 0:

                #De estar en un comentario, se ignora 
                if onLineComment:
                    if (token == "newLine"):
                        result.append(["Se reconoce un comentario de una línea: ","#%s"%(currentString)])
                        onLineComment = False
                        currentString= ""
                    else:
                        currentString = "%s %s"%(currentString, token)
                
                #De estar en un comentario, se ignora 
                elif onMultiLinesComment:
                    if (token in tokenLibrary) and (tokenLibrary[token] == "Comentarios"):
                        result.append(["Se reconoce un comentario de múltiples líneas: ","%s\"\"\""%(currentString)])
                        onMultiLinesComment = False
                        currentString = ""

                    elif(token == "newLine"):
                        currentString = "%s\n"%(currentString)

                    else:
                        currentString = "%s %s"%(currentString, token)
                
                #De estar en una cadena, se ignora (por los momentos)
                elif onString:
                    if token == "\"\"":
                        result.append(["Se reconoce un literal de cadena: ", "%s"%(currentString)])
                        onString = False
                        currentString = ""

                    elif token=="newLine":
                        currentString = "%s\n"%(currentString)

                    else:
                        currentString = "%s %s"%(currentString, token)

                #Si se encuentra en la decalración de una función
                elif onFuncDeclaration:
                    if onParameter:
                        if re.match(r"^\)$",token):
                            result += [["Se reconoce el final de argumentos de la función '%s': "%(currentFuncName),"%s"%token]]
                            onParameter = False
                        
                        elif re.match(r"^,$",token):
                            result += [["Se reconoce un separador de argumentos de la función '%s': "%(currentFuncName),"%s"%token]]
                        
                        elif re.match(r"^[a-zA-Z][a-zA-Z0-9\_\-]*$",token):
                            result += [["Se reconoce el identificador de argumento para la función '%s': "%(currentFuncName),"%s"%token]]

                    elif re.match(r"^:$",token):
                        onFuncDeclaration = False
                        result.append(["Se reconoce el comienzo de codigo de la función '%s'"%(currentFuncName),"%s"%(token)])
                        currentFuncName = ""

                    elif re.match(r"^[a-zA-Z][a-zA-Z0-9\_\-]*$",token):
                        result += [["Se reconoce el identificador de función: ","%s"%token]]
                        currentFuncName = token
                        functions[token] = "%s"%token

                    elif re.match(r"^\($",token):
                        result += [["Se reconoce el comienzo de argumentos de la función '%s': "%(currentFuncName),"%s"%token]]
                        onParameter = True

                elif onClassDeclaration: pass

                elif re.match(r"^newLine*$",token): pass

                #Si el token se encuentra en la libreria de tokens
                elif token in tokenLibrary:
                    if tokenLibrary[token] == "Comentario":
                        onLineComment = True

                    elif tokenLibrary[token] == "Comentarios":
                        onMultiLinesComment = True
                        currentString = "\"\"\""
                    
                    elif tokenLibrary[token] == "declaración de función":
                        onFuncDeclaration = True
                        result.append(["Se reconoce una %s"%(tokenLibrary[token]),"%s"%(token)])

                    elif tokenLibrary[token] == "declaración de clase":
                        onClassDeclaration = True
                        result.append(["Se reconoce una %s"%(tokenLibrary[token]),"%s"%(token)])

                    else:
                        result.append(["Se reconoce un %s: "%(tokenLibrary[token]), "%s"%(token)])

                
                elif re.match(r"^[a-zA-Z][a-zA-Z0-9\_\-]*$",token):
                    if token in functions:
                        result.append(["Se reconoce el llamado a la función '%s': "%(functions[token]),"%s"%token])

                    #Es un identificador de usuario
                    else:
                        result.append(["Se reconoce el identificador de usuario: ","%s"%token])

                """
                else:
                    quit(
                            "Error: \n\tSe ha encontrado un token desconocido en la línea '%d': '%s'\n\n" %(
                                self.searchTokenLine(token),
                                token
                            )
                        )"""

        self.text = re.sub(r" newLine ", "", self.text)
                
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