# -*- coding: utf-8 -*-

import unittest
import CalculateService

class CalcuateServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = CalculateService.CalculateService()
    
    def test_get_scale(self):
        test_key_list = []
        answer = {}
        
        answer['A'] = ['a', 'b', 'c+', 'd', 'e', 'f+', 'g+']  
        answer['B'] = ['b', 'c+', 'd+', 'e', 'f+', 'g+', 'a+']  
        answer['C'] = ['c', 'd', 'e', 'f', 'g', 'a', 'b']  
        answer['D'] = ['d', 'e', 'f+', 'g', 'a', 'b', 'c+']  
        answer['E'] = ['e', 'f+', 'g+', 'a', 'b', 'c+', 'd+']  
        answer['F'] = ['f', 'g', 'a', 'b-', 'c', 'd', 'e']  
        answer['G'] = ['g', 'a', 'b', 'c', 'd', 'e', 'f+']

        answer['a'] = ['a', 'b', 'c+', 'd', 'e', 'f+', 'g+']  
        answer['b'] = ['b', 'c+', 'd+', 'e', 'f+', 'g+', 'a+']  
        answer['c'] = ['c', 'd', 'e', 'f', 'g', 'a', 'b']  
        answer['d'] = ['d', 'e', 'f+', 'g', 'a', 'b', 'c+']  
        answer['e'] = ['e', 'f+', 'g+', 'a', 'b', 'c+', 'd+']  
        answer['f'] = ['f', 'g', 'a', 'b-', 'c', 'd', 'e']  
        answer['g'] = ['g', 'a', 'b', 'c', 'd', 'e', 'f+']

        answer['A+'] = ['a+', 'b+', 'c++', 'd+', 'e+', 'f++', 'g++']  
        answer['B+'] = ['b+', 'c++', 'd++', 'e+', 'f++', 'g++', 'a++']  
        answer['C+'] = ['c+', 'd+', 'e+', 'f+', 'g+', 'a+', 'b+']
        answer['D+'] = ['d+', 'e+', 'f++', 'g+', 'a+', 'b+', 'c++']  
        answer['E+'] = ['e+', 'f++', 'g++', 'a+', 'b+', 'c++', 'd++']  
        answer['F+'] = ['f+', 'g+', 'a+', 'b', 'c+', 'd+', 'e+']  
        answer['G+'] = ['g+', 'a+', 'b+', 'c+', 'd+', 'e+', 'f++']

        answer['a+'] = ['a+', 'b+', 'c++', 'd+', 'e+', 'f++', 'g++']  
        answer['b+'] = ['b+', 'c++', 'd++', 'e+', 'f++', 'g++', 'a++']
        answer['c+'] = ['c+', 'd+', 'e+', 'f+', 'g+', 'a+', 'b+']
        answer['d+'] = ['d+', 'e+', 'f++', 'g+', 'a+', 'b+', 'c++']  
        answer['e+'] = ['e+', 'f++', 'g++', 'a+', 'b+', 'c++', 'd++']  
        answer['f+'] = ['f+', 'g+', 'a+', 'b', 'c+', 'd+', 'e+']  
        answer['g+'] = ['g+', 'a+', 'b+', 'c+', 'd+', 'e+', 'f++']
        
        for i in range(40, 128):
            test_key_list.append(chr(i))

        result = []
        for key in test_key_list:
            result.append(self.service.get_scale(key))

        for idx in range(len(test_key_list)):
            if test_key_list[idx] not in answer:
                self.assertEqual(result[idx], False)
            else:
                self.assertEqual(result[idx], answer[test_key_list[idx]])
                
    def test_get_sacle_raise_exception(self):
        self.assertRaises(Exception, lambda: self.service.get_scale('yasdas'))


