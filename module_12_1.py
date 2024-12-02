import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_walk = Runner("test_walk")
        for i in range(10):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    def test_run(self):
        test_run = Runner("test_run")
        for i in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    def test_challenge(self):
        test_walk = Runner("test_walk")
        test_run = Runner("test_run")
        for i in range(10):
            test_walk.walk()
            test_run.run()
        self.assertNotEqual(test_walk.distance, test_run.distance)

if __name__ == "__main__":
    unittest.main()