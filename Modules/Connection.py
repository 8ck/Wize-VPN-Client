import openvpn_api.vpn, json, os

def Open():
    try:
        with open(os.getcwd() + "\Configuration.json", 'r') as f:
            OpenCON = openvpn_api.vpn(json.loads(f.read())['ip'], json.loads(f.read())['port']).connect()
            # with OpenCON.connection():
            #     return True
    except Exception as e:
        return False

