print(" Project1 : DNA GC-Content & PCR Analyzer")

dna = input("Enter your DNA sequence (A, T, C, G): ").upper()

total_length = len(dna)
count_of_g_present = dna.count("G")
count_of_c_present = dna.count("C")

gc_percentage = ((count_of_g_present + count_of_c_present ) / total_length) * 100
print("\n Analysis Report ")
print("Sequence Length:", total_length, "base pairs")
print("GC Content:", gc_percentage, "%")

if gc_percentage > 50:
    print("RESULT: High GC content detected! This means it will require a higher melting temperature in PCR.")
else:
    print("RESULT: Normal to low GC content detected. This means that the standard PCR conditions will apply .")
