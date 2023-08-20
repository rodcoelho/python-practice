#!/usr/bin/env python3


class CustomLLNode:
	def __init__(self, value):
		self.value = value
		self.node_head = None
		self.node_tail = None


class CustomLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, value):
		if self.head:
			n = CustomLLNode(value)
			old_n = self.tail
			old_n.node_tail=n
			n.node_head=old_n
			self.tail = n
		else:
			n = CustomLLNode(value)
			self.head = n
			self.tail = n
		return n

	def pop(self):
		ret_val = None
		if self.tail == self.head:
			ret_val = self.head
			self.tail, self.head = None, None
		if self.tail:
			ret_val = self.tail
			new_t = self.tail.node_head
			new_t.node_tail = None
			self.tail = new_t
		return ret_val.value

	def get_kth_node(self, k):
		current = None
		for i in range(k):
			if i == 0:
				current = self.head
				last_val = self.head.value
			else:
				current = current.node_tail
				
		return current.value

	def get_kth_node_rev(self, k):
		current = None
		for i in range(k):
			if i == 0:
				current = self.tail
				last_val = self.tail.value
			else:
				current = current.node_head
				
		return current.value