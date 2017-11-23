# 生成器.send()


def gen():
    value = ''
    while True:
        receive = yield value
        if receive == 'exit':
            return
        value = 'got: {}'.format(receive)


g = gen()
g.send(None)
print(g.send('hello'))
print(g.send(123))
print(g.send('exit'))

