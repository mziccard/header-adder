#!/usr/bin/python

"""
  Copyright (c) 2015 Marco Ziccardi
  Licensed under the MIT license.
"""

import sys
import getopt
import os
import fnmatch
import tempfile
import shutil
import datetime

HELP_MESSAGE      = """Prepend header to all files of the specified extension in the specified directory

   -h, --help
   -i, --input-header= <input file for header>
   -e, --extension= <target files extension>
   -d, --directory= <root directory>
"""

DIRECTORY_ERROR   = "ERROR: path specified is not a directory"

FILE_HEADER_ERROR = "ERROR: file header path not found"

def main(argv):

  directory     = ""
  extension     = ""
  inputheader   = ""

  try:
    opts, args = getopt.getopt(argv,"hi:e:d:",["input-header=", "extension=", "directory="])
  except getopt.GetoptError:
    print HELP_MESSAGE
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print HELP_MESSAGE
      sys.exit()
    elif opt in ("-i", "--input-header"):
      inputheader = arg
    elif opt in ("-e", "--extension"):
      extension = arg
    elif opt in ("-d", "--directory"):
      directory = arg
  
  if directory == "":
    directory = os.path.dirname(os.path.realpath(__file__))

  if inputheader == "" or  extension == "":
    print HELP_MESSAGE  
    sys.exit(2)

  if (not os.path.isdir(directory)):
    print DIRECTORY_ERROR
    sys.exit(2)

  if (not os.path.exists(inputheader)):
    print DIRECTORY_ERROR
    sys.exit(2)

  # Open header file stream
  headerfile = open(inputheader, "r")
  # Replace the date placeholder
  headerstring = headerfile.read().replace('%DATE', datetime.datetime.now().isoformat())

  # Look for all files matching the extension 
  # in the specified directory
  for root, dirnames, filenames in os.walk(directory):
    for filename in fnmatch.filter(filenames, '*.'+extension):
      filepath = os.path.join(root, filename)
      codefile = open(filepath, "r")

      # Replace the filename placeholder
      headerstring = headerstring.replace('%FILENAME', filename)

      # Create temporary stream and append header first 
      # then code file
      temporary = tempfile.NamedTemporaryFile(delete=False)
      temporary.write(headerstring)
      temporary.write(codefile.read())

      # Close streams
      codefile.close()
      temporary.close()
  
      # Copy temporary file to old source file path
      shutil.copy(temporary.name, filepath)

if __name__ == "__main__":
   main(sys.argv[1:])  
