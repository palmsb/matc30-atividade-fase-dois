# Atividade 1 — Soma de dois números inteiros

## Descrição

Função que recebe dois números inteiros e retorna a soma entre eles.

## Parâmetros

| Parâmetro | Tipo | Descrição       |
|-----------|------|-----------------|
| `a`       | int  | O primeiro valor |
| `b`       | int  | O segundo valor  |

## Retorno

Do tipo `int` retorna a soma de a e b.

## Restrições

- `1 ≤ a, b ≤ 1000`
- Caso algum valor esteja fora do intervalo, a função lança um `ValueError`

## Lógica da equipe

A solução usa o operador aritmético `+` diretamente, sem recorrer a funções prontas como `sum()`.  
A validação das restrições é feita com condicionais (`if`), garantindo que os valores de entrada estejam dentro do intervalo permitido antes de realizar o cálculo.
