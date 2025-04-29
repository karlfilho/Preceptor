import random

class PreceptorAssignment:
    def __init__(self):
        self.preceptores = []  # Lista de preceptores
        self.alunos = []  # Lista de alunos
        self.turno = ""  # Turno (Manhã ou Tarde)
        self.alunos_por_preceptor = {}  # Dicionário para controlar o número de alunos por preceptor
        self.lista_preceptores_sorteados = []  # Lista de preceptores sorteados (ordem dos alunos)
        self.grupo_nome = ""  # Nome do grupo de alunos

    def ler_preceptores(self):
        """Lê a lista de preceptores, um por linha."""
        print("Digite os nomes dos preceptores, um por linha. Quando terminar, pressione Enter em uma linha vazia:")
        while True:
            linha = input().strip()
            if linha == "":
                break
            self.preceptores.append(linha)
        self.alunos_por_preceptor = {nome: 0 for nome in self.preceptores}

    def ler_alunos(self):
        """Lê o nome do grupo de alunos, o turno e a lista de alunos."""
        self.grupo_nome = input("Digite o nome do grupo de alunos: ").strip()
        self.turno = input("Digite o turno (Manhã ou Tarde): ").strip()
        print("Digite os nomes dos alunos, um por linha. Quando terminar, pressione Enter em uma linha vazia:")
        while True:
            linha = input().strip()
            if linha == "":
                break
            self.alunos.append(linha)

    def atribuir_preceptores(self):
        """Atribui um preceptor para cada aluno, garantindo que todos os preceptores tenham pelo menos 1 aluno."""
        # Primeiro, garante que cada preceptor tenha pelo menos 1 aluno
        alunos_restantes = self.alunos.copy()
        random.shuffle(alunos_restantes)
        
        # Distribui um aluno para cada preceptor
        for preceptor in self.preceptores:
            if alunos_restantes:
                aluno = alunos_restantes.pop()
                self.alunos_por_preceptor[preceptor] = 1
                self.lista_preceptores_sorteados.append(preceptor)
        
        # Distribui os alunos restantes
        while alunos_restantes:
            aluno = alunos_restantes.pop()
            # Encontra preceptores com menos de 2 alunos
            preceptores_disponiveis = [nome for nome, count in self.alunos_por_preceptor.items() if count < 2]
            if not preceptores_disponiveis:
                print("Todos os preceptores já atingiram o limite máximo de 2 alunos!")
                break
            
            preceptor_sorteado = random.choice(preceptores_disponiveis)
            self.alunos_por_preceptor[preceptor_sorteado] += 1
            self.lista_preceptores_sorteados.append(preceptor_sorteado)

    def exibir_resultados(self):
        """Exibe a lista de preceptores sorteados, a distribuição final e a tabela de alunos e preceptores."""
        print(f"\nTurno: {self.turno}")
        print("\nLista de preceptores sorteados:")
        for preceptor in self.lista_preceptores_sorteados:
            print(preceptor)

        print("\nDistribuição final dos alunos:")
        for preceptor, quantidade in self.alunos_por_preceptor.items():
            print(f"{preceptor}: {quantidade} aluno(s)")

        print("\nTabela de alunos e preceptores:")
        print("{:<50} | {}".format("Aluno", "Preceptor"))
        print("-" * 70)
        for aluno, preceptor in zip(self.alunos, self.lista_preceptores_sorteados):
            print("{:<50} | {}".format(aluno, preceptor))

    def salvar_resultados(self):
        """Salva os resultados em um arquivo de texto cujo nome é o do grupo de alunos."""
        filename = f"{self.grupo_nome.replace(' ', '_')}_{self.turno}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Turno: {self.turno}\n")
            f.write("\nLista de preceptores sorteados:\n")
            for preceptor in self.lista_preceptores_sorteados:
                f.write(preceptor + "\n")
            f.write("\nDistribuição final dos alunos:\n")
            for preceptor, quantidade in self.alunos_por_preceptor.items():
                f.write(f"{preceptor}: {quantidade} aluno(s)\n")
            f.write("\nTabela de alunos e preceptores:\n")
            f.write("{:<50} | {}\n".format("Aluno", "Preceptor"))
            f.write("-" * 70 + "\n")
            for aluno, preceptor in zip(self.alunos, self.lista_preceptores_sorteados):
                f.write("{:<50} | {}\n".format(aluno, preceptor))
        print(f"\nResultados salvos em: {filename}")

    def run(self):
        """Método principal para executar todas as etapas do programa."""
        self.ler_preceptores()
        self.ler_alunos()
        self.atribuir_preceptores()
        self.exibir_resultados()
        self.salvar_resultados()

if __name__ == "__main__":
    app = PreceptorAssignment()
    app.run() 
