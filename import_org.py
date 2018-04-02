from importlib.abc import MetaPathFinder
from importlib.machinery import PathFinder
import subprocess
import sys


def tangle(fullname):
    cmd = [
        "emacs", "-Q", "--batch", "--file", f"{fullname}.org", "--eval",
        "(org-babel-tangle)"
    ]

    subprocess.check_call(
        cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class OrgFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        try:
            tangle(fullname)
        except subprocess.CalledProcessError:
            return None
        else:
            return PathFinder().find_spec(fullname, path, target)


sys.meta_path.append(OrgFinder())
