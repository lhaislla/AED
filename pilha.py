class Pilha(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return len(self.items) == 0

  def push(self,exp):
    self.items.append(exp)

  def pop(self):
    self.items.pop()

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)
