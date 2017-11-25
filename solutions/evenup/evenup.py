class Stack :
    def __init__(self) :
        self.__data = []

    def push(self, e) :
        self.__data.append(e)

    def peek(self) :
        if len(self.__data) == 0 :
            return None

        return self.__data[-1]

    def pop(self) :
        if len(self.__data) == 0 :
            return None

        result = self.peek()
        del self.__data[-1]
        return result

    def size(self) :
        return len(self.__data)

    def is_empty(self) :
        return self.size() == 0

input()
cards = list(map(int,input().split()))

stack = Stack()
for card in cards :
    
    if stack.is_empty() :
        stack.push(card)
        continue
    
    top = stack.peek()
    count = 0
    if top%2 == 0 :
        count += 1
    if card%2 == 0 :
        count += 1
        
    if count == 0 or count == 2 :
        stack.pop()
        continue
    else :
        stack.push(card)
        continue

print(stack.size())
    
