#!/usr/bin/env python3

import licant 
import os

install_headers_path = "/usr/local/include/"
libname = "linalg"

hpath = os.path.join(install_headers_path, libname)

licant.source("linalg.h")
licant.copy(src="linalg.h", tgt=os.path.join(hpath,"linalg.h"))

licant.fileset("install", 
[
	os.path.join(hpath,"linalg.h")
])

licant.ex("install")