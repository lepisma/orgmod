import subprocess
import importlib
import sys
import os


def tangle(filename):
    cmd = [
        "emacs", "-Q", "--batch", "--file", filename, "--eval",
        "(org-babel-tangle)"
    ]

    subprocess.check_call(
        cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class OrgFinder:
    def find_module(self, module_name, package_path):
        if os.path.exists(f"{module_name}.org"):
            return OrgLoader()
        else:
            return None


class OrgLoader:
    def load_module(self, fullname):
        tangle(f"{fullname}.org")
        module = importlib.import_module(fullname)
        os.remove(f"{fullname}.py")
        sys.modules[fullname] = module


sys.meta_path.append(OrgFinder())
