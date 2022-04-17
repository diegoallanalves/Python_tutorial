#Abaixa a livraria
import re

# Crie um destino para uma frase
str1 = "Emma's luck numbers are 251 761 231 451666"

# Padrão para encontrar três dígitos consecutivos
string_pattern = r"\d{3}"

# Compilar o padrão de string para o objeto re.Pattern
regex_pattern = re.compile(string_pattern)

# Imprimir o tipo de padrão compilado
print(type(regex_pattern))
# Resultado <class 're.Pattern'>

# Encontre todas as correspondências na string um
result = regex_pattern.findall(str1)
print(result)
# Resultado ['251', '761', '231', '451']

# Sequência de destino dois
str2 = "Kelly's luck numbers are 111 212 415"

# Encontre todas as correspondências na segunda string reutilizando o mesmo padrão
result = regex_pattern.findall(str2)
print(result)
# Resultado ['111', '212', '415']