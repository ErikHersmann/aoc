from collections import defaultdict
from lookup_tables import get_rna_codon_table, get_monoisotopic_mass_table
import re

NUCLEIC_ACID_BASE_COMPLEMENT_MAP = {"A": "T", "T": "A", "C": "G", "G": "C"}

tl_NUCLEIC_ACID_BASE_COMPLEMENT_MAP = str.maketrans(NUCLEIC_ACID_BASE_COMPLEMENT_MAP)


def format_answer_from_list(l: list):
    return " ".join([str(x) for x in l])


def count_dna_bases(string: str) -> list:
    """Solution to https://rosalind.info/problems/dna/"""
    d = defaultdict(int)
    for c in string:
        d[c] += 1
    return [d[key] for key in NUCLEIC_ACID_BASE_COMPLEMENT_MAP]


def dna_to_rna(string: str):
    return string.replace("T", "U")


def reverse_complement_of_dna(string: str):
    return string[::-1].translate(t_NUCLEIC_ACID_BASE_COMPLEMENT_MAP)


def calculate_rabbit_population(n: int, k: int):
    counts = [0, 1]
    for gen in range(1, n):
        counts[1], counts[0] = counts[0] * k, counts[0] + counts[1]
    return sum(counts)


def translate_rna_into_protein(string: str) -> str:
    table = get_rna_codon_table()
    protein = [table[string[idx : idx + 3]] for idx in range(0, len(string), 3)] + [
        "Stop"
    ]
    return protein[: protein.index("Stop")]


def calculate_protein_mass(string: str) -> float:
    table = get_monoisotopic_mass_table()
    return sum([table[c] for c in string])


def find_repeats_in_dna(string: str, motif: str):
    return [match.regs[0][0] + 1 for match in re.finditer(f"(?={motif})", string)]

def parse_fasta(string: str) -> list:
    pass

def splice_rna(string: str) -> str:
    table = parse_fasta(string)
    pass