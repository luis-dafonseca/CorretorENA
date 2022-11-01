#------------------------------------------------------------------------------#
# ./corretor/tools/Makefile





# List of all subdirectories
SUBDIRS=$(shell find -mindepth 1 -maxdepth 1 -type d -not -name __pycache__)

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~ *.pdf *.xlsx *.png

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__

#------------------------------------------------------------------------------#

all: $(PY_FILES)
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D all ;        \
	done




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
