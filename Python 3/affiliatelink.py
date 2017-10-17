#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
from genericlink import *

#############################################
# Paramétrer les identifiants d'affiliation #
#############################################
AmazonAffiliateID = "mac01-21"
iTunesAffiliateID = "11lIzz"

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