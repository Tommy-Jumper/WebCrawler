# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 00:28:55 2017

@author: Emely
"""

import searchAlgo
#import test_tree
import tree

prio = []

#artist = test_tree.test_tree()
artist = tree.main()
order_list = searchAlgo.search('Enrique Iglesias', 'artist', artist, prio)
print(order_list)