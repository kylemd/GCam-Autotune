import argparse
import libValuesAPI
import fridaLibPatcher
import fridaMemoryMonitor

print('Welcome to the AI autopatcher.')
print('Arguments:\n')
print('textfile: loads libparams.json from root dir\n')
print('patcher|monitor: start autopatching or monitor lib values')
    
    
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')
textfile = subparser.add_parser('textfile')
operation = subparser.add_parser('operation')

textfile.add_argument('textfile', type=str, required=False)
operation.add_argument('patcher', type=str, required=False)
operation.add_argument('monitor', type=str, required=False)
    
args = parser.parse_args()

if args.command == 'textfile':
    text = 'textfile'
    
if args.command == 'patcher':
    libvalues = libValuesAPI.GetLibValues('patcher',text)
    #fridaLibPatcher
elif args.command == 'monitor':
    libvalues = libValuesAPI.GetLibValues('monitor',text)
    fridaMemoryMonitor.watchInMemory(libvalues)