agenda = {1: {input("escribe tu nombre: "): input("Escribe tu número telefonico: ")}, 
          2: {input("escribe tu nombre: "): input("Escribe tu número telefonico: ")},
           3: {input("escribe tu nombre: "): input("Escribe tu número telefonico: ")}
           }

print(agenda)

user = input("Escribe el número de alguna persona: ")

print(f"El número {user} le pertenece a {agenda.get(1).get(user,
                                        (agenda.get(2).get(user,
                                        (agenda.get(3).get(user, "no existe")))))}")
"""""""""
Ejercicio 1: Agenda telefónica
medio rebuscado la PTMQLP
"""""""""""