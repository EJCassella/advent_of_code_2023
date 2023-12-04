# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import re
import numpy as np


with open('input.txt') as f:
  reader = csv.reader(f, delimiter="\n")
  str_list = list(reader)

total_points = 0

for ind, card in enumerate(str_list):
    num_of_matches = 0
    winning_numbers = card[0].split(':')[1].split('|')[0]
    winning_numbers = [n.group() for n in re.finditer(r'\d+', winning_numbers)]
    card_numbers = card[0].split(':')[1].split('|')[1]
    card_numbers = [n.group() for n in re.finditer(r'\d+', card_numbers)]
    for number in card_numbers:
        if number in winning_numbers:
            num_of_matches = num_of_matches + 1
    if num_of_matches == 0:
        card_points = 0
    else:
        card_points = 1 * (2**(num_of_matches-1))
    total_points = total_points + card_points