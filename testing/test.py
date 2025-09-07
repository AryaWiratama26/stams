from stams.stams import *
import unittest

class StamsTesting(unittest.TestCase):
    
    def setUp(self):
        self.data = [1,2,3,4,5]
    
    
    def test_mean(self):
        self.assertEqual(mean(self.data), 3.0)
        
    def test_median(self):
        self.assertEqual(median(self.data), 3.0)

    def test_population_variance(self):
        self.assertEqual(variance(self.data, def_var='p'), 2.0)

    def test_sample_variance(self):
        self.assertEqual(variance(self.data, def_var='s'), 2.5)


    def test_std(self):
        self.assertEqual(std(self.data), 1.5811388300841898)

    def test_range(self):
        self.assertEqual(ranges(self.data), 4.0)
        
    def test_modus(self):
        self.assertEqual(modus(["a","a","b","c","d"]), ['a'])
        
        
if __name__ == "__main__":
    unittest.main()
