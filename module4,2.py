def test_function():
    print('Тестовая функция')
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
inner_function()