import os

# codepath = r'D:\python_work\QualityControl\testcode\src\test\java\ComputingTest.java'
# reportpath = r'checkstyle\report\a.txt'
# cmd = r'java -classpath checkstyle\lib\checkstyle-8.4-all.jar com.puppycrawl.tools.checkstyle.Main -c checkstyle\lib\sun_checksa.xml {} >{}'.format(codepath, reportpath)
# os.system(cmd)

def static_inspection(codepath):
	codepath = codepath
	reportpath = r'checkstyle\report\a.txt'
	cmd = r'java -classpath checkstyle\lib\checkstyle-8.4-all.jar com.puppycrawl.tools.checkstyle.Main -c checkstyle\lib\sun_checksa.xml {} >{}'.format(codepath, reportpath)
	os.system(cmd)