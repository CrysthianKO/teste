import random 


print(f"""
{"*"*29}
    Adivinhe o Número secreto!
{"*"*29}""")

# While para pegar a dificuldade
while True: 
    dificuldade = int(input("""Selecione uma Dificuldade:
        [*] 1 Easy - 20 Tentativas
        [*] 2 Medium - 10 Tentativas
        [*] 3 Hard - 4 Tentativas
            """))
    if dificuldade == 1:
        total_rodadas = 20
        break
    elif dificuldade == 2:
        total_rodadas = 10
        break
    elif dificuldade == 3:
        total_rodadas = 4
        break
    else:
        print("Selecione uma alternatia correta!")


numero_secreto = random.randrange(101)
total_pontos = 1000


for rodada in range(1, total_rodadas + 1): # Loop até as rodadas acabarem
    
    print(f"""Rodada {rodada} de {total_rodadas}.  
          """)
    chute = int(input(f"Digite um número entre 1 a 100: "))
    
    if (chute <= 0) or (chute > 100): # Caso o número não esteja dentro dos parâmetros
        print(f"\"{chute}\" não é um número válido!")
        continue
    
    if chute == numero_secreto:
        print(f"""Parabéns você acertou o número secreto!
              Você tem {total_pontos} pontos!
              """) 
        break
    else:
        if chute > numero_secreto:
            print(f"O número {chute} está acima do número secreto.")
        else:
            print(f"O número {chute} está abaixo do número secreto.")
        total_pontos = total_pontos - abs(chute - numero_secreto) # Total de pontos menos os pontos perdidos

print("Fim do jogo!")