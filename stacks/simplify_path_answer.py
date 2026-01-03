class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifyPath("/home/"))  # Output: /home
    print(solution.simplifyPath("/home//foo/"))  # Output: /home/foo
    print(
        solution.simplifyPath("/home/user/Documents/../Pictures")
    )  # Output: /home/user/Pictures
    print(solution.simplifyPath("/../"))  # Output: /
    print(solution.simplifyPath("/.../a/../b/c/../d/./"))  # Output: /.../b/d
