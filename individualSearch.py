# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 01:39:54 2017

@author: Emely

search functions for the individual trees
"""
import re

def search_song(word, tree, prioList):
    
    node = find(tree, word)
    files = node.item
    return order_List(files, prioList)
    
def search_artist(word, tree, prioList):
    
    node = find(tree, word)
    files = node.item
    return order_List(files, prioList)
       
def search_lyrics(word, tree, prioList):
    
    wordList = re.sub("[^\w]", " ", word).split()
    files = []
    for i in range(0, len(wordList)-1):
        node = find(tree, wordList[i])
        temp_files = node.item
        if i==0:
            files=temp_files
        else:
            for j in range(0, len(files)-1):
                if not(files[j] in temp_files):
                    files.remove(files[j])
    return order_List(files, prioList)
    
 
#------------------------------------------------------------------------------

def find(tree, word):
    return findNode(tree.root, word)
    
def findNode(node, word, parent=None):
 
    if node is None:
        return None
    elif word == node.value:
        print(node.value)
        return node
    elif word < node.value:
        print(node.value)
        return findNode(node.leftChild, word)
    else:
        print(node.value)
        return findNode(node.rightChild, word)
    
def findFile(node):
    
    results = []
    if node is None:
        return results
    elif not(node.leftChild is None):
        results.append(node.leftChild.item)
        return findFile(node.leftChild ,results)
    elif not(node.rightChild is None):
        results.append(node.rightChild.item)
        return findFile(node.rightChild, results)
    elif (node.leftChild is None) and (node.rightChild is None):
        return results
    
def order_List(results, prioList):
    
    if len(prioList)==0:
        return results
    else:
        for i in range(0, len(prioList)):
            phrase = prioList[len(prioList)-1-i]
            if phrase in results:
                results.remove(phrase)
                results.insert(0, phrase)
