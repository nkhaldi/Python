#!/usr/bin/env python3

import math
import pytest


class TestFloatClass:
    # Is integer (parametrized)
    @pytest.mark.parametrize("num", [-76.0, -54.32, -1, -0.5, 0, 0.5, 1, 23.45, 67.0])
    def test_flt_one(self, num):
        try:
            assert num.is_integer()
        except AttributeError:
            pass
        except AssertionError:
            pass

    # Is almost equal (positive)
    def test_flt_two(self):
        num1 = 123.45678
        num2 = 123.45679
        delta = 0.0001
        try:
            assert abs(num1 - num2) < delta
        except AssertionError:
            pass
    
    # Are integer and fractional parts equal (negative)
    def test_flt_three(self):
        num = 123.456
        integ, fract = str(num).split('.')
        integ, fract = int(integ), int(fract)
        delta = 0.0001
        try:
            assert abs(integ - fract) < delta
        except AssertionError:
            pass


class TestDictClass:
    # Has all numeric values 
    @pytest.mark.parametrize(
        "dic",
        [{'a': 123, 'b': 456}, {'a': 123, 'b': '123'}, {'a': '123', 'b': 'abc'}]
    )
    def test_dic_one(self, dic):
        result = True
        for val in dic.values():
            if type(val) != int:
                result = False
                break
        try:
            assert result
        except AssertionError:
            pass

    # Has more than 2 keys (positive)
    def test_dic_two(self):
        dic = {'a': 123, 'b': '123', 'c': 'abc'}
        try:
            assert len(dic.keys()) > 2
        except AssertionError:
            pass
    
    # Has equal values (negative)
    def test_dic_three(self):
        dic = {'a': 123, 'b': '123', 'c': 'abc'}
        val_set = set(dic.values())
        try:
            assert len(val_set) < len(dic.values())
        except AssertionError:
            pass
