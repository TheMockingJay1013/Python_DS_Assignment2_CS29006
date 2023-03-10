class _DoubleLinkedBase:
	""" A base class providing a doubly linked list representation."""

	class _Node:
		""" Lightweight, nonpublic class for storing a doubly linked node"""
		__slots__ = '_element', '_prev', '_next' # streamline memory

		def __init__(self, element, prev, next): # initialize node's fields
			self._element = element
			self._prev = prev
			self._next = next

	def __init__(self):
		"""Create an empty list"""
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0 # number of elements

	def __len__(self):
		"""Return the number of elements in the list"""
		# ===== Start writing your code here =====
		return self._size
		# ===== End writing your code here =====

	def is_empty(self):
		"""Return  true if list is empty"""
		# ===== Start writing your code here =====
		return (self._size==0)
		# ===== End writing your code here =====

	def _insert_between(self, e, predecessor, successor):
		"""Add element e between two existing nodes and return new node"""
		newest = self._Node(e, predecessor, successor)
		# ===== Start writing your code here =====
		if predecessor._next==successor:      #checking if the predecessor and successor are adjacent
			predecessor._next=newest
			newest._prev=predecessor
			newest._next=successor
			successor._prev=newest
			self._size+=1
			return newest
		else :
			print("the given nodes are not adjacent")
		# ===== End writing your code here =====

	def _delete_node(self, node):
		"""Delete nonsentinel node from the list and return its elements"""
		# ===== Start writing your code here =====
		value=node._element
		if node._prev is None or node._next is None:  #checking is the node is a sentinel node
			print("cannot delete sentinel nodes")
		else:
			predecessor=node._prev
			successor=node._next
			predecessor._next=successor
			successor._prev=predecessor
			self._size-=1
		return value
		# ===== End writing your code here =====
#testing
lis1=_DoubleLinkedBase()
a=lis1._insert_between(12,lis1._header,lis1._trailer)
print(lis1.__len__(),a)
p=lis1._delete_node(lis1._header._next)
print(lis1.__len__(),p)


