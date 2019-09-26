#!/usr/bin/env python3

import licant 
import os

install_headers_path = "/usr/local/include/"
libname = "linalg-v3"

hpath = os.path.join(install_headers_path, libname)

licant.source("linalg-v3/linalg.h")
licant.source("linalg-v3/linalg-ext.h")
licant.copy(src="linalg-v3/linalg.h", tgt=os.path.join(hpath,"linalg.h"))
licant.copy(src="linalg-v3/linalg-ext.h", tgt=os.path.join(hpath,"linalg-ext.h"))

licant.fileset("install", 
[
	os.path.join(hpath,"linalg-ext.h"),
	os.path.join(hpath,"linalg.h")
])

licant.ex("install")