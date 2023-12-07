#write functions here, don't add input('') statements here!
import re


def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    start_index = 0

    while start_index < len(dna_string1):
        index = dna_string1.find(dna_string2, start_index)

        if index == -1:
            break

        positions.append(index + 1)
        start_index = index + 1

    return tuple(positions)

      
        