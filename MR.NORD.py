import os, sys
os.system("git pull")
try:
    __import__("NORDPPP").aproval()
except Exception as e:
    exit(str(e))
