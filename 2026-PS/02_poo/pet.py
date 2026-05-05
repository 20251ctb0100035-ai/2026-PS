# ============================================================
# Aula 20 — Por que POO?
# Atividade: Classe Pet
# Nome do estudante: Anthony Pagani
# ============================================================

class Pet:
    """
    Esta classe representa um Pet em um sistema simples de hotel para pets.

    Em vez de guardar os dados do pet em um dicionário solto, como fazíamos
    na programação estruturada, agora agrupamos os dados e comportamentos
    dentro de uma classe.
    """

    def __init__(self, nome, nome_funcionario, especie, idade, peso, nome_dono, telefone_dono, vacinado):
        """
        Método construtor.

        Ele é executado automaticamente quando criamos um novo objeto Pet.

        Exemplo:
        pet1 = Pet("Rex", "Cachorro", 5, 10.0, "João", "123456789", True)

        Parâmetros:
        - nome: nome do pet
        - especie: espécie do pet
        - idade: idade do pet
        - peso: peso do pet
        - nome_dono: nome do dono do pet
        - telefone_dono: telefone do dono do pet
        - vacinado: indica se o pet está vacinado
        """

        self.nome = nome
        self.nome_funcionario = nome_funcionario
        self.especie = especie
        self.idade = idade
        self.hospedado = False
        self.peso = peso
        self.nome_dono = nome_dono
        self.telefone_dono = telefone_dono
        self.vacinado = vacinado
        # =====================================================
        # ATIVIDADE 1:
        # Adicione pelo menos 3 novos atributos para o pet.
        #
        # Sugestões:
        # self.raca
        # self.peso
        # self.nome_dono
        # self.telefone_dono
        # self.vacinado
        # self.observacoes
        #
        # Atenção:
        # Se você adicionar novos atributos, também precisará alterar
        # os parâmetros do __init__.
        # =====================================================

    def exibir_dados(self):
        """
        Exibe os dados principais do pet.

        Atualmente, mostra apenas nome, espécie, idade e status de hospedagem.

        ATIVIDADE:
        Modifique este método para exibir também os novos atributos
        que você adicionou no __init__.
        """

        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        if self.hospedado:
            print("Pet está hospedado.") 
        else:
            print("Pet não está hospedado.")

    def registrar_entrada(self):
        """
        Registra a entrada do pet no hotel.

        Se o pet ainda não estiver hospedado, muda o atributo hospedado
        para True.

        ATIVIDADE:
        Melhore este método para verificar se o pet já está hospedado.
        Se já estiver, mostre uma mensagem avisando.
        """
        if self.hospedado == True:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} foi hospedado.")

    def registrar_saida(self):
        """
        Registra a saída do pet do hotel.

        Se o pet estiver hospedado, muda o atributo hospedado para False.

        ATIVIDADE:
        Melhore este método para verificar se o pet realmente está hospedado.
        Se não estiver, mostre uma mensagem avisando.
        """
        if self.hospedado:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")
        else:
            print(f"{self.nome} não estava hospedado.")

    def calcular_diaria(self):
        """
        Calcula o valor da diária do pet.

        ATIVIDADE:
        Implemente uma regra simples para calcular a diária.

        Sugestão:
        - Pet com idade até 3 anos: R$ 50,00
        - Pet com idade entre 4 e 10 anos: R$ 60,00
        - Pet com mais de 10 anos: R$ 75,00

        Este método deve retornar o valor da diária.
        """
        if self.idade <= 3:
            return "R$ 50,00"
        elif 4 <= self.idade <= 10:
            return "R$ 60,00"
        else:
            return "R$ 75,00"

    def verificar_vacinacao(self):
        """
        Verifica se o pet está vacinado.

        ATIVIDADE:
        Para este método funcionar, você precisa criar um atributo
        chamado self.vacinado no __init__.

        Se o pet estiver vacinado, exiba:
        "Vacinação em dia."

        Caso contrário, exiba:
        "Atenção: vacinação pendente."
        """
        if self.vacinado:
            print("Vacinação em dia.")
        else:
            print("Atenção: vacinação pendente.")

    def atualizar_peso(self, novo_peso):
        """
        Atualiza o peso do pet.

        ATIVIDADE:
        Para este método funcionar, você precisa criar um atributo
        chamado self.peso no __init__.

        O método deve receber um novo peso e atualizar o valor antigo.

        Exemplo:
        pet1.atualizar_peso(12.5)
        """

        # Escreva seu código aqui
        peso_anterior = self.peso
        self.peso += novo_peso
        print(f"O peso de {self.nome} foi atualizado de {peso_anterior} kg para {self.peso} kg.")

    def emitir_resumo(self):
        """
        Exibe um resumo geral do pet.

        ATIVIDADE:
        Crie uma mensagem organizada contendo:
        - nome do pet
        - espécie
        - idade
        - nome do dono
        - peso
        - status de vacinação
        - status de hospedagem
        - valor da diária

        Este método deve usar informações dos atributos e também pode
        chamar outros métodos, como calcular_diaria().
        """

        # Escreva seu código aqui
        resumo = f"""--- Resumo do Pet ---
    Nome: {self.nome}
    Nome do funcionário responsável: {self.nome_funcionario}
    Espécie: {self.especie}
    Idade: {self.idade} anos
    Nome do dono: {self.nome_dono}
    telefone do dono: {self.telefone_dono}
    Peso: {self.peso} kg
    Status de vacinação: {'Vacinado' if self.vacinado else 'Pendente'}
    Status de hospedagem: {'Hospedado' if self.hospedado else 'Não hospedado'}
    Valor da diária: {self.calcular_diaria()}
    """
        print(resumo)  
# ============================================================
# TESTES DA CLASSE
# ============================================================
# Depois de completar a classe, crie pelo menos 3 objetos Pet.
#
# Exemplo:
# pet1 = Pet("Rex", "Cachorro", 5)
#
# Atenção:
# Se você adicionou novos parâmetros no __init__, será necessário
# informar esses dados na criação do objeto.
# ============================================================

Lista_dos_pets: list[Pet] = []
pet1 = Pet("Rex", "João", "Cachorro", 5, 22.5, "Maria", "987654321", True)
pet2 = Pet("Mimi", "Maria", "Gato", 2, 4.2, "João", "123456789", True)
pet3 = Pet("Thor", "Carlos", "Cachorro", 11, 18.0, "Ana", "555555555", False)
pet4 = Pet("Luna", "Ana", "Gato", 7, 5.5, "Maria", "999999999", True)
pet5 = Pet("Bella", "João", "Cachorro", 4, 8.0, "Carlos", "777777777", False)
Lista_dos_pets.extend([pet1, pet2, pet3, pet4, pet5])

for pet in Lista_dos_pets:
    pet.exibir_dados()
    pet.registrar_entrada()
    pet.registrar_saida()
    pet.calcular_diaria()
    pet.verificar_vacinacao()
    pet.atualizar_peso(1.5)
    pet.emitir_resumo()
    

# ============================================================
# ATIVIDADE FINAL:
# Crie mais dois pets e teste todos os métodos implementados.
# ============================================================