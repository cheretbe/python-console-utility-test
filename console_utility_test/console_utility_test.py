#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Command line utility test"""

import humanfriendly


def main():
    size_in_bytes = 324634231
    print("{0} bytes is {1}".format(size_in_bytes,
          humanfriendly.format_size(size_in_bytes, binary=True)))


if __name__ == "__main__":
    main()
