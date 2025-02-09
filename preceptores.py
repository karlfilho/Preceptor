import random

# Lista inicial de preceptores (disponibilidade inicial True para todos)
preceptores = {
    "Karl Richard": True,
    "Luciana Lunardi": True,
    "Javier Rubio": True,
    "Thomas Miklos": True,
    "Gabriel Monteiro": True,
    "Maria Cristina": True,
    "Cássia Pedroga": True,
    "Luiza da Gama": True,
    "Lucas Ribeiro": True,
    "Juliana Aquino": True,
    "Cassiano Andalaft": True,
    "Mariana Marimoto": True,
    "Caroline Panone": True,
    "Elizandra Rosado": True,
    "Natasha Meletti": True,
    "Andrea Menezes": True,
    "Aline Evangelista": True,
    "Alexandre": True,
    "Marta Kempf": True,
}


# Perguntar por preceptores indisponíveis
indisponiveis = input("Digite os nomes dos preceptores indisponíveis (separados por vírgula): ").split(', ')
for nome in indisponiveis:
    if nome in preceptores:
        preceptores[nome] = False

# Dicionário para controlar o número de alunos por preceptor
alunos_por_preceptor = {nome: 0 for nome, disponivel in preceptores.items() if disponivel}

while True:
    aluno = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ").strip()
    
    if aluno.lower() == 'sair':
        break
        
    # Dividir preceptores disponíveis em dois grupos: sem alunos e com um aluno
    sem_alunos = [nome for nome, count in alunos_por_preceptor.items() if count == 0]
    com_um_aluno = [nome for nome, count in alunos_por_preceptor.items() if count == 1]
    
    # Se houver preceptores sem alunos, dar preferência a eles
    if sem_alunos:
        preceptor_sorteado = random.choice(sem_alunos)
    elif com_um_aluno:
        preceptor_sorteado = random.choice(com_um_aluno)
    else:
        print("Todos os preceptores disponíveis já atingiram o limite máximo de 2 alunos!")
        break
        
    alunos_por_preceptor[preceptor_sorteado] += 1
    
    print(f"Aluno {aluno} foi atribuído ao preceptor {preceptor_sorteado}.")
    print("\n\nSituação atual:", alunos_por_preceptor)

# Mostrar distribuição final
print("\nDistribuição final dos alunos:")
for preceptor, quantidade in alunos_por_preceptor.items():
    print(f"{preceptor}: {quantidade} aluno(s)") 