from nand import NAND_gate
from not_gate import NOT_gate

def AND_gate(a, b):
  return NOT_gate(NAND_gate(a, b))