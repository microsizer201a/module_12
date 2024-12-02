import unittest
from module_12_2 import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    def test_tournament_1(self):
        test_tournament = Tournament(90, self.usain, self.nick)
        result = test_tournament.start()
        for key, value in result.items():
            result[key] = str(value)
        self.assertTrue(result[max(result.keys())] == "Ник")
        self.all_results[1] = result

    def test_tournament_2(self):
        test_tournament = Tournament(90, self.andrei, self.nick)
        result = test_tournament.start()
        for key, value in result.items():
            result[key] = str(value)
        self.assertTrue(result[max(result.keys())] == "Ник")
        self.all_results[2] = result

    def test_tournament_3(self):
        test_tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = test_tournament.start()
        for key, value in result.items():
            result[key] = str(value)
        self.assertTrue(result[max(result.keys())] == "Ник")
        self.all_results[3] = result

if __name__ == "__main__":
    unittest.main()