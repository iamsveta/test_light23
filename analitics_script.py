from matplotlib import pyplot as plt # импортирую библиотеку matplotlib модуль pyplot
import os # для проверки пути файла


class SalesAnalyzer: # создаю класс анализатор продаж)
    def __init__(self, file_path): # инициализатор класса, принимает на вход путь к файлу
        if not self.is_valid_file_path(file_path): # использование функции для проверки пути файла
            raise FileNotFoundError(f"Файл по пути {file_path} не найден или недоступен.")
        self.sales_list_data = self.read_sales_data(file_path)

    def is_valid_file_path(self, file_path): # проверяет путь
        return os.path.isfile(file_path)

    def read_sales_data(self, file_path): # функция для чтения файла с данными
        sales_list = [] # создаю список, куда будут вноситься словари с продажами после чтения файла
        with open(file_path, "r", encoding='utf-8') as file: # открываю файл для чтения, кодировка utf-8 для русского языка
            lines = file.readlines() # читаю все строки файла, в переменной список строк
            for line in lines: # прохожу циклом по каждой строке в списке строк файла
                one_string = line.split(', ') # преобразую строку в список
                sales_dict = { # создаю словарь
                    'product_name': one_string[0].strip(), # имя продукта первое в строке
                    'quantity': int(one_string[1].strip()), # количество, преобразую в integer
                    'price': int(one_string[2].strip()), # цена, преобразую в integer
                    'date': one_string[3].strip() # дата продажи
                }
                sales_list.append(sales_dict) # добавляю строку-словарь в список
        return sales_list # функция возвращает список словарей, полученных из каждой строки

    def total_sales_per_product(self): # функция для подсчета общей суммы продаж по каждому продукту
        sales_per_product = {} # создаю пустой словарь, не множество (множество set())

        for x in self.sales_list_data: # прохожу циклом по каждому словарю в списке, поданном на входе
            name = x['product_name'] # беру имя из словаря
            quantity = x['quantity'] # беру количество из словаря
            price = x['price'] # беру цену из словаря

            total_sale = quantity * price # считаю сумму продажи

            if name in sales_per_product.keys(): # если продукт уже есть в списке
                sales_per_product[name] += total_sale  # то добавляю сумму к существующему продукту
            else:
                sales_per_product[name] = total_sale

        max_product_sales = max(sales_per_product, key = sales_per_product.get)

        return sales_per_product, max_product_sales # возвращаю словарь с суммой продаж по каждому продукту и продукт с макс кол-вом продаж


    def sales_over_time(self): # функция для подсчета общей суммы продаж по каждой дате
        sales_per_date = {}  # создаю пустой словарь

        for x in self.sales_list_data:  # прохожу циклом по каждому словарю в списке, поданном на входе
            date = x['date']  # беру дату из словаря
            quantity = x['quantity']  # беру количество из словаря
            price = x['price']  # беру цену из словаря

            total_sale = quantity * price  # считаю сумму продажи

            if date in sales_per_date.keys():  # если дата уже есть в списке
                sales_per_date[date] += total_sale  # то добавляю сумму к существующей дате
            else:
                sales_per_date[date] = total_sale

        max_date_sales = max(sales_per_date, key = sales_per_date.get)  # нахожу дату с максимальными продажами

        return sales_per_date, max_date_sales  # возвращаю словарь с суммой продаж по каждой дате и дату

    def plot_total_sales_per_product(self): # cтроит график общей суммы продаж для каждого продукта
        total_sales, _ = self.total_sales_per_product() # берем данные, которые возвращает функция
        products = list(total_sales.keys()) # все ключи словаря формируют список продуктов
        sales = list(total_sales.values()) # все значения словаря формируют список продаж по продуктам
        plt.bar(products, sales) # строим график столбцовый
        plt.xlabel('Product Name')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Product')
        plt.show()

    def plot_sales_over_time(self): # cтроит график общей суммы продаж для каждой даты
        date_sales, _ = self.sales_over_time()
        dates = list(date_sales.keys())
        sales = list(date_sales.values())
        plt.plot(dates, sales) # продажи по датам
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.title('Sales Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


file_path = input("Введите путь к файлу: ")
try:
    analyzer = SalesAnalyzer(file_path)

    _, max_product = analyzer.total_sales_per_product() # определяем продукт с наибольшей выручкой, нижнее подчеркивание для пропуска словаря
    print(f"Продукт с наибольшей выручкой: {max_product}.")

    _, max_day = analyzer.sales_over_time() # день с наибольшей суммой продаж, нижнее подчеркивание для пропуска словаря
    print(f"День с наибольшей суммой продаж: {max_day}.")

    # графики
    analyzer.plot_total_sales_per_product()
    analyzer.plot_sales_over_time()
except FileNotFoundError as e:
    print(e)