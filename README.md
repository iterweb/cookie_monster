# Вирус-шутка Cookie Monster
Cookie Monster - программа, которая была написана Крисом Таваресом в далеком 1969 году, как шутка, чтобы раздражать своих сокурсников.<br>
Я же написал эту программу только ради интереса и ностальгии, по тем временам, когда вирусы были добрые :)<br>
***
Cookie Monster is a program that was written by Chris Tavares back in 1969 as a joke to annoy his fellow students.<br>
I wrote this program just for the sake of interest and nostalgia, for those times when viruses were good :)

### Что делает программа | What does this program do
* Определяет язык OS
* Прописывает в автозагрузку ярлык
* Становится скрытой
* Каждый час просит печенье (извлекая лоток CD-ROM)

Секретное слово: ```печенька```
***
* Specifies the OS language
* Writes a shortcut to startup
* Becomes hidden
* Asks for a cookie every hour (ejecting the CD-ROM tray)

Secret word: ```cookie```

### Установка библиотек | Requirements
* [python 3.7+](https://www.python.org/)
* ```pip install -r requirements.txt``` 

### Сборка в .exe | Compile to .exe
```pyinstaller -F -w -i "cookie.ico" cookie.py```
