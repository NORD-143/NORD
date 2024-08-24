import os, sys
os.system("git pull")
try:
    __import__("NORDPPP").menu()
except Exception as e:
    exit(str(e))
