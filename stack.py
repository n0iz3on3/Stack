class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.get_size() == 0

    def get_push(self, elem):
        self.stack.append(elem)

    def get_pop(self):
        return None if self.is_empty() else self.stack.pop()
        
    def get_peek(self):
        return None if self.is_empty() else self.stack[-1]

    def get_size(self):
        return len(self.stack)


result = Stack()


TEST = '((([[[]]])))'


def chek_pair(line):
    for i in line:
        if i in '({[':
            result.get_push(i)
        elif result.is_empty():
            return False
        elif result.get_peek() + i in ['()', '[]', '{}']:
            result.get_pop()
        else:
            return False
    return result.is_empty()

print('Сбалансированно' if chek_pair(TEST) else 'Несбалансированно')
