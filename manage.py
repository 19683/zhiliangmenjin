#coding=utf-8
import re
import os

def config_checksa(modulenames):

	xmlstring = '<?xml version="1.0"?><!DOCTYPE module PUBLIC\
"-//Puppy Crawl//DTD Check Configuration 1.3//EN"\
"http://checkstyle.sourceforge.net/dtds/configuration_1_3.dtd">\
<module name="Checker">\
<module name="TreeWalker">'

	for modulename in modulenames:
		pattern = r'<module name=\"' + modulename + r'\">.+?</module>'

		xmlpath = r'checksa.xml'
		with open(xmlpath, 'r', encoding='utf-8') as xf:
			report = xf.read()
		target = re.search(pattern, report, flags=re.DOTALL).group()
		target = re.sub(r'\s+', '', target)

		xmlstring += target

	xmlstring = xmlstring + '</module></module>'

	sun_checksa_path = r'checkstyle\lib\sun_checksa.min.xml'
	with open(sun_checksa_path, 'w', encoding='utf-8') as sf:
		sf.write(xmlstring)