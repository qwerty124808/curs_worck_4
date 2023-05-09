from src.hh_api import *

def tests():
    test_1 = HeadHunterAPI()
    assert test_1.get_vacancies("python") == 200