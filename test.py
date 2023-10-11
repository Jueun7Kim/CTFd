import subprocess

command = 'ping -c 4 0.0.1'

try:
    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    print(result)
except subprocess.CalledProcessError as e:
    print("오류 발생 : ", e)
