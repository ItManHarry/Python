import sys
from sys import argv
print('-' * 80)
#本地字节指示符 - 大端模式返回big，否则返回little
print(sys.byteorder)
#Python相关的版权信息
print(sys.copyright)
#Python解释器在磁盘上的存放路径
print(sys.executable)
#当前系统保存文件使用的字符集
print(sys.getfilesystemencoding())
#Python整数支持的最大值
print(sys.maxsize)
#Python解释器所在的平台
print(sys.platform)
#Python解释器的版本信息
print(sys.version)
#Python主解释器的版本号
print(sys.winver)
print('-' * 80)
print(len(argv))
for arg in argv:
    print(arg)
sys.path.append('e:\\tmp')
import hello   