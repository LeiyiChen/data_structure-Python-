# -*- coding:utf-8 -*-
'''
用Python实现二叉搜索树。
'''


class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#求树的深度
def depth(root):
        if root is None:
            return 0
        else:
            return 1 + max(depth(root.left), depth(root.right))


#按序输出结点值（中序遍历）
def input_in_order(root):
	if root is  None:
		return
	input_in_order(root.left)
	print(root.val)
	input_in_order(root.right)



#（递归实现 、迭代实现）查询二叉搜索树中一个具有给点关键字的结点，返回该节点的位置。时间复杂度是O(h),h是树的高度。
#递归实现
def search1(root, value):
	if root is None or root.val == value:
		return root
	if root.val > value:
		return search1(root.left, value)
	if root.val < value:
		return search1(root.right, value)


#迭代实现
def search2(root, value):
	while root != None and root.val != value:
		if root.val > value:
			root = root.left
		elif root.val < value:
			root = root.right
	return root


#求最大关键字元素
#迭代实现
def max_value1(root):
	while root != None and root.left != None:
		root = root.right
	if root is None:
		return root
	else:
		return root.val

#递归实现
def max_value2(root):
	if root == None:
		return root
	elif root.right == None:
		return root.val
	else:
		return max_value2(root.right)


#求最小关键字元素
#递归实现
def min_value1(root):
	if root is None:
		return root
	elif root.left is None:
		return root.val
	else:
		return min_value1(root.left)


#迭代实现
def min_value2(root):
	if root is None:
		return root
	while root.left !=None:
		root = root.left
	return root.val


if __name__ == '__main__':
	a = Node(15)
	b = Node(6)
	c = Node(18)
	d = Node(4)
	e = Node(8)
	f = Node(17)
	g = Node(20)
	h = Node(13)
	i = Node(9)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.left = f
	c.right = g
	e.right = h
	h.left = i
	print(search1(a, 13))
	print(search2(a,13))
	print(max_value1(a))
	print(max_value2(a))
	print(min_value1(a))
	print(min_value2(a))






