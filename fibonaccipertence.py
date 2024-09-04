def fibonacci(n):
  fib_seq = [0,1]
  while fib_seq[-1] < n:
    valor_seguinte = fib_seq[-1] + fib_seq[-2]
    fib_seq.append(valor_seguinte)
  return fib_seq

def pertence_a_fibonacci(numero):
  fib_seq = fibonacci(numero)
  if numero in fib_seq:
    return f"O n�mero {numero} pertence � sequ�ncia de Fibonacci."
  else:
    return f"O n�mero {numero} n�o pertence � sequ�ncia de Fibonacci."


numero = int(input("Digite um n�mero: "))
resultado = pertence_a_fibonacci(numero)
print(resultado)
