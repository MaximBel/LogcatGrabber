from ppadb.client import Client

def dump_logcat_by_line(connect):
    file_obj = connect.socket.makefile()
    while True:
        print("Line: {}".format(file_obj.readline().strip()))

    file_obj.close()
    connect.close()

client = Client()
device = client.device("4c9a5ecc")
device.shell("logcat", handler=dump_logcat_by_line)