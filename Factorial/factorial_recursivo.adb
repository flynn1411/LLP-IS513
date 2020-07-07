--Agregado de Librerías
with Ada.Text_IO;
with Ada.Integer_Text_IO;

procedure factorial_recursivo is
    --Renombramiento de Paquetes para un uso mas sencillo
    package Console renames Ada.Text_IO;
    package Int_Console renames Ada.Integer_Text_IO;

    --Declaración de varaibles
    a : Integer :=2;
    b : Integer :=5;
    c : Integer;
    d : Integer :=5;

    --Declaración de Funciones
    function Factorial (n : Integer) return Integer is
    begin
        
        if n <= 1 then
            return 1;
        else
            return (n * Factorial (n - 1));
        end if;
    end Factorial;

--Proceso a seguir
begin

    c := a+b;
    Int_Console.Put(c);
    Console.New_Line;
    Int_Console.Put(Factorial(d));
    Console.New_Line;

end factorial_recursivo;