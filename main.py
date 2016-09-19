
class BinOp:
    """
    class represents binary tree node
    """
    def __init__(self, operator, left, right):
        self.op = operator
        self.left = left
        self.right = right

class Number:
    """
    class represents value node in tree
    """
    def __init__(self, value):
        self.value = value

# whole visitor is like switch statements (single dispatch)

class NodeVisitor:
    def visit(self, node):
        name = 'visit_' + type(node).__name__
        return getattr(self, name)(node)

class Printer(NodeVisitor):
    def visit_BinOp(self, node):
        self.visit(node.left)
        print("Operator", node.op)
        self.visit(node.right)
    def visit_Number(self, node):
        print("Number", node.value)

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    def visit_BinOp(self, node):
        leftval = self.visit(node.left)
        rightval = self.visit(node.right)
        if node.op == '+':
            return leftval + rightval
        elif node.op == '-':
            return leftval - rightval
        elif node.op == '*':
            return leftval * rightval
        elif node.op == '/':
            return leftval / rightval


# add all numbers from 0 to 100

left = []
right = []

for i in range(1, 51):
    left.append(i)

for j in range(51, 101):
    right.append(j)

binlist = []
for x,y in zip(left, right):
    binlist.append(BinOp('+', Number(x), Number(y)))

b = BinOp('+', binlist.pop(), binlist.pop())

temp = []
temp.append(b)

while binlist:
    item = binlist.pop()
    itemr = temp.pop()
    temp.append(BinOp('+', item, itemr))

Printer().visit(temp[0]) # print tree
print(Evaluator().visit(temp[0])) # print result