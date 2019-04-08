import os, random, sys, time
import argparse
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from termcolor import colored, cprint # Colorama library is also good for terminal color

class Bot:

    def __init__(self, number_of_time_to_scroll=1):
        os.system('color')
        self.choice = 0
        self.base_url = 'https://www.linkedin.com'
        self.number_of_time_to_scroll = number_of_time_to_scroll
        self.check_config()
        self.check_visited_users_file()

    def check_config(self):
        """
           Check if config file exists or not. If not then exit the program
        """
        if not os.path.isfile('config'):
            print(colored('No configuration found', 'red', attrs=['reverse', 'blink']))
            sys.exit()

    def check_visited_users_file(self):
        """
           Check if config file exists or not. If not then create the file
        """
        if not os.path.isfile('visited.txt'):
            file = open('visited.txt', 'wb')
            file.close()

    
    def prompt_choice(self):
        """
           Prompt for browser choice
        """
        print('Choose your browser:')
        print('[1] Chrome')

        self.choice = int(input("Choice: "))

        if self.choice != 1:
            raise ValueError

    def open_browser(self):
        # Open, load and close the 'config' file
        with open('config', 'r') as file:
            configs = [line.strip() for line in file]
        file.close()

        browser = webdriver.Chrome('chromedriver.exe')
        # Sign in
        browser.get(self.base_url + '/uas/login')
        emailElement = browser.find_element_by_id('username')
        emailElement.send_keys(configs[0])
        passElement = browser.find_element_by_id('password')
        passElement.send_keys(configs[1])
        passElement.submit()

        print('Signing in...')
        time.sleep(4)

        soup = BeautifulSoup(browser.page_source, "html5lib")
        if soup.find('div', {'class':'alert error'}):
            print('Error! Please verify your username and password.')
            browser.quit()
        elif browser.title == '403: Forbidden':
            print('LinkedIn is momentarily unavailable. Please wait a moment, then try again.')
            browser.quit()
        else:
            print(colored('Success!\n', 'green'))
        
        browser.get(self.base_url + '/mynetwork/')

        browser = self.infinity_scrolling(browser)

        soup = BeautifulSoup(browser.page_source, "html5lib")
        recommends = soup.findAll('a', {'class': 'mn-discovery-person-card__link--with-coverphoto ember-view'})
        print(len(recommends))
        for recommend in recommends:
            current_url = self.base_url + recommend['href']
            browser.get(current_url)
            print(current_url)
            time.sleep(4)
        
        print(colored('Completed', 'blue'))
    
    def infinity_scrolling(self, driver):
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        n = 1
        while n < self.number_of_time_to_scroll:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            n += 1
        return driver


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visit recommended peoples profile')
    parser.add_argument('-n', '--number', help='Number of time to scroll', type=int)
    args = parser.parse_args()

    bot = Bot(args.number)
    bot.prompt_choice()
    bot.open_browser()