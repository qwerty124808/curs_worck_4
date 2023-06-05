from src.abs_json import AbsJson
from src.modul import *
from operator import itemgetter
from src.vacancy import *
import json

class JsonManager(AbsJson):
    
    def __init__(self, file_name, vacansy_list):
        self.file_name = file_name
        self.vacansy_list = vacansy_list

    def add_vacancy(self):
        """ добавляет вакансию в файл """
        vacansy_list = []
        with open(f"{self.file_name}.json", "w", encoding="utf-8") as file:
            for vacansy in self.vacansy_list:
                if vacansy["sourse"] == "HeadHunter":
                    data = {"sourse": vacansy["sourse"],
                            "id": vacansy["id"],
                            "name": vacansy["name"],
                            "client": vacansy["client"],
                            "url": vacansy["url"],
                            "area": vacansy["area"],
                            "payment":{"payment_min": vacansy['payment_min'],
                                        "payment_max": vacansy['payment_max'],
                                        "currency": vacansy['currency']
                                    }
                            }
                    vacansy_list.append(data)
                else:
                    data = {"sourse": vacansy["sourse"],
                            "id": vacansy["id"],
                            "name": vacansy["name"],
                            "client": vacansy["client"][0],
                            "url": vacansy["url"][0],
                            "area": vacansy["area"][0],
                            "payment":{"payment_min": vacansy['payment_min'][0],
                                        "payment_max": vacansy['payment_max'][0],
                                        "currency": vacansy['currency']
                                    }
                            }
                    vacansy_list.append(data)
            json.dump(vacansy_list, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, demands_list):
        """" удаляет вакансию по условию """
        vacansy_list = []
        counter = 0
        with open(f"{self.file_name}.json", "r",  encoding="utf-8") as file:
            text = json.load(file)
            copy_list = text.copy()
            counter = 0
            while counter < len(copy_list):
                if demands_list[0] not in copy_list[counter]["name"]:
                    del copy_list[counter]
                else:
                    counter += 1
            with open("sorted_vacansy.json", "w", encoding="utf-8") as file:
                for vacansy in copy_list:
                    if vacansy["sourse"] == "HeadHunter":
                        data = {"sourse": vacansy["sourse"],
                                "id": vacansy["id"],
                                "name": vacansy["name"],
                                "client": vacansy["client"],
                                "url": vacansy["url"],
                                "area": vacansy["area"],
                                "payment":{"payment_min": vacansy['payment'].get('payment_min'),
                                            "payment_max": vacansy['payment'].get('payment_max'),
                                            "currency": vacansy['payment'].get('currency')
                                        }
                                }
                        vacansy_list.append(data)
                    else:
                        data = {"sourse": vacansy["sourse"],
                                "id": vacansy["id"],
                                "name": vacansy["name"],
                                "client": vacansy["client"],
                                "url": vacansy["url"],
                                "area": vacansy["area"],
                                "payment":{"payment_min": vacansy['payment'].get('payment_min'),
                                            "payment_max": vacansy['payment'].get('payment_max'),
                                            "currency": vacansy['payment'].get('currency')
                                        }
                                }
                        vacansy_list.append(data)
                json.dump(vacansy_list, file, ensure_ascii=False, indent=4)


    def top_vacansy(self, top_count):
        """ Записывает в файл top_n вакансий по зарплате """
        top_vacansy_list = []
        top_in_write = []
        with open("sorted_vacansy.json", "r", encoding="utf-8") as file:
            text = json.load(file)
            sorted_list = sorted(text, key=lambda e: e["payment"]["payment_max"], reverse=True)
            count = 0
            while count < top_count:
                    top_vacansy_list.append(sorted_list[count])
                    count += 1
        with open(f"top_{count}_vacansy.json", "w", encoding="utf-8") as file:
            for vacansy in top_vacansy_list:
                data = {"sourse": vacansy["sourse"],
                        "id": vacansy["id"],
                        "name": vacansy["name"],
                        "client": vacansy["client"],
                        "url": vacansy["url"],
                        "area": vacansy["area"],
                        "payment":{"payment_min": vacansy["payment"].get('payment_min'),
                                    "payment_max": vacansy["payment"].get('payment_max'),
                                    "currency": vacansy["payment"].get('currency')
                                }
                        }
                top_in_write.append(data)
            json.dump(top_in_write, file, ensure_ascii=False, indent=4)


    def comparison(self, par_id):
        """ Ищет вакансию по id и преобразует её в экземплял класса Vacancy """
        with open("sorted_vacansy.json", "r", encoding="utf-8") as file:
            text = json.load(file)
            for vacansy in text:
                if vacansy["id"] == par_id:
                    result = Vacancy(vacansy["sourse"],
                            vacansy["id"], 
                            vacansy["name"], 
                            vacansy["client"],
                            vacansy["url"],
                            vacansy["area"],
                            vacansy["payment"]["payment_min"], 
                            vacansy["payment"]["payment_max"],
                            vacansy["payment"]["currency"])
            return result

