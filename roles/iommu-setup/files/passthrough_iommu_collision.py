import argparse

parser = argparse.ArgumentParser()
parser.add_argument("iommu_passthrough_vga_groups")
parser.add_argument("iommu_host_vga_groups")
args = parser.parse_args()

iommu_passthrough_vga_groups = args.iommu_passthrough_vga_groups.splitlines()
iommu_host_vga_groups = args.iommu_host_vga_groups.splitlines()

collision = False
for passthrough in iommu_passthrough_vga_groups:
    for host in iommu_host_vga_groups:
        if passthrough == host: collision = True

print(collision)
