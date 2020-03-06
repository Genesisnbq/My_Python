# with 可以帮助处理异常
# 将异常与面向对象结合起来


class Testwith():
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has error %s' % exc_tb)


with Testwith():
    print('test is running')
    raise NameError('testNameError')  # 手动抛出异常
