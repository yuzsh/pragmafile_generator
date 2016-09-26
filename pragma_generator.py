# -*- coding: utf-8 -*-

import sys
import glob, os
import re

def fetch_libname(path):

    lib_name = []
    files = glob.glob(path+"\\*.lib")

    for file in files:
        names = os.path.basename(file)
        lib_name.append(names.split("\n"))

    return lib_name

def main():
    # file_name = sys.argv[1] if sys.argv[1] else "hogehoge"
    # path = sys.argv[2] if sys.argv[2] else os.getcwd()
    file_name = "hogehoge"
    path = "D:\\build\\bin_vtk\\lib\\Debug"
    lib_names = fetch_libname(path)


    char_name_debug = ""
    char_name_release = ""
    pragma_char_debug = ""
    pragma_char_release = ""
    for name in lib_names:
        debug_libs = []
        release_libs = []
        if str(name).rfind("d.lib") == -1: # match release files
            release_libs = name
            debug_libs.append(str(name).replace(".lib", "d.lib"))
        else: # match debug files
            debug_libs = name
            release_libs.append(str(name).replace("d.lib", ".lib"))

        char_name_debug = ','.join(debug_libs)
        pragma_char_debug += "#pragma comment(lib, '" + char_name_debug + "')\n"
        char_name_release = ','.join(release_libs)
        # pragma_char_release += "#pragma comment(lib, '" + char_name_release + "')\n"
        pragma_char_release += "#pragma comment(lib, '" + char_name_debug + "')\n"
        # print(pragma_char)

    try:
        f = open(file_name + ".hpp", "w")
        f.write("#ifndef " + file_name.upper() + "\n#define " + file_name.upper() + "\n\n" \
                + "#if _DEBUG\n" \
                + pragma_char_debug \
                + "#else\n" \
                + pragma_char_release \
                + "\n#endif" \
                )
    except:
        print("write failed!")
    finally:
        print("successed!")

if __name__ == '__main__':
    main()