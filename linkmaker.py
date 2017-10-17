#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from subprocess import Popen, PIPE
from urlparse import urlparse
# from genericlink import *
# from affiliatelink import *

############################
# Paramétrer le navigateur #
############################
# chrome/firefox
MyBrowser = ""

#############################################
# Paramétrer les identifiants d'affiliation #
#############################################
AmazonAffiliateID = "mac01-21"
AppleAffiliateID = ""
AppleAffiliateFRID = "ii3G"
AppleAffiliateBEID = "ijhc"
AppleAffiliateCHID = "ijhb"
iTunesAffiliateID = "11lIzz"


###########################################################
# Récupérer le lien depuis le navigateur avec AppleScript #
###########################################################
SafariLinkCmd = """tell application "Safari" to get URL of document 1"""
ChromeLinkCmd = """tell application "Google Chrome" to get URL of active tab of window 1"""
FirefoxLinkCmd = """tell application "Firefox" to activate
tell application "System Events" to keystroke "l" using command down
tell application "System Events" to keystroke "c" using command down
delay 0.25
return the clipboard"""
SafariLinkTitleCmd = """tell application "Safari" to get name of document 1"""
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
LinkDomain = "{uri.hostname}".format(uri=LinkParsed)
# print(LinkDomain)

######################
# Construire un lien #
######################
def GenericLink(Link, LinkTitle, LinkDomain):
	LinkName = LinkDomain
	LinkArray = [
				("www.20minutes.fr", "*20 Minutes*"),
				("9to5mac.com", "*9to5 Mac*"),
				# A
				("www.amazon.com", "Amazon"),
				("www.amazon.fr", "Amazon"),
				("anthony.nelzin.fr", "le site d’Anthony Nelzin-Santos"),
				("appadvice.com", "*AppAdvice*"),
				("www.apple.com", "Apple"),
				("appleinsider.com", "*AppleInsider*"),
				("www.appleworld.today", "*Apple World Today*"),
				("arstechnica.com", "*Ars Technica*"),
				# B
				("www.beatsbydre.com", "Beats"),
				("birchtree.me", "*Birchtree*"),
				("www.bloomberg.com", "Bloomberg"),
				("brooksreview.net", "*The Brooks Review*"),
				("www.boulanger.com", "Boulanger"),
				# C
				("cahier.hypotheses.org", "*Consortium Cahier*"),
				("www.cnil.fr", "le site de la CNIL"),
				("coulmont.com", "le blog de Baptiste Coulmont"),
				("craigmod.com", "Craig Mod"),
				("www.cultofmac.com", "*Cult of Mac*"),
				# D
				("daringfireball.net", "*Daring Fireball*"),
				("www.darty.com", "Darty"),
				("www.digitalaudioreview.net", "*DARKO*"),
				("www.digitalstudies.org", "*Digital Studies/Le champ numérique*"),
				("www.dpreview.com", "*DPReview*"),
				# E
				("ebookfriendly.com", "*EBook Friendly*"),
				("elpais.com", "*El País*"),
				("www.engadget.com", "*Engadget*"),
				# F
				("www.facebook.com", "Facebook"),
				("www.fnac.com", "Fnac"),
				("framablog.org", "*Framablog*"),
				("frankchimero.com", "Frank Chimero"),
				("freakonometrics.hypotheses.org", "*Freakonometrics*"),
				("www.ft.com", "*Financial Times*"),
				# G
				("github.com", "GitHub"),
				("www.goodreads.com", "Goodreads"),
				# H
				("www.headfonia.com", "*Headfonia*"),
				("www.humanite.fr", "*L’Humanité*"),
				# I
				("www.igen.fr", "*iGeneration*"),
				("www.innerfidelity.com", "*InnerFidelity*"),
				("ioccasion.fr", "iOccasion"),
				("itunes.apple.com", "iTunes"),
				# K
				("keylifornia.com", "Keylifornia"),
				# L
				("www.lci.fr", "*LCI*"),
				("www.lefigaro.fr", "*Le Figaro*"),
				("www.lemonde.fr", "*Le Monde*"),
				("abonnes.lemonde.fr", "*Le Monde*"),
				("www.leparisien.fr", "*Le Parisien*"),
				("www.liberation.fr", "*Libération*"),
				("linuxfr.org", "*LinuxFR*"),
				("lwn.net", "*LWN*"),
				# M
				("www.macg.co", "*MacGeneration*"),
				("forums.macg.co", "les forums de MacGeneration"),
				("www.macrumors.com", "*MacRumors*"),
				("www.macsales.com", "OWC"),
				("blog.macsales.com", "le blog d’OWC"),
				("www.macstories.net", "*MacStories*"),
				("www.macworld.com", "Macworld"),
				("www.manton.org", "le blog de Manton Reece"),
				("marco.org", "le blog de Marco Arment"),
				("www.marketwatch.com", "MarketWatch"),
				("medium.com", "*Medium*"),
				("metrozendodo.fr", "*métro[zen]dodo*"),
				("clio.metrozendodo.fr", "*métro[zen]dodo*"),
				("memo.metrozendodo.fr", "*métro[mémo]dodo*"),
				("photo.metrozendodo.fr", "*métro[photo]dodo*"),
				("stylo.metrozendodo.fr", "*métro[stylo]dodo*"),
				("mondaynote.com", "*Monday Note*"),
				("www.monde-diplomatique.fr", "*Le Monde diplomatique*"),
				# N
				("www.nytimes.com", "*New York Times*"),
				# O
				("www.ouest-france.fr", "*Ouest-France*"),
				# P
				("www.patentlyapple.com", "*Patently Apple*"),
				("www.pcworld.com", "*PCWorld*"),
				("www.ped30.com", "*Apple 3.0*"),
				("www.penaddict.com", "*The Pen Addict"),
				("www.popsci.com", "*Popular Science*"),
				# Q
				("www.qobuz.com", "Qobuz"),
				# R
				("www.reddit.com", "Reddit"),
				("www.recode.net", "*Recode*"),
				("refurbgeneration.com", "RefurbGeneration"),
				("www.reporterssolidaires.com", "Reporters solidaires"),
				("www.reuters.com", "Reuters"),
				# S
				("sixcolors.com", "*Six Colors*"),
				("sms.hypotheses.org", "*Mondes sociaux*"),
				("stackoverflow.com", "Stack Overflow"),
				("standblog.org", "le blog de Tristan Nitot"),
				("stratechery.com", "*Stratechery*"),
				# T
				("www.techhive.com", "*TechHive*"),
				("thepelikansperch.com", "*The Pelikan Perch*"),
				("www.theverge.com", "*The Verge*"),
				("tidbits.com", "*TidBits*"),
				("toucharcade.com", "*TouchArcade*"),
				("www.twitter.com", "Twitter"),
				# U
				("www.underconsideration.com/", "*Brand New*"),
				# W
				("www.watchgeneration.fr", "*WatchGeneration*"),
				("www.wellappointeddesk.com", "*The Well-Appointed Desk*"),
				("en.wikipedia.org", "*Wikipedia*"),
				("fr.wikipedia.org", "*Wikipédia*"),
				("www.wsj.com", "*Wall Street Journal*"),
				# Y
				("www.youtube.com", "YouTube"),
				# Z
				("zinzolin.org", "Zinzolin"),
				]
	for LinkArrayDomain,LinkArrayName in LinkArray:
		if LinkArrayDomain == LinkDomain:
			LinkName = LinkArrayName
	MarkdownLink = "[" + LinkName + "](" + Link + " '" + LinkTitle + "'" + ")"
	print (MarkdownLink)
	# Si lien affilié, vérifier qu'il fonctionne bien.
	# Popen(['open', Link])

