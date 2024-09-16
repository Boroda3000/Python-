class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
    
class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        print(file.read())
        file.close()

    def __search(self, product):
        with open(self.__file_name, 'r') as file:
            text = file.read()
            if str(product.name) in text:
                return False
            else:
                return True

    def add(self, *products):
        for product in products:
            if isinstance(product, Product):
                if self.__search(product) is True:
                    file = open(self.__file_name, 'a')
                    file.write(f'{product}\n')
                else:
                    print(f'Продукт {product.name} уже есть в магазине.')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

#print(p2) # __str__

#s1.add(p1, p2, p3)

print(s1.get_products())