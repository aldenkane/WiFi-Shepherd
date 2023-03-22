# wb.py
# Get default gateway, then open in browser
# Author: Alden Kane

import webbrowser
import netifaces

# Need to validate IPv4 here
def getDefaultGateway():
    try:
        gws = netifaces.gateways()
        gateway_addr = gws['default'][netifaces.AF_INET][0]        
        return gateway_addr
    # Handle VPN Connected Case - Find something that looks like IPv4 Gateway
    except:
        print('No WiFi Connection or VPN in Use')
        gateway_addr_vpn = gws[2][0][0]
        return gateway_addr_vpn

def goToBrowser(addr):
    browser_str = 'http://' + str(addr)
    webbrowser.open(browser_str)
    return True

if __name__ == "__main__":
    usr_gateway_ip = getDefaultGateway()
    goToBrowser(usr_gateway_ip)

