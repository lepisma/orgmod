import subprocess
import importlib
import sys
import os


def tangle(orgfile):
    cmd = [
        "emacs", "-Q", "--batch", "--file", orgfile, "--eval",
        "(org-babel-tangle)"
    ]

    subprocess.check_call(
        cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class OrgFinder:
    def find_module(self, fullname, package_path):
        name = fullname.split(".")[-1]
        paths = ["./"]

        if package_path is not None:
            # Look in all its paths
            paths += package_path._path

        for path in paths:
            if os.path.exists(f"{os.path.join(path, name)}.org"):
                return OrgLoader()
        return None


class OrgLoader:
    def load_module(self, fullname):
        fullpath = fullname.replace(".", "/")
        tangle(f"{fullpath}.org")
        module = importlib.import_module(fullname)
        os.remove(f"{fullpath}.py")
        sys.modules[fullname] = module


sys.meta_path.append(OrgFinder())