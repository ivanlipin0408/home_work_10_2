def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует часть номера карты"""
    card_number_without_spaces = card_number.replace(" ", "")
    masked_card_number = (
        card_number_without_spaces[0:4]
        + " "
        + card_number_without_spaces[4:6]
        + "** **** "
        + card_number_without_spaces[12:]
    )
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскирует часть номера счета, выводит последние 4 цифры"""
    account_number_without_spaces = account_number.replace(" ", "")
    masked_account_number = "**" + account_number_without_spaces[-4:]
    return masked_account_number
