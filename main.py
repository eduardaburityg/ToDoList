def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as f:
            return [linha.strip() for linha in f.readlines()]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada!✅ ")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa.")
    else:
        print("📋 Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print(f"Tarefa removida: {removida}")
        else:
            print("❌ Índice inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            remover_tarefa(tarefas)
        elif escolha == "4":
            print("Saindo... até mais")
            break
        else:
            print("❗ Opção inválida.")

if __name__ == "__main__":
    menu()
