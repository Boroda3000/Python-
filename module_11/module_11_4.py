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
        print("Результаты всех турниров:")
        for tournament_name, results in cls.all_results.items():
            print(f"{tournament_name}:")
            for place, runner in results.items():
                print(f"{place} место: {runner.name}")
    def tearDown(self):
        print('Результат забега:')
        for i in range(len(self.tour_result)):
            print(f'{i + 1} : {self.tour_result[i+1]}')
       
    def test_Tournament1(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.tour_result = test_tour.start()
        self.count_participants = len(test_tour.participants)
        try:
            largest_key = max(self.tour_result)
            self.assertEqual(self.tour_result[largest_key].name, 'Ник')
        except (ValueError, KeyError):
            self.fail("Ошибка при доступе к результатам")
        self.all_results[f'Турнир №1'] = self.tour_result

    def test_Tournament2(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.tour_result = test_tour.start()
        self.count_participants = len(test_tour.participants)
        try:
            largest_key = max(self.tour_result)
            self.assertEqual(self.tour_result[largest_key].name, 'Ник')
        except (ValueError, KeyError):
            self.fail("Ошибка при доступе к результатам")
        self.all_results[f'Турнир №2'] = self.tour_result

    def test_Tournament3(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.tour_result = test_tour.start()
        self.count_participants = len(test_tour.participants)
        try:
            largest_key = max(self.tour_result)
            self.assertEqual(self.tour_result[largest_key].name, 'Ник')
        except (ValueError, KeyError):
            self.fail("Ошибка при доступе к результатам")
        self.all_results[f'Турнир №3'] = self.tour_result




if __name__ == '__main__':
    unittest.main()