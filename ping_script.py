import subprocess
import platform

print('Type ip address which you want to ping: ')
host = input()

def ping(host):

    #par = '-n' if platform.system().lower == 'windows' else '-c'
    if [platform.system().lower == 'windows']:
        par = '-n'
	else:
        par = '-c'
        
    command = ['ping', '-n', '5', host]