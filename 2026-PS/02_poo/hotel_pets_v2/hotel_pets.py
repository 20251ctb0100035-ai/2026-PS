# ============================================================
# Aula 20 — Por que POO?
# Atividade: Classe Pet
# Nome do estudante: Anthony Pagani
# ============================================================
# 
# EXPLICAÇÃO: A classe Pet encapsula todas as informações e comportamentos
# relacionados a um animal de estimação no hotel. Cada pet é uma instância
# dessa classe e carrega seus dados (atributos) e ações (métodos) juntos.
# Isso é a essência da POO: agrupar dados e comportamento no mesmo lugar.

class Pet: #Resumo individual
    # cria um novo Pet. Ele inicializa todos os atributos do animal.
    # Todos os parâmetros (nome, especie, etc) são passados no momento da criação.
    def __init__(self, nome, nome_funcionario, especie, idade, peso, nome_dono, telefone_dono, vacinado):

        self.nome = nome
        self.nome_funcionario = nome_funcionario
        self.especie = especie
        self.idade = idade
        self.hospedado = False
        self.peso = peso
        self.nome_dono = nome_dono
        self.telefone_dono = telefone_dono
        self.vacinado = vacinado

    def exibir_dados(self):

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
        
        if self.hospedado == True:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} foi hospedado.")

    def registrar_saida(self):
        
        if self.hospedado:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")
        else:
            print(f"{self.nome} não estava hospedado.")

    def calcular_diaria(self):
       
        if self.idade <= 3:
            return "R$ 50,00"
        elif 4 <= self.idade <= 10:
            return "R$ 60,00"
        else:
            return "R$ 75,00"

    def verificar_vacinacao(self):
   
        if self.vacinado:
            print("Vacinação em dia.")
        else:
            print("Atenção: vacinação pendente.")

    def atualizar_peso(self, novo_peso):

        peso_anterior = self.peso
        self.peso += novo_peso
        print(f"O peso de {self.nome} foi atualizado de {peso_anterior} kg para {self.peso} kg.")

    def emitir_resumo(self):
        print(f"Resumo do {self.nome}: Espécie {self.especie}, Idade {self.idade}, Peso {self.peso}kg")

    def exibir_dados(self):

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
        
        if self.hospedado == True:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} foi hospedado.")

    def registrar_saida(self):
        
        if self.hospedado:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")
        else:
            print(f"{self.nome} não estava hospedado.")

    def emitir_resumo(self):
        print(f"Resumo do {self.nome}: Espécie {self.especie}, Idade {self.idade}, Peso {self.peso}kg")

Lista_dos_pets: list[Pet] = []


# ====================================================
# FUNÇÕES DE VALIDAÇÃO E ENTRADA
# ====================================================
# Essas funções tratam a entrada do usuário de forma robusta.
# Cada uma valida um tipo específico e só retorna quando o usuário
# fornece uma entrada válida. Sem isso, qualquer entrada inválida 
# quebraria o programa.

def ler_texto(prompt):
    # Lê uma string simples, remove espaços antes e depois.
    return input(prompt).strip()


def ler_inteiro(prompt):
    while True:
        valor = input(prompt).strip()
        try:
            return int(valor)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_float(prompt):
    while True:
        valor = input(prompt).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número válido, por exemplo 8.0.")


def ler_booleano(prompt):
    # Função auxiliar para ler respostas sim/não do usuário.
    # Aceita múltiplas variações em português e inglês.
    # Continua pedindo até receber uma resposta válida.
    while True:
        valor = input(prompt).strip().lower()
        if valor in ["s", "sim", "y", "yes"]:
            return True
        if valor in ["n", "não", "nao", "no"]:
            return False
        print("Digite 'S' para sim ou 'N' para não.")



def criar_pet_por_input():
    # Esta função encapsula todo o processo de coleta de dados do usuário.
    # Ela usa as funções de validação acima para garantir dados corretos.
    # Ao final, retorna um novo objeto Pet totalmente inicializado.
    print("\n=== Cadastro de novo pet ===")
    nome = ler_texto("Nome do pet: ")
    nome_funcionario = ler_texto("Nome do funcionário responsável: ")
    especie = ler_texto("Espécie: ")
    idade = ler_inteiro("Idade: ")
    peso = ler_float("Peso (kg): ")
    nome_dono = ler_texto("Nome do dono: ")
    telefone_dono = ler_texto("Telefone do dono: ")
    vacinado = ler_booleano("O pet está vacinado? (s/n): ")
    return Pet(nome, nome_funcionario, especie, idade, peso, nome_dono, telefone_dono, vacinado)


# ====================================================
# FLUXO PRINCIPAL — CADASTRO INTERATIVO
# ====================================================
# Este loop permite que o usuário cadastre múltiplos pets.
# A cada iteração, um novo Pet é criado e adicionado à lista global.
# O loop continua até o usuário responder "não" à pergunta de continuar.

while True:
    novo_pet = criar_pet_por_input()
    Lista_dos_pets.append(novo_pet)
    print(f"Pet {novo_pet.nome} cadastrado com sucesso!\n")
    if not ler_booleano("Deseja cadastrar outro pet? (s/n): "):
        break

