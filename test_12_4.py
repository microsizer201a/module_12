import unittest, logging
from module_12_4 import Runner

class RunnerTest(unittest.TestCase):



    def test_walk(self):
        try:
            speed = -1
            test_walk = Runner("test_walk", speed)
            for i in range(10):
                test_walk.walk()
            self.assertEqual(test_walk.distance, speed * 10)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as ve:
            logging.warning("Неверная скорость для Runner", exc_info=True)



    def test_run(self):
        try:
            name = 1
            test_run = Runner(name)
            for i in range(10):
                test_run.run()
            self.assertEqual(test_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as te_:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


    def test_challenge(self):
        test_walk = Runner("test_walk")
        test_run = Runner("test_run")
        for i in range(10):
            test_walk.walk()
            test_run.run()
        self.assertNotEqual(test_walk.distance, test_run.distance)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(levelname)s | %(message)s")
    unittest.main()