try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
config = {
	'description':'My First Python Project',
	'author':'Harry',
	'url':'URL to get it.',
	'download_url':'Where to download it.',
	'author_email':'jack_chengqian@163.com',
	'version':'0.1',
	'install_requaires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name':'FP',
}
setup(**config)