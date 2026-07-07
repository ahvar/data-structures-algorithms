class Solution:
    def simplifyPath(self, path: str) -> str:
        dirnames = path.split("/")
        dirs = []

        for dir in dirnames:
            if dir == "." or dir == "":
                continue
            elif dir == "..":
                if len(dirnames) > 0:
                    dirnames.pop()
            else:
                dirnames.append(dir)
        "/" + "/".join(dirs)
