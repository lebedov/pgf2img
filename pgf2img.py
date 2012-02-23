#!/usr/bin/env python

"""
Convert PGF files to an image file using pdflatex (from
texlive) and convert (from ImageMagick).
"""

import os, sys, shutil, tempfile, time, subprocess, string

def __find_exec(executable):
    '''Try to find an executable in the system path.'''

    if os.path.isfile(executable):
        return executable
    else:
        paths = os.environ['PATH'].split(os.pathsep)
        for p in paths:
            f = os.path.join(p, executable)
            if os.path.isfile(f):
                return f
        return ''

def __check_for_exec(executable, msg):
    '''Exit on error if the specified executable cannot be
    found. Otherwise, return the path to the executable.'''

    path = __find_exec(executable)
    if path == '':
        print msg
        sys.exit()
    else:
        return path
    
def __run_cmd(cmd, msg, cwd=None, wait=30):
    '''Run a system command; display an error message if it returns a
    nonzero exit code or it stalls for more than the specified number
    of seconds.'''

    dev_null = open('/dev/null', 'w')
    p = subprocess.Popen(cmd, stdout=dev_null, stderr=dev_null, shell=True, cwd=cwd)
    tic = time.time()
    while p.returncode == None and time.time() < tic+wait:
        try:
            p.poll()
        except KeyboardInterrupt:
            print 'manually killing command %s' % cmd
            p.kill()
            sys.exit(1)
    if p.returncode == None:
        print 'killing stalled command %s ' % cmd
        p.kill()
    if p.returncode < 0:
        print msg
        sys.exit(1)

# Check for required executables:
PDFLATEX = __check_for_exec('pdflatex', 'cannot find pdflatex')
CONVERT = __check_for_exec('convert', 'cannot find convert')
RM = __check_for_exec('rm', 'cannot find rm')

# Used to redirect program output to /dev/null:
redirect_output = ' 1>/dev/null 2>&1'

# Defaults:
default_template = string.Template("""
\\documentclass[10pt]{standalone}
\\usepackage{amsmath,amssymb,amsbsy,amsfonts,amsthm}
\\usepackage{cmbright}
\\usepackage{tikz}
\\usetikzlibrary{shapes}
\\usetikzlibrary{shapes.multipart}
\\usetikzlibrary{shadows}
\\usetikzlibrary{arrows}
\\usetikzlibrary{positioning}
\\pagestyle{empty}
\\begin{document}
${body}
\\end{document}
""")
default_density = 200

def pgf2img(input_filename, output_filename,
            template=default_template, density=default_density):
    """Convert a PGF/TikZ file to an image file.

    Parameters
    ----------
    input_filename : str
        Name of input PGF/TikZ file. The file must contain a
        tikzpicture environment.
    output_filename : str
        Name of output file. The image format is determined
        by the filename extension.
    template : str
        LaTeX template used to generate image.
    density : int
        Output image density (in DPI).

    """

    # Open the input file:
    try:
        input_file = open(input_filename, 'r')
    except IOError:
        print 'error opening input file %s' % input_filename
        sys.exit(1)
    else:
        input_data = ''.join(input_file.readlines())

    # Combine the template and input file:
    temp_data = template.substitute(body=input_data)

    # Write the output to a temporary LaTeX file:
    try:
        temp_dirname = tempfile.mkdtemp()+os.sep
    except IOError:
        print 'error creating temporary directory %s' % temp_dirname
        sys.exit(1)
    else:
        temp_latex_filename = temp_dirname + 'temp.tex'

    try:
        temp_latex_file = open(temp_latex_filename,'w')
    except IOError:
        print 'error opening temporary LaTeX file %s' % temp_latex_filename
        sys.exit(1)
    else:
        temp_latex_file.writelines(temp_data.splitlines(True))
        temp_latex_file.close()

    # Process the temporary file with pdflatex:
    __run_cmd(PDFLATEX + ' ' +
              temp_latex_filename, 
              'error running pdflatex', temp_dirname)

    # If the specified output file format is pdf, there is no need to run
    # the generated file through convert:
    temp_latex_basename = os.path.splitext(temp_latex_filename)[0]
    temp_pdf_filename = temp_latex_basename + '.pdf'
    output_ext = os.path.splitext(output_filename)[1]
    if output_ext.lower() == '.pdf':
        shutil.move(temp_pdf_filename, output_filename)
    else:
        __run_cmd(CONVERT + ' -trim -density ' + str(density) + ' ' +
                  temp_pdf_filename + ' ' +
                  output_filename, 
                  'error running convert')

    # Clean up the temporary work directory:
    __run_cmd(RM + ' -rf ' + temp_dirname, 
              'error removing temporary directory %s' % temp_dirname)


