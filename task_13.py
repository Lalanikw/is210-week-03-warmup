#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL
"""

import task_12
print task_12.FLOATVAL == task_12.DECVAL
print 'FRAC_DEC_EQUAL'
print task_12.DECVAL != task_12.FLOATVAL
print 'DEC_FLOAT_INEQUAL'
