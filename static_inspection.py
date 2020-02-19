import os
import re

def static_inspection(codepath):
	codepath = codepath
	reportpath = r'checkstyle\report\a.txt'
	cmd = r'java -classpath checkstyle\lib\checkstyle-8.4-all.jar com.puppycrawl.tools.checkstyle.Main -c checkstyle\lib\sun_checksa.xml {} >{}'.format(codepath, reportpath)
	os.system(cmd)

def readreport():
	report = ''
	reportpath = r'checkstyle\report\a.txt'
	with open(reportpath, 'r', encoding='utf-8') as f:
		report = f.read()
	# report = re.sub(r'\r\n', '<br/>', report)
	return report