# -*- coding: utf-8 -*-

class FiniteStateMachine:
    def __init__(self):
        self.currentState = None
        self.currentString = ""
        self.endStates = ["Q3","Q5","Q7","Q10","Q11","Q12"]

        #Conjunto de carácteres de transición entre estados
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        alphabet = [
                        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                        ]
        whitespace = [" ", "\n"]
        assingment = ["="]
        endInstruction = [";"]
        alphanumeric = ["-", "_"]
        alphanumeric += digits + alphabet
        punkt = ["."]
        unknown = [False]

        #Diferentes estados, sus valores son los caracteres de transición, los que no tienen transición
        #son estados de aceptación
        self.states = {
            "Q1": {
                "Q1": whitespace,
                "Q2": alphabet,
                "Q4": digits,
                "Q8": endInstruction,
                "Q9": assingment,
                "Q10": unknown
                },
            "Q2":{
                "Q2": alphanumeric,
                "Q3": whitespace,
                "Q10": unknown
                },
            "Q3":"IDENTIFIER",
            "Q4":{
                "Q4":digits,
                "Q5":whitespace,
                "Q6":punkt,
                "Q10": unknown
                },
            "Q5":"INTEGER",
            "Q6":{
                "Q6":digits,
                "Q7":whitespace,
                "Q10":unknown
                },
            "Q7":"FLOAT",
            "Q8":{
                "Q11":whitespace,
                "Q10":unknown
                },
            "Q9":{
                "Q12":whitespace,
                "Q10":unknown
                },
            "Q10":"UNKNOWN",
            "Q11":"END_STATEMENT",
            "Q12":"ASSIGNMENT_OP"
        }

    #crear una representación de estados

    #Comenzar la máquina
    def runMachine(self):
        print("La máquina de estado finito ha sido comenzada...\n")
        self.changeState("Q1", "")

    #Detener la ejecución de la máquina
    def stopMachine(self):
        self.currentString = ""
        self.changeState("STOP", "")
        print("\nLa máquina de estado finito se detuvo.\n%s\n"%("-"*50))

    def getCurrentState(self):
        return self.currentState

    #método para cambiar de estados, ingresando un estado como parámetro
    def changeState(self, state, char):
        if(state in self.endStates):
            foundToken = self.currentString
            self.stopMachine()
            return([foundToken, self.states[state]])

        elif state == "STOP":
            self.currentState = ""

        else:
            if state == "Q1":
                self.currentString = ""

            self.currentState = state
            print("El caracter ingresado es '%s', por lo que se mueve al estado: %s"%(char ,self.getCurrentState()))
            return None

    #Método que revisa un carácter en el estado actual de la máquina
    def checkChar(self, char):
        checkedTransitions = 0

        for state, transition in self.states[self.getCurrentState()].items():

            #En el caso de que el carácter no sea reconocido, se envía al estado 10, siendo este el estado de error
            if( checkedTransitions == ( len(self.states[self.getCurrentState()]) - 1 ) ):
                self.currentString = "%s%s"%(self.currentString, char)
                return self.changeState("Q10", char)

            else:

                if(char in transition):
                    self.currentString = "%s%s"%(self.currentString, char)
                    return self.changeState(state, char)
                else:
                    checkedTransitions += 1