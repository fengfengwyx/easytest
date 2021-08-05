大家好，我是谭叔。

上期，我们一起[搭建了自动化测试的项目环境](http://mp.weixin.qq.com/s?__biz=MzI0ODUyMDA2MQ==&mid=2247486690&idx=1&sn=dcc6b30079cf436a01b88aed3c084427&chksm=e99ec0f0dee949e6daa46dad408657311217973f8af46dc556bad834933431955a1718ed0a32#rd)。

本期，开始讲原理——**搞懂原理，你将更轻松的吃透自动化测试**。

> tips：网盘和github，会根据文章顺序，同步更新代码。
>
> ![image-20210603110511351](http://pic.testtalking.com/testtalking/20210603110633.png)

## 简单认识unittest

创建一个test.py文件，引入unittest包

```import unittest
import unittest
```

![image-20210508165035063](http://pic.testtalking.com/testtalking/20210508165035.png)

长按ctrl+鼠标左键进入，可获取到unittest的一些信息：

1. unittest简介
2. **unittest的方法必须以test开头**（按规矩办事）
3. 官方文档链接（支持中文）
4. 一个简单的demo例子（可以粘贴出来运行）

<img src="http://pic.testtalking.com/testtalking/20210508165458.png" alt="image-20210508165458661" style="zoom: 67%;" />

## unittest原理

一说“原理“二字，很多人顿觉脑壳痛。

放心，我不会枯燥的讲原理。

贴一张图，换种方式给你讲明白。



<img src="http://pic.testtalking.com/testtalking/20210508170212.png" alt="image-20210508170212506"  />



回忆下你平时的工作场景。

你领到了一份功能测试任务，开始：

### 写测试用例（case：TestCase）

![image-20210508172155917](http://pic.testtalking.com/testtalking/20210508172155.png)

写测试用例，得考虑一些环境问题吧。

举个例子，一些用例需要在弱网环境下执行，你得设置测试环境（setUp），然后执行测试用例（run），执行完后，为了不影响其他用例执行，你得恢复测试环境（tearDown）。

so，套用到unittest上，TestCase的作用便是如此，它有三个组件：

- setUp：在执行测试用例之前，初始化环境

- run：执行测试用例

- tearDown：在执行测试用例之后，还原环境

### 整理测试用例之一（suite：TestSuite）

![image-20210508173524213](http://pic.testtalking.com/testtalking/20210508173524.png)

你在写测试用例的过程中，是按照模块写的吧。

举个例子，拿注册来说，你写了正常注册用例、异常注册用例，这两个用例需要集合到注册模块中，形成一个注册suite（集合）；

![image-20210508173312909](http://pic.testtalking.com/testtalking/20210508173312.png)

再拿登录来说，你写了正常登录用例、异常登录用例，这两个用例需要集合到登录模块中，形成一个登录suite（集合）。

而注册suite和登录suite，又可以整理成一个更大的用户鉴权的sutie（套件）。

so，套用到unittest上，TestSuite的作用便是如此——集合用例。

### 整理测试用例之二（loader：TestLoader）

![image-20210508173538890](http://pic.testtalking.com/testtalking/20210508173538.png)

你在写用例时，不会写一条用例就去执行一条用例，而是写完每一个模块的用例，放到用例集里面，等到执行。

TestLoader的作用便是加载 testcase（测试用例） 到 testsuite（测试用例集） 中，用以后续执行。

### 执行测试用例（runner）

![image-20210508173818943](http://pic.testtalking.com/testtalking/20210508173818.png)

到这一步，相信聪明的你，不用再让我举例说明了吧。

TextTestRunner执行测试用例（run 方法），将测试结果保存在 TextTestResult 中。

### 总结下来，简单四步走：

1. 编写测试用例TestCase（方法必须以test开头）
2. TestLoader将TestCase加载到TestSuite中
3. TextTestRunner运行测试集合TestSuite
4. 运行的结果会保存至TextTestResult中

现在想想，原理难吗？

下期，我们一起写出第一个自动化测试用例！

## 一如既往，做个总结

**01 不管是Python的unittest、pytest，还是Java的JUnit、TestNG，你按照平时做功能测试的思维去理解框架，一点也不复杂；**

**02 每一类框架都有它的特性，如何运用它们的特性完成你的自动化测试工作，是你在学习并掌握它们后该去思考和探索的。**

