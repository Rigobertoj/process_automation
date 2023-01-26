import subprocess

print("DIr")
result = subprocess.run(['dir'], stdout=subprocess.PIPE)
print(result.stdout.decode())
