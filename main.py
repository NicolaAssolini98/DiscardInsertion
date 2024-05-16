import networkx as nx
import matplotlib.pyplot as plt

from cfg_build import build_cfg, print_cfg
from parser import obtain_function, clean_empty_line_and_comment
from analysis import  uncomputation_analysis, insert_discard

debug = True
"""
Recruitment:
I cannot write:
    if measure(bla):
i have to write:
    r = measure(bla)
    if r:
    

we don't consider inline function:
    q = h(qubit())
or
    p = h(x(q))
    
we have to write:
    t = qubit()
    q = h(t)
or
    t = x(q)    
    p = h(t)    
    
   
    
I must always assign when using quantum functions, apart from discard
all classical variables must be marked as ‘_’, so that they are ignored by the analysis
I consider a simplified cfg, so no break or continue
"""

file_path = 'txt_files/test_2'
# file_path = 'txt_files/test_entangled'
tag = '@guppy'
groups = obtain_function(file_path)
# for group in groups:
#     print('----')
#     print(group)



for group in groups:

    code = clean_empty_line_and_comment(group)
    name, cfg = build_cfg(code)
    print(name, ':')
    print_cfg(cfg, True)
    pairs = uncomputation_analysis(cfg)
    uncomputation = insert_discard(cfg, pairs)
    print('Uncomputation analysis results:')
    print('\t%s' % pairs)
    print('Discard must be added in these program points:\n\t%s' %
          uncomputation if len(uncomputation) > 0 else 'not discard function is needed')

    print('----------------')
    #break



# consider_discard = True
# print(entaglement_analysis(g, consider_discard))
