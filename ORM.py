# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-01 11:47  
# software  :python_learn
import aiomysql
import asyncio
import logging

# 连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务
@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global _pool
    _pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', '3306'),
        user=kw['user'],
        passwdword=kw['password'],
        db=kw[db],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

# 要执行SELECT语句，我们用select函数执行，需要传入SQL语句和SQL参数：

@asyncio.coroutine
def select(sql,args,size=None):
    log(sql, args)
    global _pool
    with (yield from _pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returnd: %s',% len(rs))
        return rs

@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected