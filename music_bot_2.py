import time
from selenium import webdriver
import pyautogui as pg 

video = input('Enter the name of the video: ')


def video_player(video):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.youtube.com/')
    pg.moveTo(857, 130, duration=1.25) 
    time.sleep(2)
    pg.click()
    pg.typewrite(video, interval=0.25)
    pg.press('enter')
    time.sleep(2)
    pg.moveTo(369, 283, duration=1.15)
    pg.click()
    time.sleep(900000)


video_player(video)