class Counter:
    count = 0  # Атрибут класу для зберігання кількості екземплярів

    def __init__(self):
        Counter.count += 1  # Збільшення лічильника кількості екземплярів

        self.call_count = 0  # Атрибут екземпляру для зберігання кількості викликів методу get_count

    @classmethod
    def get_count(cls):
        cls.count += 1
        return cls.count

# Створення екземплярів класу Counter


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

# Виклик методу get_count для екземплярів
print("Кількість екземплярів класу Counter:", Counter.get_count())
print("Кількість екземплярів класу Counter:", Counter.get_count())

# Виведення кількості екземплярів класу Counter
print("Загальна кількість екземплярів класу Counter:", Counter.count)
