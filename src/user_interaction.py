from src.modul import *
from src.json_manager import JsonManager
from src.vacancy import * 

def user_interaction():
    """Функция взаимодействия с пользователем"""
    # список ресурсов
    sourses_list = []

    # список вакансий
    vacansy_list = []

    # список nтребований
    demands_list = []

    # список вакансий для сравнения
    comparison_list = []

    # вызов
    hh_vacancies = HeadHunterAPI()
    sj_vacancies = SuperJobAPI()
    search_query = input("Введите поисковый запрос: ")
    count_page = int(input("Введите количество страниц: "))

    hh_vacancies.get_vacancies(search_query, count_page)
    sj_vacancies.get_vacancies(search_query, count_page)
    # экземпляры класса Vacancy с hh
    hh_vacancies_corrected = hh_vacancies.get_convert_exemp_vacancies()
    # экземпляры класса Vacancy с sj
    sj_vacancies_corrected = sj_vacancies.get_convert_exemp_vacancies()
    sourses_list.append(hh_vacancies_corrected)
    sourses_list.append(sj_vacancies_corrected)

    for sours in sourses_list:
        for vacansy in sours:
            vacansy = vacansy.corect_vaccansy()
            vacansy_list.append(vacansy)
    print(f"найдено: {len(vacansy_list)} вакансий\n")
    while True:
        data = JsonManager("vacansys", vacansy_list)
        user_input = int(input("Вывести список вакансий в консоль: 0\n" \
        "Записать в файл: 1\n" \
        "сортировать по требованиям: 2\n" \
        "Top n вакансий по зарплате: 3\n" \
        "Сравнить вакансии: 4\n" \
        "Выйти из программы 5\n" \
        "Введите число из списка: "))

        if user_input == 0:
            print(vacansy_list)
                # AbcApi.printj(vacansy)
        
        elif user_input == 1:
            save_data = data.add_vacancy()
            print("запись окончена")

        elif user_input == 2:
            user_input_2 = input("Хотители вы включить поиск по ключевым запросам ? [Y/N]: ")
            if user_input_2 == "Y":
                copy_list = vacansy_list.copy()
                vacansy_name = input("Введите ключевое слово для выбора вакансий: ")
                demands_list.append(vacansy_name)
                delete_data = data.delete_vacancy(demands_list)

            elif user_input_2 == "N":
                pass

        elif user_input == 3:
            user_input_3 = int(input("сколько вакансий вывести в топ ?: "))
            data.top_vacansy(user_input_3)
        
        elif user_input == 4:
            vacansy_1 = int(input("Введите id первой вакансии: "))
            vacansy_id_1 = data.comparison(vacansy_1)
            comparison_list.append(vacansy_id_1)
            vacansy_2 = int(input("Введите id второй вакансии: "))
            vacansy_id_2 = data.comparison(vacansy_2)
            comparison_list.append(vacansy_id_2)
            while True:
                comparison_user = input("Выберите метод сравнения\n" \
                ">\n" \
                "<\n" \
                ">=\n" \
                "<=\n" \
                "=\n" \
                "Для выхода нажмите Enter\n" \
                "метод сравнения: ")

                if comparison_user == ">":
                    comparison = comparison_list[0].payment_max > comparison_list[1].payment_max
                    if comparison == True:
                        AbcApi.printj(comparison_list[0].corect_vaccansy())
                    else:
                        pass

                elif comparison_user == "<":
                    comparison = comparison_list[0].payment_max < comparison_list[1].payment_max
                    if comparison == True:
                        AbcApi.printj(comparison_list[0].corect_vaccansy())
                    else:
                        pass

                elif comparison_user == ">=":
                    comparison = comparison_list[0].payment_max >= comparison_list[1].payment_max
                    if comparison == True:
                        AbcApi.printj(comparison_list[0].corect_vaccansy())
                    else:
                        pass

                elif comparison_user == "<=":
                    comparison = comparison_list[0].payment_max <= comparison_list[1].payment_max
                    if comparison == True:
                        AbcApi.printj(comparison_list[0].corect_vaccansy())
                    else:
                        pass

                elif comparison_user == "=":
                    comparison = comparison_list[0].payment_max == comparison_list[1].payment_max
                    if comparison == True:
                        AbcApi.printj(comparison_list[0].corect_vaccansy())
                        AbcApi.printj(comparison_list[1].corect_vaccansy())
                    else:
                        pass
                
                elif comparison_user == "":
                    break

        elif user_input == 5:
            break
            
# 80166196 45000 0
# 81481794 80000 1