import runner
import unittest
import random

class RunnerTest(unittest.TestCase):

    is_frozen = False
    
    name_list = ['Bob', 'Ivan', 'Li', 'Matilda', 'Vasilasa']

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self, name = random.choice(name_list)):
        test_runner = runner.Runner(name)
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self, name = random.choice(name_list)):
        test_runner = runner.Runner(name)
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challange(self, name = random.choice(name_list)):
        test_runner1 = runner.Runner(name)
        test_runner2 = runner.Runner(name)
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)

if __name__ == '__main__':
    unittest.main()