import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lspci_knn_vga")
args = parser.parse_args()

acc = args.lspci_knn_vga.splitlines()

for a in acc: print(a[0:7])
