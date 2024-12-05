import unittest
import test_12_3

suite_test = unittest.TestSuite()
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

test_run = unittest.TextTestRunner(verbosity=2)
test_run.run(suite_test)
