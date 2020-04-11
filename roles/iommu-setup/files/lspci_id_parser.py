import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lspci_binded")
parser.add_argument("vga_passthrough_buses")
args = parser.parse_args()

lspci_binded = args.lspci_binded.splitlines()
vga_passthrough_buses = args.vga_passthrough_buses.splitlines()

pci_ids = []

for bus in lspci_binded:
    for vga_passthrough_bus in vga_passthrough_buses:
        if vga_passthrough_bus in bus:
            pci_ids.append(bus[bus.rindex("[") + 1:bus.rindex("]")])

out = ""
for id in pci_ids:
    out += id + ","

out = out[0:len(out) - 1]
print(out)
