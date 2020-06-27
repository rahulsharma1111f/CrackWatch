from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

chrome_browser = webdriver.Chrome('C:/Users/rs119/PycharmProjects/CrackWatch/chromedriver.exe')


def optimizing():
    chrome_browser.get('https://crackwatch.com/games')
    chrome_browser.maximize_window()
    time.sleep(3)
    poping_window1 = chrome_browser.find_element_by_css_selector('.overlay-button')
    time.sleep(1)
    poping_window1.click()
    poping_window2 = chrome_browser.find_element_by_css_selector('.announcement-close')
    time.sleep(1)
    poping_window2.click()

def profile_login():
    profile = chrome_browser.find_element_by_class_name('nav-profile-icon')
    profile.click()
    username = chrome_browser.find_element_by_xpath("//div[@class='form-group'][1]/input[@class='form-control']")
    username.clear()
    username.send_keys('rks1196965@gmail.com')
    time.sleep(2)
    passw= chrome_browser.find_element_by_css_selector("input[type=password").click()
    time.sleep(2)
    passw.send_keys("password")
    # password = chrome_browser.find_elements_by_xpath("//div[@class='form-group'][2]/input[@class='form-control']")


def credentials_to_seach(Status, Date, Gametype):
    status = Select(
        chrome_browser.find_element_by_xpath("//div[@class='bar-grid']/select[@class='form-control bar-selector'][1]"))
    status.select_by_value(str(Status))

    date = Select(
        chrome_browser.find_element_by_xpath("//div[@class='bar-grid']/select[@class='form-control bar-selector'][2]"))
    date.select_by_value(str(Date))

    gametype = Select(
        chrome_browser.find_element_by_xpath("//div[@class='bar-grid']/select[@class='form-control bar-selector'][3]"))
    gametype.select_by_value(str(Gametype))


def bar_search(key):
    bar = chrome_browser.find_element_by_class_name('bar-search')
    bar.clear()
    bar.send_keys(key)
    time.sleep(1)
    bar.click()


def how_many_games_to_search(num):
    list_of_new_games = {}
    for game_name in range(1, num + 1):
        time.sleep(1)
        name = chrome_browser.find_element_by_xpath(
            f"//div[@class='game-row'][{game_name}]/div[@class='game-row-title']/div[@class='main-title main-title-cap']/a")
        a1 = name.get_attribute('innerHTML')
        release_date = chrome_browser.find_element_by_xpath(
            f"//div[@class='game-row'][{game_name}]/div[@class='game-row-release-date']")
        a2 = release_date.get_attribute('innerHTML')
        crack_date = chrome_browser.find_element_by_xpath(
            f"//div[@class='game-row'][{game_name}]/div[@class='game-row-crack-date']")
        a3 = crack_date.get_attribute('innerHTML')
        Drm = chrome_browser.find_element_by_xpath(
            f"//div[@class='game-row'][{game_name}]/div[@class='game-row-protection']/a")
        a4 = Drm.get_attribute('innerHTML')
        try:
            scene_group = chrome_browser.find_element_by_xpath(
                f"//div[@class='game-row'][{game_name}]/div[@class='game-row-scene-group']/a")
        except:
            scene_group = chrome_browser.find_element_by_xpath(
                f"//div[@class='game-row'][{game_name}]/div[@class='game-row-scene-group']")
        a5 = scene_group.get_attribute('innerHTML')
        best_price = chrome_browser.find_element_by_xpath(
            f"//div[@class='game-row'][{game_name}]/div[@class='game-row-followers']")
        a6 = best_price.get_attribute('innerHTML')

        list_of_new_games.update({game_name: (a1, a2, a3, a4, a5,a6)})
    return list_of_new_games


def show_games(list):
    dataframe = pd.DataFrame(list.values(), index=list.keys(),
                             columns=['Game Name','Release Date', 'Date', 'DRM', 'Scene Group', 'Followers'])
    print(dataframe)

def search_ova(key):
    chrome_browser.get('https://www.ovagames.com/')
    bar = chrome_browser.find_element_by_xpath("//div[@id ='search']/form/input")
    bar.click()
    chrome_browser.close()
    chrome_browser.switch_to.window(chrome_browser.window_handles[0])
    bar = chrome_browser.find_element_by_xpath("//div[@id ='search']/form/input")
    bar.send_keys(key)
    search_box = chrome_browser.find_element_by_xpath("//div[@id='search']/form/input[@class='input']")
    search_box.click()

def search_igg():
    chrome_browser.execute_script("window.open('https://igg-games.g2g.bar/?__cf_chl_jschl_tk__=f93e2d942318a239dfe5a547fa90269c4b52e8db-1592200134-0-AdN0xFaVwj93ktmqj2T9uT7k5Cq-mGIyTbgdEYoIfHRvOF69cEO1seddsxofSB3HZSjnefqz_MIgG6PjNJa5ZjY7HWbRI6dhLKDx91YigNifY6rLtS3HT_zxDmtCfVUyG5zN2b1KMG36uzelwzUKImWqUuZhNEdkHsTCVTwtzEG2-BpfRltud9k0uqA2apBAmyRHyaet4vHcLETeDthHB0M6mCDkle_7xQ7ep-nfUaKzp_1diaHeRbaiYtioA9zU4PF7tZyPZsoMLutv2GZIyXA');")
    time.sleep(0.5)
    chrome_browser.close()

def select_torrents():
    res = requests.get('https://unblocked-pw.github.io/')
    soup = bs(res.text, 'html.parser')
    list_of_torrents = {}
    for data in soup.find_all('div', class_='col-md-3'):
        for a in data.find_all('a'):
            list_of_torrents.update({a.text:a.get('href')})
    return list_of_torrents

def show_torrents(list):
    dataframe = pd.DataFrame(list.values(),index=list.keys(),columns=['Hyperlink'])
    print(dataframe)

def Torent_site():
    chrome_browser.get('https://unblocked-pw.github.io/')


optimizing()

input1 = input(' Search game: Directly (0)'
      ' By setting : Criteria (1) ')
if input1=='Directly' or input1=='0':
    print('Enter game name to search')
    name = input()
    bar_search(name)
    print('Enter no of games to grab')
    num = int(input())
    list_of_games = how_many_games_to_search(num)
    show_games(list_of_games)
    print('Which game to search')
    game_index = int(input())
    for key, value in list_of_games.items():
        if game_index == key:
            search_ova(value[0])
            break
    print(' search on torrents')
    print('yes - 1')
    print('No - 0')
    answer = input()
    if answer == 'Yes' or answer == '1':
        Torent_site()
        torrents_list = select_torrents()
        show_torrents(torrents_list)
    else:
        print('Ok')


elif input1=='Criteria' or input1=='1':
    print('Enter criteria to search:')
    print('All Crack Status - 0   All release date - 0   AAA and Indie - 0')
    print('Carcked - 1            Released - 1           AAA only - 1')
    print('Not Cracked - 2        Upcoming - 2           Indie only - 2')
    a,b,c = input().split()
    credentials_to_seach(a,b,c)
    print('Enter no of games to grab')
    num = int(input())
    list_of_games = how_many_games_to_search(num)
    show_games(list_of_games)
    print('Which game to search')
    game_index = int(input())
    for key,value in list_of_games.items():
        if game_index==key:
            search_ova(value[0])
            break
    print(' search on torrents')
    print('yes - 1')
    print('No - 0')
    answer = input()
    if answer =='Yes' or answer =='1':
        Torent_site()
        torrents_list = select_torrents()
        show_torrents(torrents_list)
    else: print('Ok')


