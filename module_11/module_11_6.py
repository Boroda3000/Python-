import rt_with_exceptions
import unittest
import logging

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self, name = 777, speed = -7):
        try:
            test_runner = rt_with_exceptions.Runner(name, speed)
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info('test_walk успешно выполнен.')
        # except ValueError:
        #     logging.warning('Неверная скорость для Runner.')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner.')
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self, name = 'Ivan', speed = -7):
        try:
            test_runner = rt_with_exceptions.Runner(name, speed)
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info('test_run успешно выполнен.')
        # except TypeError:
        #     logging.WARNING('Неверный тип данных для объекта Runner.')
        except ValueError:
            logging.warning('Неверная скорость для Runner.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challange(self, name = 777, speed = -7):
        test_runner1 = rt_with_exceptions.Runner(name, speed)
        test_runner2 = rt_with_exceptions.Runner(name, speed)
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='a', filename='runner_tests.log', encoding='utf-8', format='%(asctime)s # %(levelname)s # %(message)s')
    unittest.main()