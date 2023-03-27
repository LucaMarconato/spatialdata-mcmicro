# this file needs to be run from the host machine; it will update the docker image by copying ./scripts into the docker
# container, committing the changes and uploading the new image to docker hub

import argparse
import subprocess
import io
import pandas as pd
import re

parser = argparse.ArgumentParser(description='Update the docker image')
# parser.add_argument('-t', '--tag', help='new tag', required=True)
parser.add_argument('-c', '--container', help='container hash', required=True)
args = parser.parse_args()

##
# images = subprocess.check_output(['docker', 'image', 'ls']).decode('utf-8')
# print(images)
##
# lines = []
# for line in images.splitlines():
#     new_line = re.sub(' +', ' ', line).strip()
#     new_line = '\t'.join(new_line.split(' ')[:3])
#     lines.append(new_line)
# to_parse = '\n'.join(lines)
# print(to_parse)
# ##
# df = pd.read_csv(io.StringIO(to_parse), sep='\t')
# df = df[df['REPOSITORY'] == 'lucamarconato/spatialdata']
# print(df)
# ##
# tags = df['TAG'].tolist()
# if args.tag in tags:
#     # incrementally append a number to the tag
#     for i in range(10000):
#         new_tag = f'{args.tag}_{i}'
#         if new_tag not in tags:
#             break
#     else:
#         raise ValueError('No more tags available')
# else:
#     new_tag = args.tag

subprocess.check_output(['docker', 'cp', './scripts', f'{args.container}:/home/scripts'])
# subprocess.check_output(['docker', 'commit', args.container, f'lucamarconato/spatialdata:{new_tag}'])
subprocess.check_output(['docker', 'commit', args.container, f'lucamarconato/spatialdata'])
# subprocess.check_output(['docker', 'push', 'lucamarconato/spatialdata'])
