#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
import sys
import fitz

from registration import Registration
from progress_bar import print_progress_bar
from tools        import pix_to_gray_image
from enapage      import ENAPage

pdf_dir = "../pdf/"

if len(sys.argv) == 1:
    src_name = pdf_dir + "small.pdf"
else:
    src_name = sys.argv[1]

mod_name = pdf_dir + "modelo.pdf"

name = os.path.basename(src_name)
name = os.path.splitext(name)[0]

dst_name = f'{name}-anotacoes.pdf'

#------------------------------------------------------------------------------#

mod_pdf = fitz.open(mod_name)
mod_pag = mod_pdf[0]
mod_pix = mod_pag.get_pixmap( dpi=300, colorspace="GRAY" )
mod_img = pix_to_gray_image( mod_pix )
mod_pdf.close()

reg = Registration( mod_img )

#------------------------------------------------------------------------------#

src_pdf = fitz.open(src_name)
dst_pdf = fitz.open()

L = src_pdf.page_count
print_progress_bar( 0, L, fill='*' )

for ii, src_pag in enumerate(src_pdf):

    src_pix = src_pag.get_pixmap( dpi=300, colorspace="GRAY" ) 
    src_img = pix_to_gray_image( src_pix )

    img = reg.transform( src_img )

    page = ENAPage( dst_pdf )
    page.insert_image( img )
    page.write_name ( "Nome Nome Nome Nome Nome Nome Nome" )
    page.write_score( 10*ii )
    page.draw_rects( True )

    page.commit()

    print_progress_bar( ii+1, L, fill='*' )

dst_pdf.save(dst_name)

#------------------------------------------------------------------------------#
