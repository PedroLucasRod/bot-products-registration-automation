# Automação de Cadastro de Produtos

Este projeto automatiza o processo de cadastro de produtos em um sistema utilizando dados preenchidos em uma planilha Excel. Ele lê as informações da planilha e, com o auxílio do `pyperclip` e `pyautogui`, cola os valores nos campos correspondentes do sistema através de comandos de clique e teclado.

---

## Tecnologias utilizadas

- Python 3
- openpyxl: para leitura da planilha Excel
- pyperclip: para copiar textos para a área de transferência
- pyautogui: para automação do mouse e teclado
- time (sleep): para pausas entre ações e garantir resposta do sistema

---

## Como funciona

O script realiza os seguintes passos:

1. Abre a planilha Excel (`produtos_ficticios.xlsx`) e acessa a aba "Produtos".
2. Para cada linha (produto) da planilha, lê os atributos como nome, descrição, categoria, código, peso, dimensões, preço, estoque, validade, cor, tamanho, material, fabricante, país de origem, observações, código de barras e localização no armazém.
3. Usa `pyperclip` para copiar o valor de cada campo e `pyautogui` para clicar na posição da tela correspondente ao campo do sistema.
4. Cola o valor usando o atalho `Ctrl+V`.
5. Executa cliques adicionais para selecionar opções específicas (exemplo: diferentes cliques dependendo do tamanho do produto).
6. Após preencher todos os campos da página, clica em botões para finalizar o cadastro, confirmar e preparar para inserir o próximo produto.
7. Repete o processo para todos os produtos da planilha.

---

## Como usar

1. Certifique-se de que o Python 3 está instalado em seu computador.
2. Instale as bibliotecas necessárias:
3. Ajuste a planilha `produtos_ficticios.xlsx` com os dados dos produtos na aba "Produtos".
4. Execute o script Python.
5. Mantenha a janela do sistema de cadastro do produto visível e em posição fixa, para que os cliques do PyAutoGUI funcionem corretamente nas coordenadas definidas.
6. Acompanhe a execução para garantir que todos os dados sejam preenchidos corretamente.

---

## Atenção

- As coordenadas de clique (`pyautogui.click(x, y)`) são fixas e específicas para o sistema usado e resolução da tela. Ajuste conforme necessário.
- É recomendável executar em um ambiente de testes antes de usar em produção.
- O uso do `sleep` ajuda a garantir que o sistema responda antes de prosseguir para a próxima ação.
- Certifique-se que a planilha e o sistema estejam sincronizados para evitar erros de cadastro.

---

## Estrutura dos dados na planilha

| Coluna | Descrição               |
| ------ | ------------------------- |
| A      | Nome do produto           |
| B      | Descrição               |
| C      | Categoria                 |
| D      | Código do produto        |
| E      | Peso                      |
| F      | Dimensões                |
| G      | Preço                    |
| H      | Estoque                   |
| I      | Validade                  |
| J      | Cor                       |
| K      | Tamanho                   |
| L      | Material                  |
| M      | Fabricante                |
| N      | País de origem           |
| O      | Observações             |
| P      | Código de barras         |
| Q      | Localização no armazém |

---

## Processo automatizado pelo script

1. Ler um campo da planilha.
2. Copiar o valor para a área de transferência.
3. Clicar no campo do sistema correspondente.
4. Colar o valor.
5. Repetir para todos os campos.
6. Clicar em "Finalizar cadastro", "Confirmar", "Adicionar mais um".
7. Repetir para todas as linhas da planilha.

---

## Contato

Caso tenha dúvidas ou sugestões, entre em contato.

---

**Este script facilita o cadastro automático de grandes volumes de produtos, economizando tempo e minimizando erros repetitivos de digitação.**
