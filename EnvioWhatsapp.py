
# -*- coding: UTF-8 -*-

#Importa pacotes                     essenciais
import pyautogui, webbrowser, pandas
from time import sleep 

# Configuração de envio
strMensagem = 'Estou testando meu Robo, Sorry'   # mensagem que irá mandar
strNomeRemetente = 'Patricia M'                  # Nome do remetente no Contato do Whatsapp
intCount = 5                                     # Quantidade vezes que será enviado a mensagem 
i = 0 

# Aviso de inicio de execução
pyautogui.alert ("Começando a automação... não mexa em nada!!")
    
# Abre o Whatsapp
webbrowser.open('https://web.whatsapp.com/')
sleep(10)

# Verifica se está logado no Whatsapp   
blTelaInicialZap = pyautogui.locateOnScreen("QRcodeWhatsapp.png")

# Notifica caso não estejá conectado ao Whatsapp
if blTelaInicialZap:
    print('Conectar o Whatsapp')
    pyautogui.alert ("Conectar o Whatsapp ")

# Executa o Processo de envio 
else:
     print('Whatsapp Conectado!')
     pyautogui.click(x=202, y=211, duration= 0.5)      # Clica na guia de pesquisar contato
     pyautogui.write( strNomeRemetente )               # Escreve o contato do remetente 
     sleep(5)
     pyautogui.click(x=138, y=345, duration= 0.5)      # Clica no contato do remetente

# Executa loop de envio baseado na configuração do inicio
     while i != intCount:
        pyautogui.click(x=579, y=689, duration= 0.3)   # Clica no campo de escrever mensagem 
        pyautogui.write( strMensagem )                 # Escreve Mensagem    
        pyautogui.click(x=1319, y=683, duration= 0.3)  # Clica em envia mensagem 
        
        i += 1

# Aviso de Fim de execução
pyautogui.alert ("Términado a automação...")
