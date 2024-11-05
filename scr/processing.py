def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращение новых списков словарей по статусу "Выполнено" или "Отменено" """

    filtered_list_of_dict = []
    if state == "CANCELED":
        for dict in list_of_dict:
            if dict.get("state") == "CANCELED":
                filtered_list_of_dict.append(dict)
    else:
        for dict in list_of_dict:
            if dict.get("state") == "EXECUTED":
                filtered_list_of_dict.append(dict)
    return filtered_list_of_dict


def sort_by_date(list_of_dict: list[dict], sorting_method: str = "Убывание") -> list[dict]:
    """Возвращение нового списка словарей, отсортированных по дате"""

    if sorting_method == "Убывание":
        sorted_list_of_dict = sorted(list_of_dict, key=lambda x: x["date"], reverse=True)
    if sorting_method == "Возрастание":
        sorted_list_of_dict = sorted(list_of_dict, key=lambda x: x["date"])
    return sorted_list_of_dict
