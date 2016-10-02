# -*- coding: utf-8 -*-

"""Process some integers.

usage: pragma_generator.py [-h] hpp_filename dir_path_to_lib

options:
    -h, --help  show this help message and exit
"""

import sys
import glob, os

def parser():
    usage = 'Usage: python {} <hpp_filename> <dir_path_to_lib> [--help]'.format(__file__)
    arguments = sys.argv
    if len(arguments) == 1:
        return usage
    options = [option for option in arguments if option.startswith('-')]
    if '-h' in options or '--help' in options:
        return usage

def fetch_libname(path):

    lib_name = []
    files = glob.glob(path+"\\*.lib")

    for file in files:
        names = os.path.basename(file)
        lib_name += names.split("\n")

    return lib_name

def main():
    file_name = sys.argv[1] if sys.argv[1] else "hogehoge"
    path = sys.argv[2] if sys.argv[2] else os.getcwd()
    lib_names = fetch_libname(path)


    char_name_debug = ""
    char_name_release = ""
    pragma_char_debug = ""
    pragma_char_release = ""
    for name in lib_names:
        debug_libs = []
        release_libs = []
        if name.rfind("d.lib") == -1: # match release files
            release_libs.append(name)
            debug_libs.append(name.replace(".lib", "d.lib"))
        else: # match debug files
            debug_libs.append(name)
            release_libs.append(name.replace("d.lib", ".lib"))

        char_name_debug = ','.join(debug_libs)
        pragma_char_debug += '#pragma comment(lib, "' + char_name_debug + '")\n'
        char_name_release = ','.join(release_libs)
        pragma_char_release += '#pragma comment(lib, "' + char_name_release + '")\n'

    try:
        f = open(file_name + ".hpp", "w")
        f.write("#ifndef " + file_name.upper() + "\n#define " + file_name.upper() + "\n\n" \
                + "#if _DEBUG\n" \
                + pragma_char_debug \
                + "#else\n" \
                + pragma_char_release \
                + "\n#endif" \
                + "\n\n#endif" \
                )
    except:
        print("write failed!")
    finally:
        print("successed!")

if __name__ == '__main__':
    result = parser()
    if result:
        print(result)
    else:
        main()