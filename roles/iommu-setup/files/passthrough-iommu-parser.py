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

#for a in target_iommu_groups: print(a)

#print("---")

vfio_iommu_groups = []
for group in target_iommu_groups:
    vfio_iommu_groups.append(group[len("/sys/kernel/iommu_groups/"):-len(group[group.index("/devices/0000:"):len(group)])])

vfio_iommu_groups = set(vfio_iommu_groups)

for a in vfio_iommu_groups: print(a)


final = []
for group in iommu_groups:
    for vfio in vfio_iommu_groups:
        if f"/sys/kernel/iommu_groups/{vfio}/devices/" in group:
            final.append(group)

#for a in final: print(a)
