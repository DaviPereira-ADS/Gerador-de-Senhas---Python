# Gerador de Senhas em Python

Este é um simples gerador de senhas escrito em Python. Ele permite que você escolha o comprimento da senha e especifique se deseja incluir símbolos e letras maiúsculas.

## Funcionalidades

- Escolha o comprimento da senha.
- Opção para incluir símbolos.
- Opção para incluir letras maiúsculas.
- Geração de senhas seguras e aleatórias.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou faça o download dos arquivos.
2. Navegue até o diretório do projeto.
3. Execute o script Python.

```bash
python gerador_senhas.py

Siga as instruções na tela para configurar as preferências da sua senha:

Digite o tamanho da senha.
Escolha se deseja incluir símbolos (s/n).
Escolha se deseja incluir letras maiúsculas (s/n).
 ```
## Exemplo de Uso

```bash
Digite o tamanho da senha: 12
Incluir símbolos? (s/n): s
Incluir letras maiúsculas? (s/n): s
Senha gerada: &aJ8r#Q!d2Lz
```

## Personalização
Você pode personalizar o script ajustando os valores padrão dos parâmetros na função 'gerar_senha':
```bash
def gerar_senha(tamanho=8, incluir_simbolos=True, incluir_maiusculas=True):
    # Função para gerar a senha
```
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
