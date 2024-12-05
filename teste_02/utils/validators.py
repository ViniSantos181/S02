def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido!")
    return cpf

def validar_telefone(telefone):
    if len(telefone) < 8 or not telefone.isdigit():
        raise ValueError("Telefone inválido!")
    return telefone