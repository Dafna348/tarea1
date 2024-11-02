num_examenes = int(input("cuantos examenes realizaste? "))
notas = []

for i in range(num_examenes):
  nota = float(input(f"ingrese la nota de los examenes {i + 1}"))
  notas.append(nota)
  
promedio = sum(notas) / num_examenes

print("tu promedio es: ",promedio)

if promedio >=70:
    print("aprovaste")
elif promedio >=60:
  print("puedes hacer ampliacion para aprovar")
else:
  print ("reprovaste")