#!/bin/bash
cd project
aclocal
autoheader
automake -a
autoconf
./configure
make
make install
./uselessbin/mistery_foo
