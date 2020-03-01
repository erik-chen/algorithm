stack = [(root, 'white')]
while stack:
    node, color = stack.pop()
    if color == 'white':
        if node.right:
            stack.append((node.right, 'white'))
        if node.left:
            stack.append((node.left, 'white'))
        stack.append((node, 'gray'))
    else:
        pass