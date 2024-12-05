import runner_and_tournament
import unittest
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.runner_3 = runner_and_tournament.Runner('Ник', speed=3)
    
    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        print('Результат забега:')
        for i in range(self.count_participants):
            print(f'{i + 1}:', TournamentTest.all_results[i + 1])
        

    def test_Tournament1(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.count_participants = len(test_tour.participants)
        TournamentTest.all_results = test_tour.start()
        largest_key = max(TournamentTest.all_results)
        if TournamentTest.all_results[largest_key] == 'Ник':
            flag = True
        else:
            flag = False
        self.assertTrue(flag)

    def test_Tournament2(self):
        test_tour = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.count_participants = len(test_tour.participants)
        TournamentTest.all_results = test_tour.start()
        largest_key = max(TournamentTest.all_results)
        if TournamentTest.all_results[largest_key] == 'Ник':
            flag = True
        else:
            flag = False
        self.assertTrue(flag)

    def test_Tournament3(self):
        test_tour = runner_and_tournament.Tournament(6, self.runner_1, self.runner_2, self.runner_3)
        self.count_participants = len(test_tour.participants)
        TournamentTest.all_results = test_tour.start()
        largest_key = max(TournamentTest.all_results)
        if TournamentTest.all_results[largest_key] == 'Ник':
            flag = True
        else:
            flag = False
        self.assertTrue(flag)




if __name__ == '__main__':
    unittest.main()