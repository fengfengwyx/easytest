大家好，我是谭叔。

本期重点解决上期遗留的问题——如何让电脑判定用例的执行结果。

解决问题的思路跟你做功能测试是一个道理，当你测试登录接口时，你得观察登录接口返回成功还是失败，以判断登录是否成功。

那么，做自动化测试时，如何让**程序判断执行结果是不是你想要的**？

## 简单判断

修改test_add_department_001和test_add_department_002用例，加上if else的判断。

```python
    def test_add_department_001(self):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 判断请求结果
        result = json.loads(result.text)
        if result['already_exist']['count'] == 0:
            print("{} 执行成功".format(self._testMethodName))
        else:
            print("{} 执行失败".format(self._testMethodName))


    def test_add_department_002(self):
        """重复新增T01学院"""
        # self.test_add_department_001() # 或者贴一段新增T01的请求代码ETReq.post
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 判断请求结果
        result = json.loads(result.text)
        if result['already_exist']['count'] == 1:
            print("{} 执行成功".format(self._testMethodName))
        else:
            print("{} 执行失败".format(self._testMethodName))
```

看看结果吧：

![image-20210530205113006](http://pic.testtalking.com/testtalking/image-20210530205113006.png)

这样，我们便构造了一个简单的if else断言方式，让程序走判断逻辑。

但，你可能意识到这么写，略有不妥——代码冗余，不好维护。

一般来说，我们会使用unittest的assert断言来解决问题。

## 使用断言

unittest中断言主要有三种类型：

1、布尔断言。即，要么正确，要么错误

2、比较断言。通过比较两个变量的值得出布尔值，要么比较正确，要么比较错误

3、其他断言。如断言列表、元组等，使用情况较少

如图所示，输入assert，编辑器会自动联想所有的断言。

![image-20210603172038206](http://pic.testtalking.com/testtalking/20210603172038.png)

针对本次接口自动化项目，我们使用简单的assertEqual（比较断言）。其他断言方式，你可以抽时间研究下，正确理解，根据自己的项目做合适的选择。

首先，去掉if else的判断部分。

![image-20210603171708115](http://pic.testtalking.com/testtalking/20210603171708.png)

添加上assertEqual：

```python
    def test_add_department_001(self):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 判断请求结果
        result = json.loads(result.text)
        # self.assertEqual(result['already_exist']['count'], 0) # 断言会失败
        self.assertEqual(result['already_exist']['count'], 1) # 断言会失败
```

![image-20210603172921091](http://pic.testtalking.com/testtalking/20210603172921.png)

在控制台，我们可以看到最终的结果——断言失败。

![image-20210603173031667](http://pic.testtalking.com/testtalking/20210603173031.png)

## 一如既往，做个总结

**接口断言，本质上很简单，不过在真实场景下，你得解析复杂的数据结构，得根据业务场景细分断言种类，如接口断言、数据库断言等等，这些略有难度，但上手后，你依旧能很快掌握。**