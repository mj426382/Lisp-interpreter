import unittest

from atom import parse_atom
from list import parse_list
from operation import parse_operation
from condition import parse_condition
from function import parse_function

class test_parsing(unittest.TestCase):

    def test_true(self):
        self.assertEqual(True, parse_atom('true'))

    def test_single_number(self):
        self.assertEqual(1, parse_atom('1'))

    def test_complex_number(self):
        self.assertEqual(1000, parse_atom('1000'))

    def test_text(self):
        self.assertEqual('test', parse_atom('test'))

    def test_text_with_whitespaces(self):
        self.assertEqual('test', parse_atom('   test   '))

    def test_single_object_list(self):
        self.assertEqual(['test'], parse_list('(test)'))

    def test_multiple_object_list(self):
        self.assertEqual(['test1', 'test2', 'test3'], parse_list('(test1 test2 test3)'))

    def test_nested_lists_list(self):
        self.assertEqual(['test1', ['test2', ['test3']], 'test4', ['test5']], parse_list('(test1 (test2 (test3)) test4 (test5))'))

    def test_mixed_atoms_list(self):
        self.assertEqual(['+', 1, ['*', 3, 4]], parse_list('(+ 1 (* 3 4))'))

    def test_mixed_add_atoms_list(self):
        self.assertEqual(6, parse_operation('(+ 1 2 3)'))

    def test_mixed_substract_atoms_list(self):
        self.assertEqual(5, parse_operation('(- 10 2 3)'))
    
    def test_mixed_sum_lists_list(self):
        self.assertEqual(20, parse_operation('(+ (+ 10 5) (+ 2 3))'))

    def test_mixed_sum_double_lists_list(self):
        self.assertEqual(25, parse_operation('(+ 5 (+ (+ 10 5) (+ 2 3)))'))

    def test_mixed_sum_super_lists_list(self):
        self.assertEqual(38, parse_operation('(+ 5 (+ (+ 10 5) (+ (- 5 2) (* 1 10 1 1 1 )) (+ 2 3)))'))

    def test_not_operator(self):
        self.assertEqual(True, parse_operation('(not false)'))

    def test_or_operator(self):
        self.assertEqual(True, parse_operation('(or true false)'))
    
    def test_max_operator(self):
        self.assertEqual(50, parse_operation('(max 1 50)'))

    def test_complex_operators_list(self):
        self.assertEqual(True, parse_operation('(== (== 10 10) (/= a b))'))

    def test_basic_condition(self):
        self.assertEqual(9, parse_condition('(if (and (< 2 1) (> 3 1)) first (* 3 3))'))
    
    def test_complex_condition(self):
        self.assertEqual(9, parse_condition('(if (and (< 2 1) (> 3 1)) first (if (and (< 2 1) (> 3 1)) first (* 3 3)))'))

    def test_simple_main_function(self):
        self.assertEqual(3, parse_function('(defun main () 3)'))

    def test_multiple_lines_main_function(self):
        self.assertEqual(3, parse_function('(defun main () 3 3 3 3 3)'))
    
    def test_function_with_argument(self):
        self.assertEqual(3, parse_function('(defun main () (defun c (n) n) (c 3))'))

    def test_multiplying_function_result(self):
        self.assertEqual(6, parse_function('(defun main () (defun c (n) n) (* 2 (c 3)))'))

    def test_multiplying_function_result2(self):
        self.assertEqual('first', parse_function('(defun main () (defun newC (n) (if (and (< 2 n) (> 10 n)) first second)) (newC (- 4 1)))'))

    def test_recursive_function(self):
        self.assertEqual(120, parse_function('(defun main () (defun fac (n) (if (>= 1 n) 1 (* n (fac (- n 1))))) (fac 5))'))

if __name__ == '__main__':
    unittest.main()
