# 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Node 를 사용해서 트리 만들어 보기


root = Node(1)  # root 노드 만들기

# 2, 3 을 root의 왼쪽과 오른쪽에 추가
root.left = Node(2)
root.right = Node(3)

# 4, 5 를 2번의 왼쪽과 오른쪽에 추가
root.left.left = Node(4)  # Node(2).left
root.left.right = Node(5)  # Node(3).right


# 전위순회 V L R
def preorder(node):
    if node:
        print(node.data, end=" ")
        # 왼쪽 방문
        preorder(node.left)
        # 오른쪾 방문
        preorder(node.right)


preorder(root)  # 1 2 4 5 3
print()


# 중위순회 L V R
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


inorder(root)  # 4 2 5 1 3
print()


# 후위순회 L R V
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


postorder(root)  # 4 5 2 3 1
print()
