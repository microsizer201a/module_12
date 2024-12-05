import unittest
from module_12_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_walk = Runner("test_walk")
        for i in range(10):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run = Runner("test_run")
        for i in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_walk = Runner("test_walk")
        test_run = Runner("test_run")
        for i in range(10):
            test_walk.walk()
            test_run.run()
        self.assertNotEqual(test_walk.distance, test_run.distance)

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
