import csv
import numpy

# Import values
print("molecular_weights is starting import")
ifile = open("myengineerpkg/molecular_weights.csv","r")
csv_reader = csv.reader(ifile)
by_symbol = {}
by_name = {}
by_index = list()
for l in csv_reader:
    if(l[0] == "Symbol"):
        continue
    by_symbol[l[0]] = float(l[2])
    by_name[l[1]] = float(l[2])
    by_index.append(l[2])
by_atomic_number = numpy.array([0]+by_index)
del by_index
ifile.close()
print("import completed")

def by_formula(FORMULA):
    RESULT = 0.0
    COUNT = 0
    ELEMENT = ""
    for CHAR in FORMULA:
        if(CHAR.isdigit()):
            COUNT = COUNT*10 + int(CHAR)
        elif(CHAR.isupper()):
            if(ELEMENT != ""):
                RESULT += (COUNT if COUNT > 0 else 1) * by_symbol[ELEMENT]
            ELEMENT = CHAR
            COUNT = 0
        else:
            ELEMENT = ELEMENT + CHAR
    return RESULT + (COUNT if COUNT > 0 else 1) * by_symbol[ELEMENT]

by_formula = numpy.vectorize(by_formula)

def from_mole_frac(FORMULAS, MOLE_FRAC):
    return numpy.sum(MOLE_FRAC*by_formula(FORMULAS))

def from_mass_frac(FORMULAS, MASS_FRAC):
    return 1/numpy.sum(MASS_FRAC/by_formula(FORMULAS))