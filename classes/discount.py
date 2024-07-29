class Discount:
    """
    Класс Discount

    Этот класс управляет скидками, которые могут применяться к ценам товаров.

    Атрибуты:
        description (str): Описание скидки (например, 'Сезонная скидка').
        discount_percent (float): Процент скидки.
    """

    def __init__(self, description: str, discount_percent: float):
        """
        Метод инициализации для создания новой скидки.

        Аргументы:
            description (str): Описание скидки.
            discount_percent (float): Процент скидки, который будет применяться.
        """
        self.description = description    # Описание скидки
        self.discount_percent = discount_percent  # Процент скидки

    @staticmethod
    def apply_discount(price: float, discount_percent: float) -> float:
        """
        Статический метод для применения скидки к цене.

        Аргументы:
            price (float): Исходная цена, к которой будет применяться скидка.
            discount_percent (float): Процент скидки.

        Возвращает:
            float: Цена после применения скидки.
        """
        return price * (1 - discount_percent / 100)  # Рассчитываем цену после скидки

    def __str__(self):
        """
        Дандер метод для возвращения строкового представления скидки.

        Возвращает:
            str: Форматированная строка с информацией о скидке.
        """
        return f"Скидка (Описание={self.description}, Процент={self.discount_percent})"  # Возвращаем описание и процент скидки
