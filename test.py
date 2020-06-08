#!/usr/bin/python3
from app import *
import unittest

class MyTest(unittest.TestCase):

    urlObj = ShortURL(False)

    def test_shortURLTest(self):
        self.assertEqual(urlObj.shorten("www.samsung.com","sam"),"http://localhost/sam")
    
    def test_visitURLTest(self):
        self.assertEqual(urlObj.visit("http://localhost/sam"),"www.samsung.com")

    def test_counterURLTest(self):
        self.assertEqual(urlObj.countsVisited("http://localhost/sam"),2)

    def test_dummyURLTest(self):
        self.assertEqual(urlObj.visit("http://localhost/dummy"),"302")

    def test_duplicateURLTest(self):
        self.assertEqual(urlObj.shorten("www.tmobile.com","tmob"),"Duplicate")

if __name__ == '__main__':
    unittest.main()