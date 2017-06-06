# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 14:13:31 2017

@author: Emely

algorithm to search binary search tree for search word

@param word: of type string. The phrase we search for.
@param category: the category of the search: either 'artist', 'song' or 'lyrics'.
@param tree: binary search tree. Already has to be read-in. Attached files have
to be ordered in a binary search tree, too, with the node of the word as root.
@param prioList: the priority list of past searches which determines the ranking
of the files.
"""
import individualSearch

def search(word, category, tree, prioList):
    
    if(category=='artist'):
        individualSearch.search_artist(word, tree, prioList)
        
    elif(category=='song'):
        individualSearch.search_song(word, tree, prioList)
        
    elif(category=='lyrics'):
        individualSearch.search_lyrics(word, tree, prioList)
        
    else:
        print('Error: Category unknown')