#######################################
# Définir les fonctions de traitement #
#######################################
# Lien Amazon
# L'ASIN comporte toujours 10 caractères
# Les liens originaux peuvent contenir dp ou gp, mais les liens affiliés doivent contenir dp
def AmazonLink(Link, LinkTitle, LinkDomain):
	search = re.search(r'(dp|gp)(\/product)?\/(\S{10})\/', Link)
	if search:
		GenericLink("https://www.amazon.fr/dp/" + search.group(3) + "/?tag=" + AmazonAffiliateID, LinkTitle, LinkDomain)
	else:
		GenericLink(Link, LinkTitle, LinkDomain)
		
# Lien AppleLink
def AppleLink(Link, LinkTitle, LinkDomain):
	search = re.search(r'https://www.apple.com/(fr|be-fr|ch-fr|fr-edu|be-fr-edu|ch-fr-edu)?(\S)*', Link)
	if search:
		if search.group(1) == "be" or search.group(1) == "be-edu":
			AppleAffiliateID = AppleAffiliateBEID
		elif search.group(1) == "ch" or search.group(1) == "ch-edu":
			AppleAffiliateID = AppleAffiliateCHID
		else:
			AppleAffiliateID = AppleAffiliateFRID
		GenericLink("http://aos.prf.hn/click/camref:" + AppleAffiliateID + "/destination:" + Link, LinkTitle, LinkDomain)
	else:
		GenericLink(Link, LinkTitle, LinkDomain)

# Lien iTunes
# Le paramètre mt n'est pas obligatoire, mais souvent présent
# Utilisation de geo.itunes.apple.com pour gérer les différents pays
def iTunesLink(Link, LinkTitle, LinkDomain):
	search = re.search(r'https://itunes.apple.com/fr/(app|album|artist|audiobook|book|collection|movie|podcast|tv-season)/\S*(id\d+)(\?mt=\d+)?', Link)
	if search.group(3): # Si ?mt=
		GenericLink("https://geo.itunes.apple.com/fr/" + search.group(1) + "/" + search.group(2) + search.group(3) + "&at=" + iTunesAffiliateID, LinkTitle, LinkDomain)
	elif search.group(2):
		GenericLink("https://geo.itunes.apple.com/fr/" + search.group(1) + "/" + search.group(2) + "&at=" + iTunesAffiliateID, LinkTitle, LinkDomain)
	else:
		GenericLink(Link, LinkTitle, LinkDomain)
		
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
	GenericLink(LinkCleaned, LinkTitle, LinkDomain)	