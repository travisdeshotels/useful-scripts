import copywriter.writer as writer
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='File needing a copyright block')
    parser.add_argument('-n', '--nostrip', help='Omit stripping existing copyright block', action='store_true')
    parser.add_argument('-v', '--verbose', help='Print trace level logging', action='store_true')
    return parser.parse_args()


writer.main(parse_args())
