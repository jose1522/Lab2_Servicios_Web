import netifaces

def getIP():
    ip = "0.0.0.0"
    if 'lo0' in netifaces.interfaces():
        ip = netifaces.ifaddresses('lo0')[netifaces.AF_INET][0]['addr']
    elif 'eth0' in netifaces.interfaces():
        ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    return ip

def getGatewayIP(offset=1):
    localIP = getIP()
    default_gateway = ".".join(localIP.split(".")[:3])+"."+str(offset) if localIP != "0.0.0.0" else localIP
    return default_gateway