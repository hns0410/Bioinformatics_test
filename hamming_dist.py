"""Script to find Hamming distance"""
#Himanshu Sharma 11/08/14
#For learning git and for fun

def hammingdist(str1,str2) :

    count = 0

    for seq in range(0,len(str1)):
        if str1[seq] != str2[seq]:
            count += 1


    return count


print hammingdist('TGGACCTCCAATACTGGACGTTGAGTATCTTCTATGGGTTGAAGGCGCTGGAAAGAGGATCTGTGACGTCGAATGGGTCACAGCGCGCCCATTTAGATGACCGCAAGCGGGCGATCTTCGTGACATCGTGACATTACTGTGAATCGTTGCTGAGCGTGTATACGCCTCATGTTCCGCGTCGAAGTCTTATAGCCTTTAGTTGGCGCAGGTGGTGGTAGCATATAGCAGGGTAGGACCCTTTCATGACACATCCTTCGGCGAGCCAATAAAAAGTGGCTCGAGCTTATGCGCGTTTTGAAACTCGCGAGCGCGCATTAGAGGAAGCCCGTGGGGATTGCACTATGCTAGAAGTGGGAAAGGGGCTATCACCAAGTTGGATGAGAGCATGGATAGCGGGTTCGACGCGAAGTCAGCTTAAGTGACTAGTGCAGCTATGTAAGGCGCCCACGTCGGTTATCGCAATACTTCCCGTAATTTCGGCGCCGGCGACCTACGAAGATGGAGTCGTCGAGACTGATAAATGATTAATGAGGCCTTTACCAAGTGATGTCCGACGGATCTTCGCCAGCGCTAAATGCATGAAGTTTGATACCTATGTGACACATGGGTTTCCTATACAACGGAACACCAGTGACACGTGTGATACATTCATGAGATTTTCTAGGCTACCCTACAGGTCGGTTTATATGGGGCCGAGGAGGACCTAACGGCCAAGGTATGTAAAAAATACTGGACGACATCCAAGTGGCATAGTCAATGACAGACCTTAGCAACTGGACGGCGTTTGTTTAAGCGACGGGATTGAACAACCTCACTACTCATGAATGTGCTGAAGGACGGAGAATGATGGAAAGCGAAGTAATCAGTATAAGCGGAAATGGTCTGGTTGTGCCACGTTAACGGTATCGATCCAATATCATAAACAGGGTTACTAGCCGAGAGAGTCCATGGATACCTCTGTTTACCGCTGAG','GCCATCACAAATACTCTCCGTGCGGTTTCGAATATCAGGACACGTATCTTCGACAGGGGGCTCGGACGATTTTTTTAACGCAGAGAAAATATTGACATAACCTGAATCGTAGGTATTAGACGACCAATCGAAACCATCCCGAACTATTGCATAGCCTCTACGCGCCTTTCGCCTAAGTTCAAAGACTAATGACCTGTAAGTTGTGCAGCCGGTATTGTCCTATAGCAGTCTAGTACGGTTTAGTGAAACATCCTTCAGCGCTACCATAATCAGAGGCAGTAGCTGTGATCCATCGGCTAACTGGCAAGCGTACATACCCACAAGCTCAGGAGGAAGGCTGGCTGGTATTAGATTGATATCCGGATCTTTCATCTAGTCTGCGCGATAGCTTAGCCGACTCGGCGTGGAAAAAGCTTGGGTGAGGAATGCCCCGGGTTTCGGAGACGACGTCGCATATAGCGCGACATCAAGGAATTGGGGCACCGCCGCCTTTTGGTTACCGGGTTCAATAGGATAACAAGTGATTAATTAGGCCTGGAGGCCGGGGTGTATAATATATGGCCTCCTGAGCCCAATTTGTGATGGTTGGTTAAAATGTGCCCTACCGCTTTCCGAGAAAGGGGCACACCAGGCCGTCATGACGATCATGCAGAAGGTGTTCCGTGCTTCCCTACAGTGCAGTGCTTACAGACCACTGGAGGGCCTCTTAGATACGGTCTGTAAATTAGCGTGGCAGACTTCAAATTGGGGTACCTATCGGTATCCTATAACAAGATGATGGAATACGGTTAATGGACGACCATATTCGATTGCGGTTCGCATGAAAGCGAGTATTAAGGGTTAATGCTCGAAACCCACGCAATCCGTAAGAAGTAAAATCCTCTCATTGCTCGATTGTACCACTACCGCTTTAGTAAGGGATATCGCGATACAGTTACCAAGAATAACTACGTTAAGCGCATGGCTCGATAT')
