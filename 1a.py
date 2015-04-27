#!/usr/local/env python
import re

pdb_fn = raw_input("Enter PDB filename [test_ensemble.pdb]: ") or "test_ensemble.pdb"
fi = open(pdb_fn,"r")
ca_lines = [l for l in fi.readlines() if re.match("ATOM.* CA ",l)] 
