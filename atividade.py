import itertools

def gerar_anagramas(palavra):
  """
  Gera todos os anagramas de uma palavra.

  Args:
    palavra: A palavra da qual gerar os anagramas.

  Returns:
    Uma lista de strings, onde cada string é um anagrama da palavra.
  """
  letras = list(palavra)
  anagramas = [''.join(p) for p in itertools.permutations(letras)]
  return anagramas

# Exemplo de uso
palavra = "Marcelo"
anagramas = gerar_anagramas(palavra)
print(f"Anagramas de '{palavra}': {anagramas}")