class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        dirnames = []
        for dir in dirs:
            if dir == "." or dir == "":
                continue
            elif dir == "..":
                if len(dirnames) > 0:
                    last = dirnames.pop()
            else:
                dirnames.append(dir)
        if len(dirnames) == 0:
            return "/"
        return "/" + "/".join(dirnames)
