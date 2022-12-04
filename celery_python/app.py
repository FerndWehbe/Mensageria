from tasks import teste

result = teste.delay(4, 8)
print(result.id)
