from cpf_cnpj import Documento
from validate_docbr import CNPJ, CPF

# cpf_um = cpf("15398745687")

# print(cpf_um)

# fatia1 = cpf[:3]
# fatia2 = cpf[3:6]
# fatia3 = cpf[6:9]
# fatia4 = cpf[9:11]

# cpf_formato = "{}.{}.{}-{}".format(fatia1, fatia2, fatia3, fatia4)

# print(cpf_formato)

exemplo_cnpj = "35379838000112"
cpf_um = "15398745687"


documento = Documento.cria_documento(exemplo_cnpj)

print(documento)
