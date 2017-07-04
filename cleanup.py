# Small bit of code that cleans up images left by the user after analysis
import time
import os
from path import Path
def clean():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	d = Path(dir_path)
	files = d.walkfiles("*.jpeg")
	starttime=time.time()
	for file in files:
	    file.remove()
	    print "Removed {} file".format(file)
	    time.sleep(0.2 - ((time.time() - starttime) % 0.2))
	return "Done"
