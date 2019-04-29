from __future__ import print_function
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from clint.arguments import Args
from clint.textui import puts, colored, indent
args = Args()
with indent(4, quote='>>>'):
puts(colored.blue('Aruments passed in: ') + str(args.all))
puts(colored.blue('Flags detected: ') + str(args.flags))
puts(colored.blue('Files detected: ') + str(args.files))
puts(colored.blue('NOT Files detected: ') + str(args.not_files))
puts(colored.blue('Grouped Arguments: ') + str(dict(args.grouped)))
print()
