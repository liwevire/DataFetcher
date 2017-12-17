f = open('test.txt', 'a')
f.writelines("test1");
f.writelines("test2");
f.close()

g = open('test.txt', 'a+')
g.writelines("testAgain1");
g.writelines("testAgain2");
g.close()