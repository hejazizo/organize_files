import sys

from utils import OrganizeDir

if len(sys.argv) < 2:
    raise IndexError("Input path not given!")

org = OrganizeDir(sys.argv[1])
org.run()
