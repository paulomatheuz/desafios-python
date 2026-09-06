# 10. A lagarta e o balde
# Uma lagarta caiu em um balde de 10 metros. Durante o dia, sobe 3 metros; durante a noite, escorrega 2 metros. O
# movimento comeca pela manha. Quantos dias ela levara para sair do balde?

dias = 0
distancia = 0

while distancia < 10:
    distancia += 3
    dias += 1
    
    if distancia >= 10:
        break
    
    distancia -= 2
    
    print(f"Apos o dia e noite {dias}, a distancia e: {distancia} metros")

print(f"A lagarta levará {dias} dias...")