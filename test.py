from subprocess import Popen,PIPE
import subprocess
import os,time
from github import Github

subprocess.call("git init", shell=True)
subprocess.call("git config user.name mirzaei-ce", shell=True)
subprocess.call("git add .", shell=True)
subprocess.call("git commit -m 'init'", shell=True)
subprocess.call("git remote add origin git@github.com:mirzaei-ce/final.git",shell=True)

p1 = Popen(["git","push","-u","origin","master"], stdout=PIPE, stdin=PIPE,)

p1.communicate()