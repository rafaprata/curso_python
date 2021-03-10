times = ("FLAMENGO", "INTERNACIONAL", "ATLÉTICO MG", "SAO PAULO", "FLUMINENSE", "GRÊMIO", "PALMEIRAS", "SANTOS", "ATHLETICO PR", "BRAGANTINO", "CEARÁ", "CORINTHIANS", "ATLETICO GO", "BAHIA", "SPORT", "FORTALEZA", "VASCO", "GOIAS", "CORITIBA", "BOTAFOGO")

print(f'Os primeiros colocados foram: {times[:5]}')

print(f'Os times rebaixados foram: {times[-4:]}')

print(f'Times em ordem alfabética: {sorted(times)}')

print(f'O CORINTHIANS está na {times.index("CORINTHIANS")+1}ª posição')

