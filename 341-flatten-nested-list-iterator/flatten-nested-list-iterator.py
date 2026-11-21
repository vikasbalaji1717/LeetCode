
# """
# This is the interface that allows for creating nested lists.
# You should not implement it.
# """

# class NestedInteger:
#     def isInteger(self) -> bool:
#         ...
#     def getInteger(self) -> int:
#         ...
#     def getList(self) -> list['NestedInteger']:
#         ...

class NestedIterator:

    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        self.hasNext()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:

        while self.stack:

            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()

            for item in reversed(top.getList()):
                self.stack.append(item)

        return False