# ====================================================
# DEMONSTRAÇÃO DE MÉTODOS
# ====================================================
# Este loop percorre todos os pets cadastrados e executa uma série de métodos
# para demonstrar como a classe Pet funciona. Na prática, esses métodos
# seriam chamados através do menu do programa, não automaticamente.

for pet in Lista_dos_pets:
    pet.exibir_dados()
    pet.registrar_entrada()
    pet.registrar_saida()
    pet.calcular_diaria()
    pet.verificar_vacinacao()
    pet.atualizar_peso(1.5)
    pet.emitir_resumo()

def cadastrar(pet):
    print("\n--- Novo Contato ---")
    Lista_dos_pets: list[Pet] = []
    print("✓Contato cadastrado.")

def listar(pets):
    if not pets:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(pets)} pets) ---")
    for i, c in enumerate(pets, start=1):
        print(f"\n[{i}]")
        c.exibir()


def remover(pets):
    listar(pets)
    if not pets:
        return
    indice = int(input("\nNᵒ do pet a remover: ")) - 1
    if 0 <= indice < len(pets):
        removido = pets.pop(indice)
        print(f"✓ Pet '{removido.nome}' removido.")
    else:
        print("Índice inválido.")
# ====================================================
# PERSISTÊNCIA EM TEXTO (.txt)
# ====================================================
# Vantagem: humano lê. Desvantagem: tudo vira string e a "remontagem"
# do objeto é manual (perdemos tipos, classe, métodos).

def salvar_em_txt(pets, agenda):
    """Grava cada pet em uma linha no arquivo de texto."""
    # Modo "w": abre para escrita e SOBRESCREVE o conteúdo existente.
    # encoding="utf-8": garante que acentos funcionem corretamente.
    # Cada pet é convertido em uma linha com campos separados por "-".
    with open(agenda, "w", encoding="utf-8") as arquivo:
        for c in pets:
            # ".join() concatena os atributos do pet em uma única linha.
            # str() converte números (idade, peso) em texto para poder unir.
            # "1" ou "0" representa os booleanos hospedado e vacinado.
            linha = "-".join([
                c.nome,
                c.nome_funcionario,
                c.especie,
                str(c.idade),
                str(c.peso),
                c.nome_dono,
                c.telefone_dono,
                "1" if c.hospedado else "0",
                "1" if c.vacinado else "0",
            ])
            # Escreve a linha no arquivo e adiciona "\n" (quebra de linha) ao final.
            arquivo.write(linha + "\n")
    print(f"✓ {len(pets)} pet(s) salvo(s) em {agenda}")

def carregar_de_txt(agenda):
    # Esta função é o inverso de salvar_em_txt: reconstrói Pet a partir de texto.
    pets = []
    try:
        with open(agenda, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # strip() remove o \n e espaços nas pontas.
                linha = linha.strip()
                if not linha:
                    # Pula linhas em branco (mais robusto).
                    continue
                # split("-") quebra a linha em pedaços usando o separador.
                # Aqui aparece a fragilidade do .txt: se algum campo tiver
                # ponto-e-vírgula no conteúdo, esse parsing quebra.
                partes = linha.split("-")
                if len(partes) != 9:
                    continue
                # Desempacota as 9 partes em variáveis nomeadas para clareza.
                nome, nome_funcionario, especie, idade, peso, nome_dono, telefone_dono, hospedado_s, vacinado_s = partes
                # Reconstrói um Pet chamando o construtor com tipos corretos.
                # int(idade), float(peso) convertem as strings de volta ao tipo numérico.
                # vacinado_s == "1" compara a string "1" e retorna True ou False.
                pet = Pet(
                    nome,
                    nome_funcionario,
                    especie,
                    int(idade),
                    float(peso),
                    nome_dono,
                    telefone_dono,
                    vacinado_s == "1",
                )
                # Atualiza o atributo hospedado que não foi passado no construtor.
                pet.hospedado = hospedado_s == "1"
                pets.append(pet)
    except FileNotFoundError:
        # Na primeira execução, o arquivo não existe - Começamos vazio.
        # Sem esse tratamento, o programa quebraria ao iniciar.
        print(f"Arquivo {agenda} ainda não existe. Começando vazio.")
    return pets

import pickle #(Rick)

# ====================================================
# PERSISTÊNCIA EM BINÁRIO (pickle)
# ====================================================
# pickle "congela" o objeto inteiro: classe, atributos e tipos
# preservados. Vantagem: zero parsing manual. Desvantagem: só Python lê
# e existe risco de segurança ao abrir .bin de fontes desconhecidos.

def salvar_em_binario(agenda):
    with open(agenda, "wb") as arquivo:
        pickle.dump(Lista_dos_pets, arquivo)
    print(f"✓ {len(Lista_dos_pets)} pet(s) salvo(s) em {agenda}")


def carregar_de_binario(agenda):
    try:
        with open(agenda, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {agenda} ainda não existe. Começando vazio.")
        return []

# Salva em texto automaticamente sempre que o programa terminar.
salvar_em_txt(Lista_dos_pets, "pets.txt")
