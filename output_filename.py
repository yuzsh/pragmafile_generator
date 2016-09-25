# -*- coding: utf-8 -*-

import sys
import glob, os

def fetch_libname(path):

    lib_name = []
    files = glob.glob(path+"\\*.lib")

    for file in files:
        names = os.path.basename(file)
        lib_name.append(names.split("\n"))

    return lib_name

if __name__ == '__main__':
    file_name = sys.argv[1] if sys.argv[1] else "hogehoge"
    path = sys.argv[2] if sys.argv[2] else os.getcwd()
    lib_names = fetch_libname(path)

    pragma_char = ""
    for name in lib_names:
        char_name = ','.join(name)
        pragma_char += "#pragma comment(lib, '"+char_name+"')\n"
    # print pragma_char

    try:
        f = open(file_name+".hpp", "w")
        f.write("#ifndef "+file_name.upper()+"\n#define "+file_name.upper()+"\n\n"\
                + pragma_char\
                + "\n#endif"\
                )
    except:
        print "write failed!"
    finally:
        print "successed!"