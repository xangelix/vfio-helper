import argparse
import pprint

#TODO: Major refactoring and readability changes
#TODO: Collision detection needs to not apply within buses

parser = argparse.ArgumentParser()
parser.add_argument("iommu_groups")
parser.add_argument("vga_buses")
parser.add_argument("passthrough_vga_bus")
args = parser.parse_args()

iommu_groups = args.iommu_groups.splitlines()
vga_buses = args.vga_buses.splitlines()

bus_key = {}

for vga_bus in vga_buses:
    for iommu_group in iommu_groups:
        if (vga_bus[0:2] in iommu_group) and (iommu_group not in bus_key.keys()):
            bus_key[iommu_group] = vga_bus

pprint.pprint(bus_key)

target_buses = []
for bus in bus_key:
    target_buses.append(bus[len("/sys/kernel/iommu_groups/"):-21])

pprint.pprint(target_buses)

out = True
if len(target_buses) != len(set(target_buses)): out = False
print(out)

hit_buses = []
for target_bus in set(target_buses):
    for iommu_group in iommu_groups:
        if target_bus == iommu_group[len("/sys/kernel/iommu_groups/"):-21]:
            hit_buses.append(iommu_group)

#pprint.pprint(hit_buses)


