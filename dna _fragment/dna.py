import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequences.text")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1]) as csv_file:
        reader = csv.DictReader(csv_file)
        all_sequences = reader.fieldnames[1:]
        for row in reader:
            database.append(row)

    # TODO: Read DNA sequence file into a variable
    text = open(sys.argv[2], "r")
    dna = text.read()

    # TODO: Find longest match of each STR in DNA sequence
    strs_dna = {}
    for subsequence in all_sequences:
        longest_run = longest_match(dna, subsequence)
        strs_dna[subsequence] = longest_run

    # TODO: Check database for matching profiles
    for person in database:
        if match(all_sequences, strs_dna, person):
            print(person['name'])
            return
    print("NO MATCH")
    return
     
def match(all_sequences, strs_dna, person):
    for subsequence in all_sequences:
        if strs_dna[subsequence] != int(person[subsequence]):
            return False
        return True    

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run

main()
