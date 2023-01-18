from os import path
import re


class Solution:

    def simplifyPath(self, path: str) -> str:
        splitPath = path.split("/")
        stack = []
        for c in splitPath:
            if c == "" or c == ".":
                continue
            if c == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(c)

        print(stack)
        return '/' + "/".join(stack)


def test_():
    solution = Solution()
    assert solution.simplifyPath("/a/./b/../../c/") == "/c"
    assert solution.simplifyPath("/a/../../b/../c//.//") == "/c"
    assert solution.simplifyPath("/home/") == "/home"
    assert solution.simplifyPath("/../") == "/"
    assert solution.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
    assert solution.simplifyPath("/...") == "/..."
    assert solution.simplifyPath("/abc/...") == '/abc/...'
    assert solution.simplifyPath("/.aa/....hidden") == "/.aa/....hidden"
    assert solution.simplifyPath(
        "/home/foo/.ssh/authorized_keys/") == "/home/foo/.ssh/authorized_keys"
    assert solution.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/"
                                 ) == "/home/foo/.ssh2/authorized_keys"
