from src import masks


def mask_account_card(card_account_number: str) -> str:
    """Функция различает номер счета и номер карты, возвращает частично замаскированный номер"""
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
    date = date_and_time[8:10] + "." + date_and_time[5:7] + "." + date_and_time[:4]
    return date
