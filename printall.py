import pickle

def storeData(obj, filename):
    pickleFile = open(filename, 'wb')
    pickle.dump(obj, pickleFile)
    pickleFile.close()

def loadData(filename):
    pickleFile = open(filename, 'rb')
    obj = pickle.load(pickleFile)
    pickleFile.close()
    return obj


ips_checked = loadData("ips_checked.dat")
hikvision_camera_addr = loadData("hikvision_camera_addr.dat")
sonicWall_firewall_addr = loadData("sonicWall_firewall_addr.dat")
netgear_router_addr = loadData("netgear_router_addr.dat")
TR069_protocolDevice_addr = loadData("TR069_protocolDevice_addr.dat")
lighttpd_protocolDevice_addr = loadData("lighttpd_protocolDevice_addr.dat")
Huawei_router_addr = loadData("Huawei_router_addr.dat")
kangle_addr = loadData("kangle_addr.dat")
tplink_router_addr = loadData("tplink_router_addr.dat")
app_web_server_addr = loadData("app_web_server_addr.dat")


print("hikvision_camera_addr: ")
print(hikvision_camera_addr)


print("\n\n\n"+ "sonicWall_firewall_addr: ")
print(sonicWall_firewall_addr)


print("\n\n\n"+ "netgear_router_addr ")
print(netgear_router_addr)


print("\n\n\n"+ "TR069_protocolDevice_addr ")
print(TR069_protocolDevice_addr)


print("\n\n\n"+ "lighttpd_protocolDevice_addr ")
print(lighttpd_protocolDevice_addr)


print("\n\n\n"+ "Huawei_router_addr ")
print(Huawei_router_addr)

print("\n\n\n"+ "kangle_addr ")
print(kangle_addr)


print("\n\n\n"+ "tplink_router_addr ")
print(tplink_router_addr)


print("\n\n\n"+ "app_web_server_addr ")
print(app_web_server_addr)