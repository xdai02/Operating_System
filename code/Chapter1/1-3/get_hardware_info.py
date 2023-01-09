import psutil

print("Number of CPUs (physical): %d" % psutil.cpu_count(logical=False))
print("Number of CPUs (logical): %d" % psutil.cpu_count(logical=True))
print("CPU time (user): %f" % psutil.cpu_times().user)
print("CPU time (system): %f" % psutil.cpu_times().system)
print("CPU time (idle): %f" % psutil.cpu_times().idle)