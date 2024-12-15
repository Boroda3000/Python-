import unittest
import module_11_3
import module_11_4

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_11_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_11_4.TournamentTest))

test_run = unittest.TextTestRunner(verbosity=2)
test_run.run(test_suite)
