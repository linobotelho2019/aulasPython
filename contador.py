segundos_str = int(input("Por favor, entre com o número de segundos que deseja converter: "))
total_segs = int(segundos_str)

dias = total_segs // 86400
segundos_rest = total_segs % 86400

horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600

minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")