
CC=gcc
CFLAGS= -Wall
MONTH= $(shell date '+%B')


all=strange_app

strange_app : strange_app.o ${MONTH}.o
	${CC} -o strange_app strange_app.c ${MONTH}.o


strange_app.o: strange_app.c
	${CC} -o strange_app.o -c strange_app.c ${CFLAGS}

${MONTH}.o: ${MONTH}.c strange_app.h
	gcc -o ${MONTH}.o -c ${MONTH}.c ${CFLAGS}

clean:
	rm -f *.o core
