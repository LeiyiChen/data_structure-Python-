# -*- coding:utf-8 -*-
'''
用Python实现树，并遍历。
'''


class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def depth(root):
        if root is None:
            return 0
        else:
            return 1 + max(depth(root.left), depth(root.right))

    #前序遍历
def pre_order(root):
        if root is None:
             return
        else:
            print(root.val)
            pre_order(root.left)
            pre_order(root.right)

	#中序遍历
def mid_order(root):
        if root is None:
            return
        else:
            mid_order(root.left)
            print(root.val)
            mid_order(root.right)


	#后序遍历
def post_order(root):
        if root is None:
            return
        else:
            post_order(root.left)
            post_order(root.right)
            print(root.val)

#层次遍历
def level_order(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        current = q.pop(0)
        print(current.val)
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)

#按层次打印
def level_print(root):
	if root is None:
		return []
	p = [root]
	results = []
	current_level_num = 1
	next_level_num = 0
	d = []
	while p:
		current = p.pop(0)
		d.append(current.val)
		current_level_num -= 1
		if current.left:
				p.append(current.left)
				next_level_num += 1
		if current.right:
				p.append(current.right)
				next_level_num += 1
		if current_level_num == 0:
			current_level_num = next_level_num
			next_level_num = 0
			results.append(d)
			d = []
	return results[::-1]






if __name__ == '__main__':
	a = Node(3)
	b = Node(9)
	c = Node(20)
	d = Node('null')
	e = Node('null')
	f = Node(15)
	g = Node(7)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.left = f
	c.right = g
	print('深度：%d' % depth(a))
	print("前序遍历：")
	print(pre_order(a))
	print('中序遍历：')
	print(mid_order(a))
	print('后序遍历：')
	print(post_order(a))
	level_order(a)
	print(level_print(a))