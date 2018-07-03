# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:48:58 2017

@author: ice-fire
"""
import json

obj = {"one":1, "two":2, "three":[1,2,3], "four":4, "five":5}

encoded = json.dumps(obj)
print(type(encoded))
print(encoded)

decoded = json.loads(encoded)
print(type(decoded))
print(decoded)


