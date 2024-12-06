import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.tour_result = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.runner_3 = runner_and_tournament.Runner('Ник', speed=3)
    
    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def tearDown(self):
        print('Результат забега:')
        for i in range(self.count_participants):
            print(f'{i + 1}: {self.tour_result[i + 1].name}')
       
    def test_Tournament1(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.tour_result = test_tour.start()
        try:
            largest_key = max(self.tour_result)
            self.assertEqual(self.tour_result[largest_key].name, 'Ник')
        except (ValueError, KeyError):
            self.fail("Ошибка при доступе к результатам")
        self.all_results[f'Турнир №1'] = self.tour_result

    def test_Tournament2(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.tour_result = test_tour.start()
        try:
            largest_key = max(self.tour_result)
            self.assertEqual(self.tour_result[largest_key].name, 'Ник')
        except (ValueError, KeyError):
            self.fail("Ошибка при доступе к результатам")
        self.all_results[f'Турнир №2'] = self.tour_result

    def test_Tournament3(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.tour_result = test_tour.start()
        try:
            largest_key = max(self.tour_result)
            self.assertEqual(self.tour_result[largest_key].name, 'Ник')
        except (ValueError, KeyError):
            self.fail("Ошибка при доступе к результатам")
        self.all_results[f'Турнир №1'] = self.tour_result




if __name__ == '__main__':
    unittest.main()