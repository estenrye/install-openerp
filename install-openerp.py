#!/usr/bin/env python
# Thanks to Alan Lord for his OpenERP-on-Ubuntu tips: http://www.theopensourcerer.com/2012/12/how-to-install-openerp-7-0-on-ubuntu-12-04-lts/
import argparse
import urllib
import platform
import subprocess

system = platform.system().lower()
print system

if system == "linux":
	distro = platform.linux_distribution()[0].lower()
	print "%s distro: %s" % (system, distro)

if distro:
	if distro in ['ubuntu', 'debian']:
		url = "http://nightly.openerp.com/7.0/nightly/deb/openerp_7.0-latest-1_all.deb"
		filename = "openerp_7.0-latest-1_all.deb"
	else:
		print "Sorry, we don't have an automated install for %s yet!" % distro

print "downloading %s" % url
urllib.urlretrieve(url, filename)
subprocess.call("sudo apt-get -y install postgresql", shell=True)
subprocess.call("sudo dpkg -i %s" % filename, shell=True)
subprocess.call("sudo apt-get -f -y install", shell=True)
print "Creating OpenERP Postgres user"
subprocess.call("sudo -u postgres createuser --createdb --no-createrole --no-superuser --pwprompt openerp", shell=True)

