# Euserv续期脚本——selenium版本
这是鄙人学习python自动化测试的时候突发奇想,只是单纯的测试一下euserv的续期测试哈哈哈😁还真可以续期,本人测试过了,初步脚本已经写出来了,脚本会有所改进,还是有不少可以优化的地方的.请大佬指教指教,好菜ing✨

------

⚠️提醒：这里使用德鸡vps自己续期自己嘻嘻,全部环境使用较为干净的真实浏览器,较为安全,不过鉴于德鸡现在的负载,一键脚本安装请耐心等待~

### 脚本使用
#### 德鸡centos7 加入dns 获取ipv4访问能力 (如已经添加过了或者使用了WARP请忽略)
```
echo -e "search blue.kundencontroller.de\noptions rotate\nnameserver 2001:67c:2b0::4\nnameserver 2001:67c:2b0::6" > /etc/resolv.conf
```

##### 一键安装脚本(主要是selenium等环境的搭建和测试环境,执行一次就可,主要是测试使用环境是否能够运行)

> 目前只有centos版,其他待更新........... 支持多个账号

```shell
wget -N --no-check-certificate https://github.com/MTkej122/EUserv_extend/blob/main/Euserv.sh && chmod +x Euserv.sh && ./Euserv.sh
```

##### Chromedriver驱动下载

> 因为Chrome版本会更新这个需要手动复制linux驱动下载链接

点击 [驱动下载页面](http://chromedriver.storage.googleapis.com/index.html)根据此处输出的chrome版本(大版本一致即可如4515.159也能对应4515.107)复制链接并输入即可



![image-20210827085215986](https://gitee.com/liujie2021/imgre/raw/master/image-20210827085215986.png)



![](https://gitee.com/liujie2021/imgre/raw/master/Snipaste_2021-08-27_08-56-18.png)

![](https://gitee.com/liujie2021/imgre/raw/master/Snipaste_2021-08-27_08-46-45.png)

输入后 会出现vi编辑器来编辑py文件输入自己的TG机器人的ID与Token 以及自己的德鸡账号密码

> 具体操作: 输入i进入编辑模式然后将光标定位到XXX删除并修改使用方向键定位,输入完以后按Esc退出输入模式并输入:wq保存退出回车

![Xshell_wNa0XaM3Vk](https://gitee.com/liujie2021/imgre/raw/master/Xshell_wNa0XaM3Vk.png)



![Xshell_wrF633XUMQ](C:\Users\kuxiaojie\Documents\ShareX\Screenshots\2021-09\Xshell_wrF633XUMQ.png)









> 脚本分为windows版和linux无界面版

- euserv_test_linux.py
- euserv_test_win.py

这两个文件主要区别就是linux无界面,win是有界面的测试,vps可以使用宝塔或crontab计划任务运行一下命令:

```python
python3 euserv_test_linux.py
```

新增 TG 推送 机器人

```
# 通过@BotFather 申请获得
# 用户、群组或频道 ID
```

输入你的TG ID 和token

并输入输入你的德鸡邮箱或ID以及密码

![image-20210828165858010](https://gitee.com/liujie2021/imgre/raw/master/image-20210828165858010.png)

![](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210828165605.png)



根据自己的小鸡到期时间进行配置(只需要定时运行euserv_test_linux.py即可)

![QQ截图20210826120602.png](https://gitee.com/liujie2021/imgre/raw/master/QQ截图20210826120602.png)

![QQ截图20210826120608](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120608.png)

![QQ截图20210826120618](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120618.png)

![QQ截图20210826120625](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120625.png)

![QQ截图20210826120715](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120715.png)

### 说明

如何安装python3、selenium、Chrome、chromedriver等遇到相关问题请提[issues](https://github.com/huanngy/EUserv_extend/issues)
