import argparse

parser = argparse.ArgumentParser()
parser.add_argument("iommu_groups")
parser.add_argument("passthrough_vga_bus")
args = parser.parse_args()

iommu_groups = args.iommu_groups.splitlines()
passthrough_vga_bus = args.passthrough_vga_bus

target_iommu_groups = []

for group in iommu_groups:
    if f"0000:{passthrough_vga_bus[0:5]}" in group:
        target_iommu_groups.append(group)

for a in target_iommu_groups:
    start = a.index("/devices/0000:") + len("/devices/")
    stop = start + 12
    print(a[start:stop])
