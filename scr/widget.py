from scr import masks


def mask_account_card(card_account_number: str) -> str:
    """Функция различает номер счета и номер карты, возвращает частично замаскированный номер"""

    if type(card_account_number) != str:
        raise TypeError("Неверный тип данных")

    type_of_number = ""
    number = ""
    for i in card_account_number:
        if i.isdigit():
            number += i

    if (
        "Счет" not in card_account_number
        and "Счёт" not in card_account_number
        and "Maestro" not in card_account_number
        and "MasterCard" not in card_account_number
        and "Visa" not in card_account_number
    ):
        return "К сожалению, не удалось распознать вашу карту или счет"

    elif "Счет" in card_account_number or "Счёт" in card_account_number:
        type_of_number = "Счет"
        number_with_mask = masks.get_mask_account(number)

    else:
        if "Maestro" in card_account_number:
            type_of_number = "Maestro"
        elif "MasterCard" in card_account_number:
            type_of_number = "MasterCard"
        elif "Visa Classic" in card_account_number:
            type_of_number = "Visa Classic"
        elif "Visa Platinum" in card_account_number:
            type_of_number = "Visa Platinum"
        elif "Visa Gold" in card_account_number:
            type_of_number = "Visa Gold"
        number_with_mask = masks.get_mask_card_number(number)

    masked_card_account_number = type_of_number + " " + number_with_mask
    return masked_card_account_number


def get_date(date_and_time: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""

    if type(date_and_time) != str:
        raise TypeError("Неверный тип данных")
    if int(date_and_time[8:10]) > 31:
        raise ValueError("Указана неверная дата")
    if int(date_and_time[5:7]) > 12:
        raise ValueError("Указана неверная дата")
    if not date_and_time[0].isdigit() or not date_and_time[1].isdigit() or not date_and_time[2].isdigit() or not date_and_time[3].isdigit() or not date_and_time[5].isdigit() or not date_and_time[6].isdigit() or not date_and_time[8].isdigit() or not date_and_time[9].isdigit():
        raise ValueError("Указан неверный формат даты")
    if not date_and_time[4] == "-" or not date_and_time[7] == "-":
        raise ValueError("Указан неверный формат даты")


    date = date_and_time[8:10] + "." + date_and_time[5:7] + "." + date_and_time[:4]
    return date

# "2024-03-11T02:26:18.671407"