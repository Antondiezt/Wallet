from constants import *

import subprocess


command = './derive -g --mnemonic="stable morning essence hybrid energy version sunny keen paddle refuse box naive survey cousin interest" --cols=path,address,privkey,pubkey --coin=eth,btctest --numderive=5 --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

print(output)

import json
coins = json.loads(output)