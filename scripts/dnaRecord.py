#!/usr/bin/env python3
class DNARecord(object):
  # define class attributes
  sequence = 'ACGTAGCTGACGATC'
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster'

  # define methods
  def reverse_complement(self):
    replacement1 = self.sequence.replace('A', 't')
    replacement2 = replacement1.replace('T', 'a')
    replacement3 = replacement2.replace('C', 'g')
    replacement4 = replacement3.replace('G', 'c')
    reverse_comp = replacement4[::-1]
    return reverse_comp.upper()

  def get_AT(self):
    length = len(self.sequence)
    a_count = self.sequence.count('A')
    t_count = self.sequence.count('T')
    at_content = (a_count + t_count) / length
    return at_content

dna_rec_obj = DNARecord()
print('Created a record for ' + dna_rec_obj.gene_name + ' from ' + dna_rec_obj.species_name)
print('AT is ' + str(dna_rec_obj.get_AT()))
print('complement is ' + dna_rec_obj.reverse_complement())
