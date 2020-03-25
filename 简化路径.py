# -*- coding: utf-8 -*-
class Solution:
    def simplifyPath(self, path: str) -> str:
        # .表示当前目录本身，..返回上一级
        # 两个目录之间必须只有一个/，最后一个目录不能/结尾
        # 我感觉用个栈来维护
        # 我只想知道这个如果开头不为/是应该自己补上吗
        # 如果是三个点的话看成是一个名字叫...的目录
        res = ""
        tmp = ""
        tmp_stack = []
        path += "/"
        # 这么多个if，看了题解发现有的人直接一个字典解决了
        for i in range(len(path)):
            if path[i] != "/":
                tmp += path[i]
            else:
                if tmp.isalpha() or len(tmp) >= 3:
                    tmp_stack.append(tmp)
                elif tmp == "..":
                    if tmp_stack:
                        tmp_stack.pop()
                tmp = ""
        if tmp:
            tmp_stack.append(tmp)
        if tmp_stack:
            for i in tmp_stack:
                res += "/" + i
            return res
        else:
            return "/"


print(Solution().simplifyPath("/.../"))

