#!/usr/bin/env python                                                                                                                                                       
import os, operator

nodes = {}
with open(r'masterData.csv') as f1:
    count = 1
    next(f1)
    for line in f1:
        n1, n2, w = line.strip().split(",")
        if n1 not in nodes:
            nodes[n1] = count
            count += 1
        if n2 not in nodes:
            nodes[n2] = count
            count += 1
            
with open('masterData.net', 'w') as f:
    f.write("*Vertices {}\n".format(len(nodes)))
    sorted_nodes = sorted(nodes.items(), key=operator.itemgetter(1))
    
    for node, value in sorted_nodes:
        f.write('{} "{}"\n'.format(value, node))
    
    f.write("*Edges\n")
    with open(r'masterData.csv') as f1:
        next(f1)
        for line in f1:
            n1, n2, w = line.strip().split(",")
            f.write("{} {} {}\n".format(nodes[n1], nodes[n2], w))