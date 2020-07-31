PAC II 2020 - LLP 1100 @author swd @date 2020/07/22 @cersion 0.1

# LISP

- Es un lenguaje de propósito general.
- Integers, Ratios, Complex Numbers, Strings, Arrays, Vetors, Hash Tables, Functions, Streams.
- Expresiones-S se definen recursivamente como:
    - Un tipo de dato simple, el cual se llama "átomo".
        - Un átomo corresponde con: número, listas, cádenas de caracteres y símbolos.
    - Una lista de expresiones-S donde una expresión-S podría ser una lista de expresiones-S, que a su vez podría ser listas, y se pueden obtener expresiones anidadas de cualquier nivel de profundidad.

## Expresión-S (S-expression)

- Expresión Simbólica: es una notación de forma texto de texto usada en la representación de estructuras de árbol, está basada en listas anidadas, en donde cada sublista es un subárbol. Las expresiones-S se usan en la familia de lenguajes de programación LISP. Su representación es mediante secuencias de cadenas de carácteres, delimitadas por paréntesis, y separadas por espacios (= 4(+2 2)). En C este ejemplo sería: 4 == 2+2.

## Common Lisp

- https://lisp-lang.org/
- Requiere el uso de notación pre-fija.
- En Consola los ejecutaremos usando un programa SBCL (sudo aptitude).

    - http://www.sbcl.org
    - http://www.sbcl.org/manual

---

- Ejemplos:

#
    ❯ sbcl

    This is SBCL 2.0.1.debian, an implementation of ANSI Common Lisp.
    More information about SBCL is available at <http://www.sbcl.org/>.

    SBCL is free software, provided as is, with absolutely no warranty.
    It is mostly in the public domain; some portions are provided under
    BSD-style licenses.  See the CREDITS and COPYING files in the
    distribution for more information.
    * (+ 1 1)       
    2
    * (exit)
#

---

> (+ 1 2)
> (+ 1 (+ 1 1))
> (* (+ 1 2) (- 3 4)) ;Observe que existen espacios que separan cada elemento de la instrucción
> (+ (+ 3 4) (+ (+ 4 5) 6))
> (+ 3 4 5 6) ;La función de adición puede tomar más de un parámetro.
> (defun funcion (x y) (+ x y 5)) ;La definición de una función.
> (funcion 1 2) ;La ejecución de una función.
> (let ((x 10)) x)
> (let ((y 10)) (- y 10))
> (list 4 5 6)

---

- Para ejecutar un script:

---

> $ sbcl --script program.lisp

---

- Tome en cuenta que:

    - SET que puede establecer el valor de símbolos.
    - SETQ puede establecr el valor de variables.
    - SETF es un macro, posee la capacidad de definir varios elementos: símbolos, variables, elementos de un arreglo, instancias, etc.

- Ejemplo de petición de datos:

---

> (write (+ 1 (read)))

---

- Ejemplo (sin imprimir resultados):

---

> (defvar *unaVariableCualquiera*)
> (setf *unaVariableCualquiera* 42.1)
> (* 2.1 *unaVariableCualquiera*)

---

- Ejemplo de función y ejecución de función:

---

> ; Se define una función
> (defun square (x) (+ x x))
>
> ; Se usa la función
> (write (square 3))

---

- Ejercicio de un programa que imprime mensajes de pantalla y recibe datos de ususario.

- Ejercicio de factorial que imprime el resultado en pantalla de un número fijo.

- Enlaces de apoyo:

    - http://www.cs.cmu-edu/~ggordon/lisp-hints.txt
    - htps://www.tutorialspoint.com/lisp
        - https://www.tutorialspoint.com/lisp/lisp_basic_syntax.htm
        - https://www.tutorialspoint.com/lisp/lisp_variables.htm
        - https://www.tutorialspoint.com/lisp/lisp_strings.htm
        - https://www.tutorialspoint.com/lisp/lisp_input_output.htm

- Por tanto el estudiante debe:

    - Orientar su pensamiento en la creación de programas basados en otros paradigmas conceptuales, donde existe la posibilidad de aplicar múltiples formas gramaticales para resolver operaciones, usando el generador de analizadores léxicos Plex, y el generador de analizadores sintácticos Lark.

## sbcl

- Es el intérprete de Common Lisp que se usará en la clsae
- http://www.sbcl.org/
- http://www.sbcl.org/manual/index.html#Running-from-Shell

## GNU Emacs

- Es parte del conjunto de lenguajes de Lisp
- https://www.gnu.org/software/emacs/