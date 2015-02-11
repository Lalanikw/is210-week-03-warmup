#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long book."""

FHANDLER = open('war_and_peace.txt', 'r')

WORDS = FHANDLER.read()

FHANDLER.close()
WORDCT = len(WORDS[3:566319])
print WORDCT
