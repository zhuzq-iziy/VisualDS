# path = []
# def dfs(subtree):
#     if subtree is None: return
#     dfs(subtree.left)
#     path.append(subtree.val)
#     dfs(subtree.right)
#     return
"""
idx = i
path[i] left->left_subtree [0,i) 
right->right_subtree (i, -1]
"""
"""
peoples = [[x1,y1], ...]
< \eta
"""
from collections import defaultdict
def mse(root, people):
    pass
def grouping(peoples, eta):
    used = defaultdict(int)
    ans = []
    for p in peoples:
        if used[p]: continue
        queue = []
        queue.append(p)
        # peoples = peoples[1:]
        path = []
        path.append(p)
        while(queue):
            len_pp = len(queue)
            tmp = []
            for i in range(len_pp):
                root  = queue[i]
                queue = queue[1:]
                used[root] = 1
                for people in peoples:
                    if not used[people] and mse(root, people) < eta:
                        # queue.append(people)
                        tmp.append(people)
                        path.append(people)
            queue = tmp
            # path.append(tmp)
        ans.append(path)
    return ans
"""
queue = [[x1, y1]]
tmp = [[x2,y2], [x3,y3]]
queue = tmp
tmp = [[x4, y4], ...]
"""             

            

