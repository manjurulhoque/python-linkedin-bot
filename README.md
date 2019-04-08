# Linkedin Bot
Increase your popularity on Linkedin.

## Requirements

LInBot was developed under [Pyhton 3](https://www.python.org/downloads).

Before you can run the bot, you will need to install a few Python dependencies.

- [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4), for parsing html: `pip install BeautifulSoup4`
- [Selenium](http://www.seleniumhq.org/), for browser automation: `pip install Selenium`

This bot using chrome [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) as browser.

## Configuration
Before you run the bot, edit the `config` file to add your account login informations (email and password) like below:

```
xxx@gmail.com
123456
```

## Run
Once you have installed the required dependencies and edited the `config` file, you can run the bot.

There are two file named `main.py` and `connection.py`.

`main.py` is finding people from `People you may know` page and visit each one profile.

`connection.py` is finding people from `Connections` page and visit each one profile.

Make sure you are in the correct folder and run the following command: `python main.py -n <any_number>` or `python connection.py -n <any_number>`

Here, **-n** means how many page you want the bot to scroll down and find people.

After choosing your favorite browser (always chrome, anyone can add another browser), the bot will start finding people and then visiting profiles.

## More
**Tips:** You have to `sleep` the bot few seconds after each profile visit otherwise linkedin will detect the bot and restrict your account.

**Feel free to contribute.**
