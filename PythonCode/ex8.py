# _*_  coding:utf-8 _*_.
print "." * 50
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight"
)
formatter2 = "%s %s %s %s"
print formatter2 % (
	"��Һã�",
	"���ǳ̹�ǰ��",
	"������ѧϰPyhon����",
	"���͡�����������"
)

print "����"
print "." * 50