/*
    Basics de Prolog.
    @author swd
    @date 2020/07/30
    @version 0.1
*/

mujer('Gabriela').
mujer('Rosa Maria').

hombre('Alexis').
hombre('David').
hombre('Edgar').

progenitor/a('Alexis','Rosa Maria').
progenitor/a('Gabriela','Rosa Maria').
progenitor/a('Alexis','David').
progenitor/a('Gabriela','David').
progenitor/a('Alexis','Edgar').
progenitor/a('Gabriela','Edgar').

/*
    Para que alguien sea madre, tiene que ser progenitor/a y mujer.
    Para que alguien sea padre, tiene que ser progenitor/a y hombre.
    Para que alguien sea hermano/a, tiene que ser tener los mismos padres.

    Para el estudiante, queda pendiente separar hermano y hermana.
    -----------
    Para que alguien sea hermano, tiene que tener los mismos padres y ser hombre.
    Para que alguien sea hermana, tiene que tener los mismos padres y ser mujer.
*/

madre(X,Y) :-
    progenitor/a(X,Y),
    mujer(X).

padre(X,Y) :-
    progenitor/a(X,Y),
    hombre(X).

hermano/a(X,Y) :-
    madre(A,X),
    padre(B,X),
    madre(C,Y),
    padre(D,Y),
    A == C,
    B == D.