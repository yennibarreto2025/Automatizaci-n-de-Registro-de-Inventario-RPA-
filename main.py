import pyautogui
import time
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")
pyautogui.press ("enter")
time.sleep (1)
pyautogui.click (x=458, y=907) 
pyautogui.press ("enter")
pyautogui.write (link)
pyautogui.press ("enter")
pyautogui.click (x=1024, y=42)
time.sleep (1)
pyautogui.click (x=606, y=526) 
pyautogui.write ("yennimail@exemplo.com")
pyautogui.press ("enter")
pyautogui.press ("tab")
pyautogui.write ("senha123")
pyautogui.press ("enter")
time.sleep (3)
import pandas
tabela = pandas.read_csv("ejemplochico.csv")
print(tabela)
for linha in tabela.index:
    pyautogui.click (x=549, y=373)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write( str(codigo))
    pyautogui.press ("tab")
    pyautogui.write ( str(tabela.loc[linha, "marca"]))
    pyautogui.press ("tab")
    pyautogui.write ( str(tabela.loc[linha, "tipo"]))
    pyautogui.press ("tab")
    pyautogui.write ( str(tabela.loc[linha, "categoria"]))
    pyautogui.press ("tab")
    pyautogui.write ( str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press ("tab")
    pyautogui.write ( str(tabela.loc[linha, "custo"]))
    pyautogui.press ("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna (obs):
        pyautogui.write ( str(tabela.loc[linha, "obs"]))    
    pyautogui.press ("tab")
    pyautogui.press ("enter")
    pyautogui.scroll (5000)
    time .sleep (1)