# _*_ coding:utf-8 _*_
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses !" % cheese_count
	print "You have %d boxes of crackers !" % boxes_of_crackers
	print "Man that is enough for a party !"
	print "Get a blanket.\n"
print "-" * 60
#ֱ�Ӵ��ݲ���
print "We just give parameters directly:"
cheese_and_crackers(20, 30)
print "-" * 60
#�������ݲ���
print "Or , we can user variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print "-" * 60
#���㴫�ݲ���
print "We can even do math inside of the method:"
cheese_and_crackers(10+20, 5+6)
print "-" * 60
#���ģʽ���ݲ���
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
print "-" * 60
#�û��������
param1 = raw_input("Amount of cheese > ")
param2 = raw_input("Amount of crackers > ")
cheese_and_crackers(int(param1), int(param2))