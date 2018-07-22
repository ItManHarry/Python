# pip的安装与使用

	- pip在python3.X的版本中已自动安装，使用命令：pip --version即可查看对应的版本。
	
	- pip安装软件
	
		基本安装：pip install '[软件包名]'
		
		安装指定的版本：pip install '[软件包名]==[版本号]'
	
	- pip删除软件包
	
		pip uninstall '[软件包名]'
		
	- 若要查看当前系统已安装的软件包及版本，则可使用list或者freeze指令：
	
		pip list/freeze
		
# 高级软件包的安装 - Anaconda工具

	Anaconda工具是一个包含300多种最受欢迎的科学、工程、数学和数据分析的Python软件
	组合包，以安装文件的形式在网络上发布，官网地址：
	
	https://www.anaconda.com/
	
	登录下载对应的Anaconda版本，安装完成后，即可使用conda命令安装Numpy和Matplotlib了
	
	conda install numpy
	
	conda install matplotlib
	
	注：以上命令需在管理员模式下执行（windows），Linux下使用root账号执行即可。
	
以下是绘制sin函数图形的程序：
	
```python
	import numpy as np
	import matplotlib.pyplot as pt
	x = np.arange(0,360)
	y = np.sin(x * np.pi / 180.0)
	pt.plot(x,y)
	pt.xlim(0.360)
	pt.ylim(-1.2,1.2)
	pt.title('Sin Function')
	pt.show()
```
# Python在线资源与支持

	- PypI网站
	
	网址：https://pypi.python.org
	