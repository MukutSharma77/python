'''Transcribe to mRNA
Transcribe the given DNA strand into corresponding mRNA - a type of RNA, that will be formed from it after transcription. DNA has the bases A, T, G and C, while RNA converts to U, A, C and G respectively.
Examples
dna_to_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"
dna_to_rna("CGATATA") ➞ "GCUAUAU"
dna_to_rna("GTCATACGACGTA") ➞ "CAGUAUGCUGCAU"
Notes
Transcription is the process of making complementary strand.
A, T, G and C in DNA converts to U, A, C and G respectively, when in mRNA.
'''

string="ATTAGCGCGATATACGCGTAC"
str_=''
for i in string:
    if i=='A':
        str_+='U'
    elif i == 'T':
        str_ += 'A'
    elif i == 'G':
        str_ += 'C'
    elif i == 'C':
        str_ += 'G'
    else:
        str_+=i

print(str_)