segundosInput = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundosInput // (3600*24)
horas = (segundosInput % (3600*24)) // 3600
minutos = ((segundosInput % (3600*24)) % 3600) // 60
segundos = ((segundosInput % (3600*24)) % 3600) % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")