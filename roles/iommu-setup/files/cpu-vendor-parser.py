import argparse

parser = argparse.ArgumentParser()
parser.add_argument("vendor_string")
args = parser.parse_args()

acc = args.vendor_string

vendor_key = {
    "AMD" : "AMD",
    "Amd" : "AMD",
    "amd" : "AMD",
    "INTEL" : "INTEL",
    "Intel" : "INTEL",
    "intel" : "INTEL"
}

out = "UNK"
for vendor in vendor_key:
    if vendor in acc:
        out = vendor_key[vendor]

print(out)
