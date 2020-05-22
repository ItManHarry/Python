from collections import ChainMap
import builtins
import os, argparse
print('-' * 80)
a = {'Kotlin':90,'Python':86}
b = {'Go':93,'Python':92}
c = {'Swift':89,'Go':87}
cm = ChainMap(a,b,c)
print('ChainMap : ', cm)
print('Python : ', cm['Python'])
print('Go : ', cm['Go'])
print('-' * 80)
my_name = 'Harry'
def test():
    my_name = 'Jack'
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    print(pylookup['my_name'])
    print(pylookup['len'])
test()    
print('-' * 80)
defaults = {'color':'Blue','user':'Harry'}
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])
print('-' * 80)