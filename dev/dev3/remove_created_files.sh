#!/bin/bash
cd project
rm Makefile Makefile.in aclocal.m4 compile config.h config.h.in config.log config.status configure depcomp install-sh missing stamp-h1
rm -r autom4te.cache
rm -r uselessbin
cd src
rm Makefile Makefile.in
cd lib_foo
rm Makefile Makefile.in foo.o libfoo.a
rm -r .deps
cd ..
cd main
rm Makefile Makefile.in main.o mistery_foo
rm -r .deps
