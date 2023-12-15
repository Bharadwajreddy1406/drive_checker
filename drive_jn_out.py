import os, string, time
from ctypes import windll


def devices_in():
    devices = []
    deviceBit = windll.kernel32.GetLogicalDrives()
    for name in string.ascii_uppercase:  # The uppercase letters 'A-Z'
        if deviceBit & 1:
            devices.append(name)
        deviceBit >>= 1
        # print(devices)
    return devices


def list_folders(drive):
    folder_paths = []
    for root, _, files in os.walk(drive + ":\\"):
        for folder in files:
            folder_path = os.path.join(root, folder)
            folder_paths.append(folder_path)
    return folder_paths


def look_for_devices():
    now = devices_in()[1:]
    print('Detecting...')
    time.sleep(2)
    add_device = [i for i in devices_in() if i not in now]
    # print(len(add_device)," is added devices")
    removed_device = [i for i in now if i not in devices_in()]

    if len(add_device):
        # print("There were %d" % (len(add_device)))
        for drive in add_device:
            print("The drive added: %s." % drive)

    elif len(removed_device):
        # print("There were %d" % (len(removed_device)))
        for drive in removed_device:
            print("The drive removed : %s." % drive)


if __name__ == '__main__':

    while True:
        look_for_devices()

