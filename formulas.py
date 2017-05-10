import re
def parseFormula(formula):
    ''' input formula (string)
        returns dictionary of elements (keys)
        and atom count (integer)
        '''
    parsed_dict = {}
    elements = re.findall('[A-Z][a-z]?', formula)
    atom_count = re.findall('\d+', formula)
    # If the formula is perfectly explicit
    if len(elements) == len(atom_count):
        for i in range(len(elements)):
            if parsed_dict.get(elements[i], 0) == 0:
                parsed_dict[elements[i]] = int(atom_count[i])
            else:
                parsed_dict[elements[i]] += int(atom_count[i])
    # Else modifies the implicit formula explicitly
    # and recalls chemParser
    else:
        index_list = []
        single_elem = re.finditer('[A-Z][A-Z]|[a-z][A-Z]|[A-Z]$|[a-z]$', formula)
        single_elem2 = re.findall('[A-Z][A-Z]|[a-z][A-Z]|[A-Z]$|[a-z]$', formula)
        for index in single_elem:
            index_list.append(index.start())
        formula = list(formula)
        for i in range(len(index_list)):
            formula.insert(index_list.pop() + 1, "1")
        a = "".join(formula)
        return parseFormula(a)
    return parsed_dict
