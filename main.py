from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    f = open('File.txt', 'w')
    url = 'https://omgtu.ru/ecab/persons/index.php?b=7' # передаем необходимы URL адрес
    page = requests.get(url, verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.find('div', id='pagecontent') # находим  контейнер с нужным классом
    divs=block.findAll('div')
    s = ''
    start = False
    for data in divs: # проходим циклом по содержимому контейнера
        if (start == False):
            start=True
            continue
        if data.find('a'):
            s += data.text  # записываем в переменную содержание тега
            print(s)
            while '\n\n' in s:
                s = s.replace('\n\n', '\n')
    f.write(s)
    f.close()




parse()