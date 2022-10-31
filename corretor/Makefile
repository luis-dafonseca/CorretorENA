#------------------------------------------------------------------------------#
# ./corretor/Makefile





# List of all subdirectories
SUBDIRS=$(shell find -mindepth 1 -maxdepth 1 -type d -not -name __pycache__)

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~ *.png *.pdf *.xlsx

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__

#------------------------------------------------------------------------------#

all: modelo.pdf exemplo.pdf exemplo.xlsx
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D all ;        \
	done

modelo.pdf:
	cp ../../pdf/modelo.pdf .

exemplo.pdf:
	cp ../../pdf/exemplo.pdf .

exemplo.xlsx:
	cp ../../pdf/exemplo.xlsx .

#------------------------------------------------------------------------------#

clean:
	-@ rm -vf ${CLEAN_FILES}
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D clean ;      \
	done

distclean: 
	-@ rm -vf ${DISTCLEAN_FILES}
	@ for D in ${SUBDIRS}; do   \
	  make -C $$D distclean ;   \
	done

.PHONY: all clean distclean

#------------------------------------------------------------------------------#
