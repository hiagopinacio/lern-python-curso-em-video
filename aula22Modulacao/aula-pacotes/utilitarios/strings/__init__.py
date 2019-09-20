def reverte(str):
    revertido = ""
    for c in range(len(str)-1,-1,-1):
        revertido += str[c]
    return revertido
