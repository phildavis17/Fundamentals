import random
from typing import Union


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"TreeNode with value {self.val}"

    def __str__(self) -> str:
        return str(self.val)


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: Union[int, float]) -> None:
        if self.root is None:
            self.root = TreeNode(val)
            return

        hot = self.root
        placed = False
        while not placed:
            if hot.val > val:
                if hot.left is None:
                    hot.left = TreeNode(val)
                    placed = True
                else:
                    hot = hot.left
            else:
                if hot.right is None:
                    hot.right = TreeNode(val)
                    placed = True
                else:
                    hot = hot.right

    def __contains__(self, target) -> bool:
        hot = self.root
        while hot is not None:
            if hot.val == target:
                return True
            elif hot.val > target:
                hot = hot.left
            else:
                hot = hot.right
        return False

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass


if __name__ == "__main__":
    n = [i for i in range(10)]
    random.shuffle(n)
    t = Tree()
    for i in n:
        t.insert(i)

    print(0 in t)
    print(9 in t)
    print(-1 in t)
