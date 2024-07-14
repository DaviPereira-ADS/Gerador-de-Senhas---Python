import random
import string


def gerar_senha(tamanho=8, incluir_simbolos=True, incluir_maiusculas=True):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += string.punctuation
    caracteres += string.digits

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


# Configurações do usuário
tamanho = int(input("Digite o tamanho da senha: "))
incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'

# Gerar e exibir a senha
senha = gerar_senha(tamanho, incluir_simbolos, incluir_maiusculas)
print("Senha gerada:", senha)
