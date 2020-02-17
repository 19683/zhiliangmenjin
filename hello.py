
# java -classpath checkstyle\lib\checkstyle-8.4-all.jar 
# com.puppycrawl.tools.checkstyle.Main -c checkstyle\lib\sun_checksa.xml 
# D:\python_work\QualityControl\testcode\src\test\java\ComputingTest.java >checkstyle\report\a.txt

#  Check.java替换为要检测的java文件，可以是路径或具体文件。
#  a.txt为要输出的检测报告

import os

codepath = r'D:\python_work\QualityControl\testcode\src\test\java\ComputingTest.java'
reportpath = r'checkstyle\report\a.txt'
cmd = r'java -classpath checkstyle\lib\checkstyle-8.4-all.jar com.puppycrawl.tools.checkstyle.Main -c checkstyle\lib\sun_checksa.xml {} >{}'.format(codepath, reportpath)
os.system(cmd)