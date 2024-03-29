import speedtest

speed_test = speedtest.Speedtest()

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

download_speed = bytes_to_mb(speed_test.download())
print(f"Your Download Speed is {download_speed} MB")