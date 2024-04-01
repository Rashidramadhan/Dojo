import unittest

from Tutorialtesting.countrycodes import get_CountryCodes
class MyTestCase(unittest.TestCase):
    def test_allow_country(self):
        country_codes_Available = ['US', 'UK', 'KE', 'TZ', 'UG', 'EN', 'DN']
        for get_code in country_codes_Available:
            country = get_CountryCodes(code=get_code)
            self.assertTrue(country[0])
            self.assertEqual(dict, type(country[1]))# add assertion here

    def test_disallow_country(self):
        country = get_CountryCodes(code='SA')
        self.assertFalse(country[0])
        self.assertEqual(None, (country[1]))

    def test_raise_country_TypeError(self):
        with self.assertRaises(TypeError):
            get_CountryCodes()
            get_CountryCodes(12)

    def test_raise_country_ValueError(self):
        with self.assertRaises(ValueError):
            get_CountryCodes(code='United States of America')
            get_CountryCodes(code='U')
            get_CountryCodes(code='')

if __name__ == '__main__':
    unittest.main()
