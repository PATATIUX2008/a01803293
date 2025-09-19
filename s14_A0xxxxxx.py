primero : Determinar si es adulto o no
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad (adulto).")
else:
    print("Eres menor de edad (no adulto).")
# segundo : Determinar si es adolescente (13-19 años)
edad = int(input("Ingresa tu edad: "))

if 13 <= edad <= 19:
    print("Eres adolescente.")
else:
    print("No eres adolescente.")
# tercer Determinar la edad a partir del año de nacimiento
edad_nacimiento = int(input("Ingresa tu año de nacimiento: "))
año_actual = 2025
edad = año_actual - edad_nacimiento
print(f"Tienes {edad} años.")
