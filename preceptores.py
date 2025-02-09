import random

class PreceptorAssignment:
    def __init__(self):
        # Lista inicial de preceptores (todos inicialmente disponíveis)
        self.preceptores = {
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
        # Dicionário para controlar o número de alunos por preceptor (inicialmente com todos disponíveis)
        self.alunos_por_preceptor = {nome: 0 for nome, disponivel in self.preceptores.items() if disponivel}
        self.alunos = []  # Lista de alunos a serem processados
        self.lista_preceptores_sorteados = []  # Lista de preceptores sorteados (ordem dos alunos)
        self.grupo_nome = ""  # Nome do grupo de alunos

    def configurar_preceptores(self):
        """Atualiza a disponibilidade dos preceptores conforme os informados pelo usuário."""
        indisponiveis = input("Digite os nomes dos preceptores indisponíveis (separados por vírgula): ").split(', ')
        for nome in indisponiveis:
            if nome in self.preceptores:
                self.preceptores[nome] = False
        # Reconfigura o dicionário para controlar o número de alunos apenas com preceptores disponíveis
        self.alunos_por_preceptor = {nome: 0 for nome, disponivel in self.preceptores.items() if disponivel}

    def ler_alunos(self):
        """Lê o nome do grupo de alunos e a lista de alunos, um por linha."""
        self.grupo_nome = input("Digite o nome do grupo de alunos: ").strip()
        print("Digite os nomes dos alunos, um por linha. Quando terminar, pressione Enter em uma linha vazia:")
        while True:
            linha = input().strip()
            if linha == "":
                break
            self.alunos.append(linha)

    def atribuir_preceptores(self):
        """Atribui um preceptor para cada aluno, priorizando aqueles que ainda não receberam alunos."""
        for aluno in self.alunos:
            # Separa os preceptores disponíveis em dois grupos: sem alunos e com um aluno
            sem_alunos = [nome for nome, count in self.alunos_por_preceptor.items() if count == 0]
            com_um_aluno = [nome for nome, count in self.alunos_por_preceptor.items() if count == 1]
            
            if sem_alunos:
                preceptor_sorteado = random.choice(sem_alunos)
            elif com_um_aluno:
                preceptor_sorteado = random.choice(com_um_aluno)
            else:
                print("Todos os preceptores disponíveis já atingiram o limite máximo de 2 alunos!")
                break
            
            self.alunos_por_preceptor[preceptor_sorteado] += 1
            self.lista_preceptores_sorteados.append(preceptor_sorteado)

    def exibir_resultados(self):
        """Exibe a lista de preceptores sorteados, a distribuição final e a tabela de alunos e preceptores."""
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
        # Remove espaços para construir um nome de arquivo. Ex.: "Grupo A" vira "Grupo_A.txt"
        filename = f"{self.grupo_nome.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Lista de preceptores sorteados:\n")
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
        self.configurar_preceptores()
        self.ler_alunos()
        self.atribuir_preceptores()
        self.exibir_resultados()
        self.salvar_resultados()


if __name__ == "__main__":
    app = PreceptorAssignment()
    app.run() 