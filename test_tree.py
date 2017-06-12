# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 00:58:56 2017

@author: Emely
"""

class Node:
    
    """
	 Tree node: left and right child + data which can be any object
	 """
    
    def __init__(self, value):
        
        """
        Node constructor
        @param data node data object
        """
        
        self.root = value
        self.left = None
        self.right = None
        self.value = value
        self.item = value  	        

    def get_root(self):
        return self.root
    
    def get_value(self):
        return self. value
    
    def get_item(self):
        return self.item

    def insert(self, value):

	        """
	        Insert new node with data
	        @param data node data object to insert
	        """

	        if self.value:

	            if value < self.value:
	                if self.left is None:
	                    self.left = Node(value)

	                else:
	                    self.left.insert(value)

	            elif value > self.value:
	                if self.right is None:
	                    self.right = Node(value)

	                else:
	                    self.right.insert(value)

	        else:
	            self.value = value

    def print_tree(self):
	        """
	        Print tree content inorder
	        """
	        if self.left:
	            self.left.print_tree()

	        print self.value,

	        if self.right:
	            self.right.print_tree()    
       
def test_tree():
    
    names = ['aaron', 'maaron5', 'madonna', 'diana', 'helene', 'beyonce', 'rihanna', 'eminem']
    root = Node(names[0])

    for i in range(1, len(names)):
        root.insert(names[i])
    root.print_tree()
    print(root.get_root())
    print(root.get_value())
    return root                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	       