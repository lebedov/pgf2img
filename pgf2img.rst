.. -*- rst -*-

=======
pgf2img
=======

-----------------------------------------------
generate an image directly from PGF/TiKZ source
-----------------------------------------------

:Author: Lev Givon <lev@columbia.edu>
:Date: 2010-03-04
:Copyright: BSD
:Version: 0.01
:Manual section: 1

SYNOPSIS
========
**pgf2img** [*options*] \<*input pgf file*\> [*output image file*]

DESCRIPTION
===========
**pgf2img** transforms a LaTeX file containing a diagram specified using
PGF/TiKZ directly into a cropped image using **pdflatex** and the
**convert** command provided by ImageMagick. If no output file name is
specified, the output image is given the same basename as the input
file.

OPTIONS
=======
-h 
   Print usage statement.

-t \<template file\>             
   Specify template LaTeX file. By default, **pgf2img** uses a
   template that provides access to *AMS-LaTeX*.

-d \density
   Resolution (in DPI) of the output image.

NOTES
=====
The default output format is PNG; other formats supported by
ImageMagick can be requested by specifying an output file name with
the appropriate suffix.

SEE ALSO
========
**pdflatex**\(1), **convert**\(1)

BUGS
====
**pgf2img** doesn't clean up its temporary work files in the event
that it fails.
