# # source: https://xbplib.readthedocs.io/en/latest/user_doc/working_with_xbee_classes.html
# # https://xbplib.readthedocs.io/en/latest/user_doc/communicating_with_xbee_devices.html#communicatereceivedata
#
# local_xbee = XBeeDevice("COM1", 9600)
#
# local_xbee.open()
#
# # Instantiate a remote XBee device object.
# remote_xbee = RemoteXBeeDevice(local_xbee, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))
#
# # Read the device information of the remote XBee device.
# remote_xbee.read_device_info()
#
# # Get the operating mode of the device.
# operating_mode = local_xbee.get_operating_mode()
#
# #Closing connection
# # try:
# #     xbee.open()
# #
# #     [...]
# #
# # finally:
# #     if xbee is not None and xbee.is_open():
# #         xbee.close()

# Instantiate an XBee device object.
device = XBeeDevice("COM1", 9600)
device.open()

# Instantiate a remote XBee device object.
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A200XXXXXX"))

# Read data sent by the remote device.
xbee_message = device.read_data(remote_device)

# zakładam ze z GSM leci JSON zapisywany w pliku o jakiejść nazwie, pewnie trzeba będzie to uściślić. Do tego skryptu oddać logikę, zabezpiecznie przed zbyt dużymi JSONami i takimi w złych formatach