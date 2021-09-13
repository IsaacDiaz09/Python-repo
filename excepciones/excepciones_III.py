def evaluarEdad(edad):
	if edad<0:
		raise ValueError("No es posible tener una edad negativa...")

	if edad<20:
		return "Eres muy joven"

	elif edad<40:
		return "Eres joven"

	elif edad<65:
		return "Eres maduro"

	elif edad<100:
		return "Eres un adulto mayor"

print(evaluarEdad(55))
