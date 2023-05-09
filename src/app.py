from src.abstract_api import AbstractApi
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy

hh_vacancies =HeadHunterAPI.get_vacancies(key_word)
print(hh_vacancies)
