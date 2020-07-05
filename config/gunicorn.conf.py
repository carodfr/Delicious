import multiprocessing

#bind = "127.0.0.1:8000"
bind = "unix:/run/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1

#remember to set forwarded_allow_ips
#forwarded-allow-ips = "*"

