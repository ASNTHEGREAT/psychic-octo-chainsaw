import time
import pyautogui as pg

screenwidth, screenheight = pg.size()

currentMouseX, currentMouseY = pg.position()

# pg.alert('This is the message to display.')
name = input('Enter the name of the song: ')
# print(pg.size())
time.sleep(1)
# print(pg.position())
pg.moveTo(594, 761, duration=1.25) 
pg.click()
time.sleep(0.5)
pg.hotkey('ctrl', 't') # Press the Ctrl-t hotkey combination.
pg.moveTo(867, 49, duration=1.25)
pg.click()
time.sleep(1)
pg.typewrite('https://www.youtube.com/', interval=0.1)
pg.press('enter')
pg.moveTo(867, 115, duration=1.25)
time.sleep(1.25)
pg.click()
pg.typewrite(name, interval=0.1)
pg.press('enter')
time.sleep(2)
pg.moveTo(369, 283, duration=1.15)
pg.click()





# print(pg.onScreen(594, 761))