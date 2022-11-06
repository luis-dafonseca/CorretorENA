#------------------------------------------------------------------------------#
# ./corretor/Makefile





# List of all subdirectories
SUBDIRS=$(shell find -mindepth 1 -maxdepth 1 -type d -not -name __pycache__ -not -name venv)

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~ *.png *.pdf *.xlsx

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__

#------------------------------------------------------------------------------#

all: exemplo-dados.xlsx  exemplo-modelo.pdf  exemplo-respostas.pdf
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D all ;        \
	done

exemplo-dados.xlsx:
	cp ../docs/example/exemplo-dados.xlsx .

exemplo-modelo.pdf:
	cp ../docs/example/exemplo-modelo.pdf .

exemplo-respostas.pdf:
	cp ../docs/example/exemplo-respostas.pdf .

#------------------------------------------------------------------------------#

clean:
	-@ rm -vf ${CLEAN_FILES}
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D clean ;      \
	done

distclean: 
	-@ rm -rvf ${DISTCLEAN_FILES}
	@ for D in ${SUBDIRS}; do   \
	  make -C $$D distclean ;   \
	done

.PHONY: clean distclean

#------------------------------------------------------------------------------#
