import multiprocessing

bind = "127.0.0.1:8000"
workers = 1
#only one worker because then ill have to update the sessions in all
#workers = multiprocessing.cpu_count() * 2 + 1

#remember to set forwarded_allow_ips
#forwarded-allow-ips = "*"

