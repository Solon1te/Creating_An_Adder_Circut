from nand import NAND_gate

def NOT_gate(a):
  if NAND_gate(a, a):
    return 1
  else:
    return 0