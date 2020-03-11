import redis

r = redis.StrictRedis(host="10.3.1.19", port=6379, password="PTzjOKOuGnwcmQ2r", db=0)
datet = '20191204'
#r.delete('list_gps_inout_time2')
list2 = r.lrange('list_gps_inout_time4',0,-1)
for row in list2:
    print(row.decode('utf-8') )