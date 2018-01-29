#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################
#########################
# Anthony Nelzin-Santos #
# Licence CeCILL v2.1   #
#########################
#########################

from __future__ import print_function
import re
from subprocess import Popen, PIPE
from urlparse import urlparse

############################
# Paramétrer le navigateur #
############################
# safaridev/chrome/firefox
MyBrowser = ""

#############################################
# Paramétrer les identifiants d'affiliation #
#############################################
AmazonAffiliateID = "mac01-21"
AppleAffiliateFRID = "ii3G"
AppleAffiliateBEID = "ijhc"
AppleAffiliateCHID = "ijhb"
iTunesAffiliateID = "11lIzz"

###########################################################
# Récupérer le lien depuis le navigateur avec AppleScript #
###########################################################
SafariLinkCmd = """tell application "Safari" to get URL of document 1"""
SafaridevLinkCmd = """tell application "Safari Technology Preview" to get URL of document 1"""
ChromeLinkCmd = """tell application "Google Chrome" to get URL of active tab of window 1"""
FirefoxLinkCmd = """tell application "Firefox" to activate
tell application "System Events" to keystroke "l" using command down
tell application "System Events" to keystroke "c" using command down
delay 0.25
return the clipboard"""
SafariLinkTitleCmd = """tell application "Safari" to get name of document 1"""
SafaridevLinkTitleCmd = """tell application "Safari Technology Preview" to get name of document 1"""
ChromeLinkTitleCmd = """tell application "Google Chrome" to get URL of active tab of window 1"""

def osacript(script):
	popen = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
	stdout, stderr = popen.communicate(script)
	return stdout.strip()

if MyBrowser == "chrome":
	Link = osacript(ChromeLinkCmd)
	LinkTitle = osacript(ChromeLinkTitleCmd)
elif MyBrowser == "firefox":
	Link = osacript(FirefoxLinkCmd)
	LinkTitle = ""
elif MyBrowser == "safaridev":
	Link = osacript(SafaridevLinkCmd)
	LinkTitle = osacript(SafaridevLinkTitleCmd)
else:
	Link = osacript(SafariLinkCmd)
	LinkTitle = osacript(SafariLinkTitleCmd)
	# print(Link)
	# print(LinkTitle)

###############################
# Extraire le domaine du lien #
###############################
LinkParsed = urlparse(Link)
LinkCleaned = LinkParsed.scheme + "://" + LinkParsed.netloc + LinkParsed.path
LinkDomain = LinkParsed.netloc
# print(LinkDomain)

######################
# Construire un lien #
######################
def MakeLink(Link, LinkTitle, LinkDomain, LinkType):
	MarkdownLink = "[]: " + Link + " '" + LinkTitle + "'"
	print (MarkdownLink, end='')
	
	if LinkType == "affiliate":
		Popen(['open', Link])

#######################################
# Définir les fonctions de traitement #
#######################################
# Lien Amazon
# L'ASIN comporte toujours 10 caractères
# Les liens originaux peuvent contenir dp ou gp, mais les liens affiliés doivent contenir dp
def AmazonLink(Link, LinkTitle, LinkDomain):
	search = re.search(r'(dp|gp)(\/product)?\/(\S{10})\/', Link)
	if search:
		MakeLink("https://www.amazon.fr/dp/" + search.group(3) + "/?tag=" + AmazonAffiliateID, LinkTitle, LinkDomain, "affiliate")
	else:
		MakeLink(Link, LinkTitle, LinkDomain, "normal")
		
# Lien Apple
def AppleLink(Link, LinkTitle, LinkDomain):
	search = re.search(r'https://www.apple.com/(fr|be-fr|ch-fr|fr-edu|be-fr-edu|ch-fr-edu)/shop/?(\S)*', Link)
	if search:
		if search.group(1) == "be" or search.group(1) == "be-edu":
			AppleAffiliateID = AppleAffiliateBEID
		elif search.group(1) == "ch" or search.group(1) == "ch-edu":
			AppleAffiliateID = AppleAffiliateCHID
		else:
			AppleAffiliateID = AppleAffiliateFRID
		MakeLink("http://aos.prf.hn/click/camref:" + AppleAffiliateID + "/destination:" + Link, LinkTitle, LinkDomain, "affiliate")
	else:
		MakeLink(Link, LinkTitle, LinkDomain, "normal")

# Lien iTunes
# Utilisation de geo.itunes.apple.com pour gérer les différents pays
def iTunesLink(Link, LinkTitle, LinkDomain):
	search = re.search(r'https://itunes.apple.com/fr/(app|album|artist|audiobook|author|book|collection|movie|podcast|tv-season)/(\S*)/(id\d+)', Link)
	iTunesLinkMediaType = "1"
	iTunesLinkTypeArray = [
		("app", "8"),
		("audiobook", "3"),
		("book", "11"),
		("movie", "6"),
		("podcast", "2"),
		("tv-season", "4"),
	]
	for iTunesLinkTypeArrayName,iTunesLinkTypeArrayNumber in iTunesLinkTypeArray:
		if iTunesLinkTypeArrayName == search.group(1):
			iTunesLinkMediaType = iTunesLinkTypeArrayNumber
	MakeLink("https://geo.itunes.apple.com/fr/" + search.group(1) + "/" + search.group(2) + "/" + search.group(3) + "?mt=" + iTunesLinkMediaType + "&at=" + iTunesAffiliateID, LinkTitle, LinkDomain, "affiliate")
	
##########################################
# Traiter le lien en fonction du domaine #
##########################################
if "www.amazon" in LinkDomain:
	AmazonLink(LinkCleaned, LinkTitle, LinkDomain)
elif LinkDomain == "www.apple.com":
	AppleLink(LinkCleaned, LinkTitle, LinkDomain)
elif LinkDomain == "itunes.apple.com":
	iTunesLink(LinkCleaned, LinkTitle, LinkDomain)
else:
	MakeLink(LinkCleaned, LinkTitle, LinkDomain, "normal")	