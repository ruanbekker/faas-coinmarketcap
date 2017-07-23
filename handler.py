import sys
import json
import requests

market_list =  [
    'antshares', 'ark', 'asch', 'bitbay', 'bitcoin', 'bitcoindark', 'bitconnect',
    'bitdeal', 'bitshares', 'blackcoin', 'blocknet', 'burst', 'byteball', 'bytecoin-bcn',
    'chaincoin', 'clams', 'cloakcoin', 'counterparty', 'crown', 'dash', 'decent',
    'decred', 'digibyte', 'digitalnote', 'dogecoin', 'e-coin', 'e-dinar-coin',
    'earthcoin', 'eb3-coin', 'elastic', 'emercoin', 'energycoin', 'ethereum', 'expanse',
    'factom', 'faircoin', 'firstcoin', 'gamecredits', 'golos', 'gridcoin', 'groestlcoin',
    'gulden', 'heat-ledger', 'infinitecoin', 'iocoin', 'ion', 'iota', 'komodo', 'leocoin',
    'library-credit', 'lisk', 'litecoin', 'luckchain', 'lykke', 'megacoin', 'monacoin',
    'monero', 'monetaryunit', 'mooncoin', 'mysterium', 'namecoin', 'nav-coin', 'nem',
    'neoscoin', 'nexus', 'novacoin', 'nxt', 'omni', 'particl', 'peercoin', 'peerplays-ppy',
    'pivx', 'potcoin', 'qtum', 'quark', 'radium', 'reddcoin', 'ripple', 'rubycoin', 'salus',
    'shift', 'siacoin', 'sibcoin', 'skycoin', 'spreadcoin', 'steem', 'stellar', 'stratis', 'syscoin',
    'ubiq', 'verge', 'vertcoin', 'viacoin', 'voxels', 'waves', 'worldcoin', 'ybcoin', 'zcash', 'zcoin'
]

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if __name__ == "__main__":
    market_name = get_stdin().split()[0]
    if market_name not in market_list:
        print('Market Name: ' + market_name + ' does not exist')
    else:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/' + market_name + '/?convert=USD').content
        data = json.loads(r)[0]
        print(json.dumps(data, indent=4))
