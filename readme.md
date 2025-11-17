# Product Registration Automation

This project automates the product registration process in a system using data filled in an Excel spreadsheet. It reads information from the spreadsheet and, with the help of `pyperclip` and `pyautogui`, pastes values into corresponding system fields through click and keyboard commands.

---

## Technologies Used

* Python 3
* openpyxl: for reading Excel spreadsheets
* pyperclip: for copying text to the clipboard
* pyautogui: for mouse and keyboard automation
* time (sleep): for pauses between actions to ensure system response

---

## How It Works

The script performs the following steps:

1. Opens the Excel spreadsheet (`produtos_ficticios.xlsx`) and accesses the "Produtos" sheet.
2. For each row (product) in the spreadsheet, reads attributes such as name, description, category, code, weight, dimensions, price, stock, expiration date, color, size, material, manufacturer, country of origin, notes, barcode, and warehouse location.
3. Uses `pyperclip` to copy each field value and `pyautogui` to click on the screen position corresponding to the system field.
4. Pastes the value using the `Ctrl+V` shortcut.
5. Executes additional clicks to select specific options (example: different clicks depending on product size).
6. After filling all fields on the page, clicks buttons to finalize registration, confirm, and prepare to insert the next product.
7. Repeats the process for all products in the spreadsheet.

---

## How to Use

1. Ensure Python 3 is installed on your computer.
2. Install the required libraries:

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>pip </span><span class="token token">install</span><span> openpyxl pyperclip pyautogui
</span></span><span></span></code></span></div></div></div></pre>

3. Adjust the `produtos_ficticios.xlsx` spreadsheet with product data in the "Produtos" sheet.
4. Run the Python script.
5. Keep the product registration system window visible and in a fixed position so that PyAutoGUI clicks work correctly at the defined coordinates.
6. Monitor the execution to ensure all data is filled correctly.

---

## Important Notes

* Click coordinates (`pyautogui.click(x, y)`) are fixed and specific to the system used and screen resolution. Adjust as needed.
* It is recommended to run in a test environment before using in production.
* Using `sleep` helps ensure the system responds before proceeding to the next action.
* Make sure the spreadsheet and system are synchronized to avoid registration errors.

---

## Data Structure in Spreadsheet

| Column | Description        |
| ------ | ------------------ |
| A      | Product name       |
| B      | Description        |
| C      | Category           |
| D      | Product code       |
| E      | Weight             |
| F      | Dimensions         |
| G      | Price              |
| H      | Stock              |
| I      | Expiration date    |
| J      | Color              |
| K      | Size               |
| L      | Material           |
| M      | Manufacturer       |
| N      | Country of origin  |
| O      | Notes              |
| P      | Barcode            |
| Q      | Warehouse location |

---

## Process Automated by Script

1. Read a field from the spreadsheet.
2. Copy the value to the clipboard.
3. Click on the corresponding system field.
4. Paste the value.
5. Repeat for all fields.
6. Click "Finalize registration", "Confirm", "Add another one".
7. Repeat for all rows in the spreadsheet.

---

## Authorship

Dev Aprender | Jhonatan de Souza

[jhonatan@devaprender.com](mailto:jhonatan@devaprender.com)

Video link: [https://www.youtube.com/watch?v=UtkPIpov6h8&amp;list=PLnNURxKyyLIJ5ftIIYFLNNLyCmBx5uXYM&amp;index=2](https://www.youtube.com/watch?v=UtkPIpov6h8&list=PLnNURxKyyLIJ5ftIIYFLNNLyCmBx5uXYM&index=2)

---

**This script facilitates automatic registration of large volumes of products, saving time and minimizing repetitive typing errors.**


# (PT-BR Version)Automação de Cadastro de Produtos

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

## Autoria

Dev Aprender | Jhonatan de Souza

jhonatan@devaprender.com

link do video: https://www.youtube.com/watch?v=UtkPIpov6h8&list=PLnNURxKyyLIJ5ftIIYFLNNLyCmBx5uXYM&index=2

---

**Este script facilita o cadastro automático de grandes volumes de produtos, economizando tempo e minimizando erros repetitivos de digitação.**
