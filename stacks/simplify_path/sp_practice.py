class Solution:
    def simplifyPath(self, path: str) -> str:
        dirnames = []
        parts = path.split("/")
        for part in parts:
            if part == "." or part == "":
                continue
            elif dir == "..":
                if len(dirnames) > 0:
                    last = dirnames.pop()
            else:
                dirnames.append(part)
        if len(dirnames) == 0:
            return "/"
        "/" + "/".join(dirnames)
