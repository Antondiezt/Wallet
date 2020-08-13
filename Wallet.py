from constants import *

import subprocess


command = './derive -g --mnemonic="stable morning essence hybrid energy version sunny keen paddle refuse box naive survey cousin interest" --cols=path,address,privkey,pubkey --coin=eth --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

print(output)

import json
keys = json.loads(output)