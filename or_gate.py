from nand import NAND_gate

def OR_gate(a, b):
  return NAND_gate(NAND_gate(a, a), NAND_gate(b,b))