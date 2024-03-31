def disamvowel(string_):
    '''
    parameter
    string_: str
    output
    return str
    '''
    vokal = 'aiueoAIUEO'
    for s in string_:
        if s in vokal:
            string_ = string_.replace(s, "")
    return string_


print(disamvowel("hallo INI LOL"))
