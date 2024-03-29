from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            return ValueError('Documento inválido')


class DocCpf():
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        return self.format_cpf()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj():
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido')

    def __str__(self):
        return self.format_cnpj()

    def valida(self, documento):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(documento)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
