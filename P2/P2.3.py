while True:
    #para evitar os problemas de conta quando usamos float e int no python, o troco antes era convertido para um int multiplicando ele por 100
    inp = float(input())
    inp = inp * 100
    int(inp)
    troco = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.50: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    while inp > 0:
        for i in troco.keys():
            while (i*100) <= inp:
                troco[i] += 1
                inp = inp - (i*100)
    print(f"""
NOTAS:
{troco[100]} nota(s) de R$ 100.00
{troco[50]} nota(s) de R$ 50.00
{troco[20]} nota(s) de R$ 20.00
{troco[10]} nota(s) de R$ 10.00
{troco[5]} nota(s) de R$ 5.00
{troco[2]} nota(s) de R$ 2.00

MOEDAS:
{troco[1]} moeda(s) de R$ 1.00
{troco[0.50]} moeda(s) de R$ 0.50
{troco[0.25]} moeda(s) de R$ 0.25
{troco[0.10]} moeda(s) de R$ 0.10
{troco[0.05]} moeda(s) de R$ 0.05
{troco[0.01]} moeda(s) de R$ 0.01


""")
    for i in troco.keys():
        #após o calculo de um troco, é preciso resetar o dicionário de trocos
        troco[i] = 0
