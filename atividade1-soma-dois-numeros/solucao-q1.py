def soma(a, b):
    if a < 1 or a > 1000:
        raise ValueError(f"Valor de 'a' está fora do intervalo permitido: {a}. Deve ser entre 1 e 1000.")
    if b < 1 or b > 1000:
        raise ValueError(f"Valor de 'b' está fora do intervalo permitido: {b}. Deve ser entre 1 e 1000.")
    
    return a + b

print(soma(0, 5))