import pandas as pd
import sys

file_path = sys.argv[1]

df = pd.read_csv(file_path, sep = '\t', header = 0)

pathogenic = df[df['RENOVO_Class'].str.contains('Pathogenic')] 

clinvar = df[(df['CLNSIG'].str.lower().str.contains('pathogenic')) & 
    (df['Otherinfo10'] == 'PASS')]

patho_and_clinvar = pathogenic.merge(clinvar, how = 'outer').sort_values(by = 'PL_score', ascending = False)

patho_and_clinvar.to_csv(f'{file_path[:-4]}_cleaned.txt', sep='\t', index=False)