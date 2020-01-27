"""Snakemake wrapper for Kallisto quant"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTQ files
fastq = snakemake.input.get("fastq")
assert fastq is not None, "input-> a FASTQ-file is required"
fastq = " ".join(fastq) if isinstance(fastq, list) else fastq

shell(
    "kallisto quant "  # Tool ##added -b and --single for sleuth
    "{extra} "  # Optional parameters
    "--threads={snakemake.threads} "  # Number of threads
    "--index={snakemake.params.index} "  # Input file
    "--output-dir={snakemake.params.outdir} "  # Output directory
    "{fastq} "  # Input FASTQ files
    "{log}"  # Logging
)
