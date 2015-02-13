#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""numeric types."""
import decimal
from fractions import Fraction
INTVAL = 1
FLOATVAL = decimal.Decimal('0.1')
DECVAL = decimal.Decimal('0.1')
FRACVAL = Fraction(1, 10)
print INTVAL
print FLOATVAL
print DECVAL
print FRACVAL
