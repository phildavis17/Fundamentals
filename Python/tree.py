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

    def insert(self, val) -> None:
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


    def __contains__(self, val) -> bool:
        pass

    def __repr__(self) -> str:
        

    def __str__(self) -> str:
        pass
