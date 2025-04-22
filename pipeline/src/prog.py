"""
https://github.com/DataScientest/pipeline-calculatrice-Jenkins.git
"""

import calc 
import sys 

if len(sys.argv) - 1 != 3: 
    print("need 3 arguments")
    sys.exit(0)

res = calc.ope(sys.argv[1],sys.argv[2],sys.argv[3])
if res != None: 
    print("{} {} {} = {}".format(sys.argv[2],sys.argv[1],sys.argv[3],res))
