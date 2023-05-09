from abc import ABC, abstractmethod

class AbstractApi(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass