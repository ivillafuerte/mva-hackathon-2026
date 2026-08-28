from pathlib import Path
import platform
import sys

PRIVATE_VARIANTS = Path("/data/private/variants")
RESULTS = Path("/results")


def main():
    print("MVA Genomic Analysis Pipeline")
    print("=============================")
    print(f"Python:       {sys.version.split()[0]}")
    print(f"Architecture: {platform.machine()}")
    print()

    vcfs = list(PRIVATE_VARIANTS.glob("*.vcf.gz"))

    print(f"VCF files detected: {len(vcfs)}")

    for vcf in vcfs:
        print(f" - {vcf.name}")

    print()
    print(f"Results directory: {RESULTS}")


if __name__ == "__main__":
    main()
