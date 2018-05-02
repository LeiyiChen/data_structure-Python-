# 链表
链表的实现及增加、删除、插入、更新。
```python
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
```
ps:链表需要用一个变量来存储头节点，通过使用变量.next属性，来遍历后续结点。一般头节点是不存储数值的，只存储第一个结点的位置。

# 树
二叉树的实现及遍历
```
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
```
知识点：
#### 1. 遍历
所谓遍历是指对树中所有结点的信息的访问，即依次对树中每个结点访问一次且仅访问一次。
树的两种重要的遍历模式是深度优先遍历和广度优先遍历：
+ 深度优先一般用递归
+ 广度优先一般用队列

1、前序遍历：
2、中序遍历
3、后序遍历
4、层次遍历（广度遍历）

** 问题 ** ：哪两种遍历方式能顾唯一确定一棵树？
答：中序+先序、中序+后序、中序+层次都可以确定一棵树。但先序和后序无法确定一棵树。

#### 2. 二叉排序树（BST）又称二叉查找树、二叉搜索树
二叉排序树(Binary Sort Tree)又称二叉查找树。它或者是一棵空树；或者是具有下列性质的二叉树：
1.若左子树不空，则左子树上所有结点的值均小于根结点的值；
2.若右子树不空，则右子树上所有结点的值均大于根节点的值；
3.左、右子树也分别为二叉排序树。

从二叉查找树BST中查找元素X，返回其所在结点的地址，查找的次数取决于树的高度。

#### 3.平衡二叉树（AVL树）
平衡二叉树的定义（Balance Binary tree）:
1.空树；
2.任意节点左右子树的高度差不超过1，即|BF|<=1。

平衡二叉树的调整：
1.RR调整




