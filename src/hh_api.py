from src.abstract_api import AbstractApi
from src.vacancy import Vacancy
import requests

class HeadHunterAPI(AbstractApi):
    """
        Класс обрабатывает вакансии с hh.ru
    """
    def __init__(self, url, key_word):
        self.url = url = 'https://api.hh.ru/vacancies'
        self.__params ={
            'page': 0 ,
            'par_page': 100
        }
        self.vacancies = []

    def get_vacancies(self, text):
        """
            возвращает список вакансий
        """
        endpoint = self.url
        response = requests.get(endpoint, params={"text": text})
        vacancy_list = response.json()
        for item in vacancy_list.get("items", []):
            name = item.get('name')
            url = item.get('area')['url']
            requrements = item.get('snippet')['requirement']
            try:
                payment = item.get('salary')["from"]
                # Добавляет созданный экземпляр класса для работы с вакансиями в список вакансий
                vacancys.append(Vacancy(name, url, payment, requrements))
            except:
                continue            
        return(vacancys)

if __name__ == "__main__": 
    test = HeadHunterAPI.get_vacancies("Python")