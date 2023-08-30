from nand import NAND_gate
from and_gate import AND_gate
from or_gate import OR_gate

def XOR_gate(a, b):
  return AND_gate(NAND_gate(a, b), OR_gate(a, b))