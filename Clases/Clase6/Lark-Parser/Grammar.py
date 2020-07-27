# -*- coding:utf-8 -*-

grammar ="""

    //El axioma inicial
    ?start: exp+

    //Definición de una expresión
    ?exp: var "=" string ";" -> assignvar
        | var "=" arithmeticoperation ";" -> assignvar
        | "print" "("? string ")"? ";" -> printstatement
        | "print" "("? var ")"? ";" -> printvar

    //Definición de operación aritmética
    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation "+" arithmeticoperationatom -> sum
        | arithmeticoperation "-" arithmeticoperationatom -> sub

    //Definición de un átomo de operación aritmética
    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperationatom
        | "(" arithmeticoperation ")"

    //Definición de una cadena
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definición de variable
    ?var: /[a-zA-Z]\w*/

    //Definición de número
    ?number: /\d+(\.\d+)?/

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/
    """