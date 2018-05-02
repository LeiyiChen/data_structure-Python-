# -*- coding:utf-8 -*-
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.length = 0
		self.head = None

	def is_empty(self):
		return self.length == 0

	def append(self, this_node):
		if isinstance(this_node, Node):
			pass
		else:
			this_node = Node(this_node)
		if self.is_empty():
			self.head = this_node
		else:
			p = self.head
			while p.next:
				p = p.next
			p.next = this_node
		self.length+=1

	def insert(self, this_node, index):
		if index > self.length:
			return 'Error'
		if isinstance(this_node, Node):
			pass
		else:
			this_node = Node(this_node)
		if index == 0:
			this_node.next = self.head
			self.head = this_node
		else:
			p = self.head
			while index-1:
				p = p.next
				index-=1
			this_node.next = p.next
			p.next = this_node
		self.length+=1

	def delete(self, index):
		if not 0<= index < self.length:
			return 'Error'
		if index == 0:
			self.head = self.head.next
		else:
			p = self.head
			while index-1:
				p = p.next
				index-=1
			p.next = p.next.next
		self.length-=1

	def update(self, data, index):
		if not 0<= index < self.length:
			return 'Error'
		if index == 0:
			self.head.data = data
		else:
			p = self.head
			while index:
				p = p.next
				index-=1
			p.data = data

	def get_data(self, index):
		if not 0<= index < self.length:
			return 'Error'
		if index == 0:
			return self.head.data
		else:
			p = self.head
			while index:
				p = p.next
				index-=1
			return p.data

	def get_length(self):
		return self.length

	def clear(self):
		self.head = None
		self.length = 0

	def PrintList(self):
		if self.length ==0:
			return None
		else:
			p = self.head
			while p.next:
				print(p.data,'-->',end = '')
				p = p.next
			print(p.data)

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    s = LinkedList()
    s.append(a)
    s.append(b)
    s.append(c)
    s.PrintList()
    s.insert(e,2)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.insert(d,0)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.delete(0)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.delete(2)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.update(0,1)
    print(s.head.data)
    print(s.head.next.data)
    print(s.get_data(0))
    print(s.get_data(1))
    print(s.get_length())
    s.PrintList()



