import psutil
import time

def net_usage():
    net_stat = psutil.net_io_counters()
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(1)
    net_stat = psutil.net_io_counters()
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

    return net_in, net_out

down_speed, up_speed = net_usage()
print("\n")
print("################# NET USAGE ##################\n")
print(f"UP: {up_speed} MB/s DOWN: {down_speed} MB/s")
print("\n")
print("##############################################\n")
    