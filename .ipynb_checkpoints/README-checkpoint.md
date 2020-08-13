## Wallet
- Cloning and installing your hp-wallet-derive into your into your folder:
git clone https://github.com/dan-da/hd-wallet-derive
cd hd-wallet-derive
php -r "readfile('https://getcomposer.org/installer');" | php
php -d pcre.jit=0 composer.phar install


- Use the pip install command to download and install the web3.py module.
pip install web3

## HD Wallet Derive
- Create the shortcut
ln -s hd-wallet-derive/hd-wallet-derive.php derive

- Add the mnemonic keys by running
/derive -g --mnemonic="INSERT MNEMONIC HERE" --cols=path,address,privkey,pubkey --coin ETH
/derive -g --mnemonic="INSERT MNEMONIC HERE" --cols=path,address,privkey,pubkey --coin BTC

- Run ./derive to check it works

- Deriving the wallet keys
import subprocess

command = './derive -g --mnemonic="stable morning essence hybrid energy version sunny keen paddle refuse box naive survey cousin interest" --cols=path,address,privkey,pubkey --coin=eth --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

print(output)

import json
keys = json.loads(output)