import os
import glob

assignments="assignments/*md"
osdir='os'

for osfile in glob.glob(os.path.join(osdir,'*')): os.remove(osfile)

for assignment in glob.glob(assignments):
  with open(assignment,'r') as fr:
    lines = fr.readlines()
  lines = [x.strip() for x in lines]
  for line in lines:
    if line.startswith('os:'):
      oses = [x.strip() for x in line[len('os:'):].split(',')]
      for o in oses:
        tname = o.replace('/','')
        fname = tname + '.md'
        fpath = os.path.join(osdir,fname)
        if not os.path.exists(fpath):
          with open(fpath,'w') as fw: 
            fw.write('---' + '\n')
            fw.write('layout: default' + '\n')
            fw.write('---' + '\n')
        with open(fpath,'a') as fw: 
          bnf = os.path.basename(assignment).replace('.md','')
          bnp = os.path.join('/', assignment.replace(' ','%20').replace('.md','.html'))
          fw.write('[' + tname +' @ ' + bnf + '](' + bnp +')' + '<br>\n')
