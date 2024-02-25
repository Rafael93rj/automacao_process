import pyautogui
import time
import webbrowser
from selenium import webdriver

# Usar para acrescentar pausa em todos os intervalos
# pyautogui.PAUSE = 5

# Links
link_query_demand = ("https://console.cloud.google.com/bigquery?_ga=2.190875114.-1761143521.1707918604&_g"
                     "ac=1.124828792.1707919413.Cj0KCQiA5rGuBhCnARIsAN11vgRiPftC5NnJLef4x5HYH3dLm190drQMY"
                     "RhdefUEFNBdBWh5i71dVOsaAkBwEALw_wcB&hl=pt-br&project=utility-grin-414314&ws=!1m4!1m"
                     "3!8m2!1s937096313603!2s98a52f92d25a405d9e9cd4158a4aaa04")
link_query_supply = ("https://console.cloud.google.com/bigquery?_ga=2.190875114.-1761143521.1707918604&_ga"
                     "c=1.124828792.1707919413.Cj0KCQiA5rGuBhCnARIsAN11vgRiPftC5NnJLef4x5HYH3dLm190drQMYRhd"
                     "efUEFNBdBWh5i71dVOsaAkBwEALw_wcB&hl=pt-br&project=utility-grin-414314&ws=!1m4!1m3!8m2"
                     "!1s937096313603!2s582007838a904f9b84f9f2b4ae711ee6")
link_sheets = ("https://docs.google.com/spreadsheets/d/1ro-qhdfEOY3Kl5KiVRTtIVSf06By89D9QWcmQ9zrXLg/edit#g"
               "id=0")

# Etapa query demand
webbrowser.open(link_query_demand)
time.sleep(10)
pyautogui.click(x=736, y=290)
time.sleep(5)
pyautogui.click(x=1503, y=645)
time.sleep(3)
pyautogui.click(x=1291, y=577)

# Etapa sheets
time.sleep(3)
webbrowser.open(link_sheets)
time.sleep(3)
pyautogui.hotkey('ctrl', 'v')

# Etapa query supply
time.sleep(3)
webbrowser.open(link_query_supply)
time.sleep(10)
pyautogui.click(x=736, y=290)
time.sleep(5)
pyautogui.click(x=1503, y=645)
time.sleep(3)
pyautogui.click(x=1291, y=577)

# Etapa sheets 2
time.sleep(3)
webbrowser.open(link_sheets)
time.sleep(3)
pyautogui.click(x=344, y=991)
time.sleep(3)
pyautogui.hotkey('ctrl', 'v')


