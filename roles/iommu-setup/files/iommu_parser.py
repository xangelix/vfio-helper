import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pci_buses")
parser.add_argument("iommu_groups")
args = parser.parse_args()

pci_buses = args.pci_buses.splitlines()
iommu_groups = args.iommu_groups.splitlines()

pci_buses_head = []

for a in pci_buses:
    if "\t" not in a:
        pci_buses_head.append(a)

pci_buses_ports = []
pci_buses_names = []

for a in pci_buses_head:
    pci_buses_ports.append(a[0:7])
    pci_buses_names.append(a[8:len(a)])

iommu_groups_with_names = iommu_groups

for i in range(len(pci_buses_head)):
    for j in range(len(iommu_groups)):
        if pci_buses_ports[i] in iommu_groups[j]:
            iommu_groups_with_names[j] = iommu_groups[j] + " " + pci_buses_names[i]

def groupFinder(a):
    return int(a[len("/sys/kernel/iommu_groups/"):-len(a[a.index("/devices/0000:"):len(a)])])

iommu_groups_with_names_sorted = iommu_groups_with_names
iommu_groups_with_names_sorted.sort(key=groupFinder)

for a in iommu_groups_with_names: print(a)
