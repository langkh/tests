Was trying to do some instance segmentation stuff in roboflow, while the camera is capturing and deleteing frames,so you gotta unlink the file right\n
I kept getting a permission error and wasn't sure why.\n
Was cause u can't unlink() within with statement, makes sense obv\n
but like it works without a problem on MacOS so idk. 
