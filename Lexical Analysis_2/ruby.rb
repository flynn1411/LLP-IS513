/comment

 Comentarios de multiples lineas Ruby
 #hola
uncomment/

=begin
dadfniafniafaffa
Comentarios de múltiples lineas tambieeeen
=end

def factorial n
    if n<2
        return 1
    end
    n*factorial(n-1)
end

n = 5
puts("El factorial en Ruby para '%d' es: %d" % [n, factorial(n)] )