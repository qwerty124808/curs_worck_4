from src.abstract_api import AbstractApi
from src.vacancy import Vacancy
import requests

class SuperJobAPI(AbstractApi):
    """
        Класс обрабатывает вакансии с hh.ru
    """
    url:str