# coding=utf-8

import redis
import time

def main(ip):
    # 连接数据库
    # client=redis.client.Redis(host='192.168.43.36', port=6379, db=0)
    client=redis.client.Redis(host=ip, port=6379, db=0)
    
    # 单个string
    result=client.set('Mark', 1001)
    print(result)
    age=client.get('Mark').decode()
    print(age)
	
    # 多个string
    student={'name':'zhangs', 'age':22}
    
    result=client.mset(student)
    # 返回bool值，是否设置成功
    print(result)
    print(client.mget(student))
    print(client.mget(['name', 'age', 'Mark']))
    
    # 删除操作
    client.delete('Mark')    
    d=client.delete('name','age')
    print(d)
    result=client.get('name')
    print(result)

    # 集合操作
    # sadd:将一个或多个成员元素加入到集合中，已经存在于集合的成员元素将被忽略；
    sets=('name', 'age', 'class', 'score')
    result=client.sadd('new_sets', *sets)
    print(result)
    
    # smembers()：判断成员元素是否是集合的成员；
    result=client.smembers('new_sets')
    word={x.decode() for x in result}
    print(word)
    for i in range(len(word)):
        print(word.pop())
    
    # srem()：用于移除集合中的一个或多个成员元素，不存在的成员元素会被忽略；
    result=client.srem('new_sets', 'class', 'score')
    print(client.smembers('new_sets'))
    time.sleep(5)

    
if __name__=="__main__":
    ip = input("请输入redis服务器IP：")
    main(ip)