import json
import zmq
import time
from subprocess import check_output, CalledProcessError
from multiprocessing import Process, Manager


CURL_METRICS = ('{ '
	'"Host": "%{remote_ip}", '
	'"Port": "%{remote_port}", '
	'"Speed": %{speed_download}, '
	'"Bytes": %{size_download}, '
	'"Url": "%{url_effective}", '
	'"TotalTime": %{time_total}, '
	'"SetupTime": %{time_starttransfer} '
	'}')
size_download=1048576 #In Bytes
ftp_server="ftp://ftp.uma.es/mirror/remi/SRPMS/libmemcached-last-1.0.18-6.remi.src.rpm"
cmd = ["curl",
   "-o", "/dev/null",  # to not output filecontents on stdout
   "--fail",  # to get the curl exit code 22 for http failures
   "--insecure",  # to allow selfsigned certificates
   "--raw",
#   "--user","monroe:1234",
   "--silent",
   "--range", "0-{}".format(size_download - 1),
   "--write-out", "{}".format(CURL_METRICS),
   "{}".format(ftp_server)]#10MB.db
# Safeguard to always have a defined output variable
output = None
err_code = 0
start_curl = time.time()
output = check_output(cmd)

	# if e.returncode == 28:  # time-limit exceeded
	#     if expconfig['verbosity'] > 2:
	#         print ("Exceding timelimit {}, "
	#                "saving what we have").format(expconfig['time'])
	#     output = e.output
	# else:
	#     raise e
# Clean away leading and trailing whitespace
output = output.strip(' \t\r\n\0')
#print(timestamp=str(datetime.datetime.now())
print(output)
with open('result.json', 'w') as outfile:
    json.dump(output, outfile)
