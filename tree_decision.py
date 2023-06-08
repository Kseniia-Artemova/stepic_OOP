class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx if type(indx) is int else None
        self.value = value

        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        if isinstance(obj, TreeObj):
            self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        if isinstance(obj, TreeObj):
            self.__right = obj


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        current = root
        while current.left is not None and current.right is not None:
            if x[current.indx]:
                current = current.left
            else:
                current = current.right
        else:
            return current.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):

        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj


# if __name__ == "__main__":
#
#     root = DecisionTree.add_obj(TreeObj(0))
#     v_11 = DecisionTree.add_obj(TreeObj(1), root)
#     v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
#     DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
#     DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
#     DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
#     DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
#     print(root.left, root.right)
#     print(root.left.right.value, root.right.left.value)
#
#     x = [1, 1, 0]
#     res = DecisionTree.predict(root, x)  # будет программистом
#     print(res)