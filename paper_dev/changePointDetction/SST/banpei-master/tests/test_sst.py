import unittest
import pandas as pd
from banpei.sst import SST


class TestSST(unittest.TestCase):

    def setUp(self):
        self.raw_data = pd.read_csv('tests/test_data/periodic_wave.csv')
        self.data = self.raw_data['y']

    def test_detect_by_svd(self):
        model = SST(w=50)
        results = model.detect(self.data)
        self.assertEqual(len(self.data), len(results))

    def test_detect_by_lanczos(self):
        model = SST(w=50)
        results = model.detect(self.data, is_lanczos=True)
        self.assertEqual(len(self.data), len(results))

    def test_stream_detect(self):
        model = SST(w=50)
        result = model.stream_detect(self.data)
        self.assertIsInstance(result, float)


if __name__ == "__main__":
    unittest.main()
