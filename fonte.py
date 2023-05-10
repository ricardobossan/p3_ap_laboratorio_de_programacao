print("O programa deve:\n")
print("1. Abrir, ler o conteúdo do arquivo e mostrar:\n\n")
txt = open("texto.txt", "r").read()
print(txt)

print("\n\n2. Contar o número de caracteres:", len(txt) )

userInput = input("\n\n3. Inserir uma userInput e salvar (digitada pelo usuário do programa) no final do arquivo: ")

open("texto.txt", "a").write(userInput) 

print(open("texto.txt", "r").read())

