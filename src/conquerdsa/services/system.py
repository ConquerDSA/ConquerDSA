import shutil
import sys


class SystemService:
    @staticmethod
    def python_version() -> str:
        return sys.version.split()[0]

    @staticmethod
    def git_installed() -> bool:
        return shutil.which("git") is not None