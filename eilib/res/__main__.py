import argparse
import os
import sys

from eilib.res.resfile import ResFile


def main():
    parser = argparse.ArgumentParser('eilib.res')
    parser.add_argument('-f', '--force', help='Overwrite existing files', action='store_true')
    parser.add_argument('path', help='Path to directory/file to pack/unpack')
    args = parser.parse_args()

    if os.path.isdir(args.path):
        print('TODO pack', args.path)
    elif os.path.isfile(args.path):
        name, ext = os.path.splitext(args.path)
        dirpath = name + '_' + ext.lstrip('.')
        if os.path.exists(dirpath) and not args.force:
            print('File or directory', dirpath, 'already exists', file=sys.stderr)
            sys.exit(1)

        os.mkdir(dirpath)
        with open(args.path, 'rb') as resfile:
            with ResFile(resfile) as res:
                for fileinfo in res.iter_files():
                    with res.open(fileinfo.name) as file_in:
                        with open(os.path.join(dirpath, fileinfo.name), "wb") as file_out:
                            file_out.write(file_in.read())
    else:
        print('File', args.path, 'not found', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
