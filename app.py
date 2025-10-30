import openpyxl
import pyperclip
import pyautogui
from time import sleep

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

for linha in sheet_produtos.iter_rows(min_row=2):
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1134,319, duration=1)
    pyautogui.hotkey('ctrl', 'v')
   
    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1175,450, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1154,600, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1170,700, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    
    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1163,810, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1161,918, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(1164,992, duration=1)
    sleep(1)

    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(1144,345, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    estoque = linha[7].value
    pyperclip.copy(estoque)
    pyautogui.click(1146,455, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    validade = linha[8].value
    pyperclip.copy(validade)
    pyautogui.click(1144,561, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(1144,669, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    tamanho = linha[10].value
    if tamanho == 'Pequeno':
        pyautogui.click(1210,776, duration=1)
        pyautogui.click(1153,820, duration=1)
    elif tamanho == 'Médio':
        pyautogui.click(1210,776, duration=1)
        pyautogui.click(1146,853, duration=1)
    else:
        pyautogui.click(1210,776, duration=1)
        pyautogui.click(1153,887, duration=1)
        


    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(1148,883, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(1148,952, duration=1)
    sleep(1)

    # 
    # 
    # 
    # 
    # 

    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1162,375, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(1195,476, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(1180,611, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_de_barras = linha[15].value
    pyperclip.copy(codigo_de_barras)
    pyautogui.click(1180,755, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.click(1175,865, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(1163,934, duration=1)
    sleep(1)
    # Finalizar cadastro
    pyautogui.click(1649,234, duration=1)
    sleep(1)
    # Adicionado ao banco de dados
    pyautogui.click(1653,232, duration=1)
    sleep(1)
    # Adicionar mais um
    pyautogui.click(1433,651, duration=1)
    sleep(1)



#1-Entrar na planilha
#2-Copiar a informação de um campo e colar no campo correspondente.
#3-Repetir os passos para outros campos até preencher os campos daquela página
#4-Clicar em próxima
#5-Repetir os mesmo passos e ir para a próxima página
#6-Finalizar o cadastro do produto, clicar em concluir.
#7-Clicar no ok.
#8-Clicar no ok novamente.
#9- Clicar em adicionar mais um
#10- Repetir o processo até finalizar a planilha