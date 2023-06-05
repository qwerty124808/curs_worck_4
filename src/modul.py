import os
import requests
from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy


class ParsingError(Exception):
    def __str__(self):
        return 'Ошибка получения данных по API.'


class AbcApi(ABC):

    @abstractmethod
    def get_request(self):
        """
        Класс для подключения к API сервиса
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword, page_count):
        """
        Класс для получения информации по вакансиям
        :return:
        """
        pass

    @abstractmethod
    def get_convert_exemp_vacancies(self):
        """
        Класс для конвертировани информации в экземпляры класса Vacancy 
        :return:
        """
        pass

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class HeadHunterAPI(AbcApi):
    def __init__(self):
        self.__header = {
            "User-Agent": "unknown"
        }
        self.__params = {
            "text": None,
            "page": 0,
            "per_page": 100
        }
        self.__vacancies = []

    def get_vacancies(self, keyword, page_count=1):
        self.__params["text"] = keyword
        while self.__params['page'] < page_count:
            print(f"HeadHunter, Парсинг страницы {self.__params['page'] + 1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print('Ошибка получения данных!')
                break
            print(f"Найдено ({len(values)}) вакансий.")
            self.__vacancies.extend(values)
            self.__params['page'] += 1
        

    def get_request(self):
        response = requests.get('https://api.hh.ru/vacancies',
                                headers=self.__header,
                                params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['items']

    def get_convert_exemp_vacancies(self):
        convert_vacancies = []
        for item in self.__vacancies:
            sourse = "HeadHunter"
            id = int(item["id"])
            name = item["name"]
            client = item["employer"]["name"]
            url = item["alternate_url"]
            area = item["area"]["name"]
            if item["salary"] is not None:
                payment_min = item["salary"]["from"]
                payment_max = item["salary"]["to"]
                currency = item["salary"]["currency"]
            convert_vacancies.append(Vacancy(sourse, id, name, client, url, area, payment_min, payment_max, currency))
        return convert_vacancies

    @property
    def vacancies(self):
        return self.__vacancies


class SuperJobAPI(AbcApi):
    def __init__(self):
        self.__header = {'X-Api-App-Id': os.getenv("SUPER_JOB_API_KEY")}
        self.__params = {
            "keyword": None,
            "page": 0,
            "count": 100
        }
        self.__vacancies = []

    def get_vacancies(self, keyword, page_count=1):
        self.__params["keyword"] = keyword
        while self.__params['page'] < page_count:
            print(f"SuperJob, Парсинг страницы {self.__params['page'] + 1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print('Ошибка получения данных!')
                break
            print(f"Найдено ({len(values)}) вакансий.")
            self.__vacancies.extend(values)
            self.__params['page'] += 1

    def get_request(self):
        response = requests.get(f'https://api.superjob.ru/2.0/vacancies/',
                                headers=self.__header,
                                params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['objects']

    def get_convert_exemp_vacancies(self):
        convert_vacancies = []
        for item in self.__vacancies:
            sourse = "SuperJob"
            id =  item["id"]
            name = item["profession"]
            client = item["firm_name"],
            url = item["link"],
            area = item["town"]["title"],
            payment_min = item["payment_from"],
            payment_max = item["payment_to"],
            currency = item["currency"]
            convert_vacancies.append(Vacancy(sourse, id, name, client, url, area, payment_min, payment_max, currency))           
        return convert_vacancies