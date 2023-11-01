import typing


class DNAAnalyser:
    REPORT_MAPPING_FILENAME = "codon.tsv"

    def _read_codon_mapping(self) -> dict:
        """Reads the codon mapping file and returns a dictionary with codons as keys and amino acids as values."""
        mapping = {}
        with open(self.REPORT_MAPPING_FILENAME, "r") as file:
            for line in file:
                codon, amino_acid = line.strip().split()
                mapping[codon] = amino_acid
        return mapping

    def get_amino_acids_report(self, dna_sequence: str) -> typing.Dict[str, int]:
        """
        Returns a dictionary with amino acids as keys and their count as values.
        """
        report = {}
        mapping = self._read_codon_mapping()

        # check if the dna sequence's length is a multiple of 3
        if len(dna_sequence) % 3 != 0:
            print("Warning: The dna_sequence length is not a multiple of 3!")
            dna_sequence = dna_sequence[
                : -(len(dna_sequence) % 3)
            ]  # trim the sequence to make it a multiple of 3

        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i : i + 3]
            amino_acid = mapping.get(codon)
            if amino_acid:
                report[amino_acid] = report.get(amino_acid, 0) + 1

        return report
