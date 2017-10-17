#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
	print ("[" + LinkName + "](" + Link + " '" + LinkTitle + "'" + ")")