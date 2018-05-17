#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys, re, codecs, os, csv
csv.field_size_limit(sys.maxsize)

corpusparts = ['train', 'train-test1', 'test1', 'test2']
corpuspath = '../data/'
arffpath = '../arff/'
doctypees = ['fakeNews', 'satire', 'trusted']

for part in corpusparts:
	for file in os.listdir(corpuspath+part+'/'):
		print('Parsing ', part, file)
		with open(corpuspath+part+'/'+file,'r') as filetsv:
			tsvinput = csv.reader(filetsv, delimiter='\t')
			headers = next(tsvinput)
			arff = codecs.open(arffpath+part+'/'+file+'.arff', 'w', 'utf8')
			outids = codecs.open(arffpath+part+'/'+file+'.ids', 'w', 'utf8')
			arff.write('@relation faketrusted\n')
			arff.write('@attribute titre string\n')
			arff.write('@attribute texte string\n')
			arff.write('@attribute class {'+','.join(doctypees)+'}\n')
			arff.write('@data\n')
			instid = 1
			for doc in tsvinput:
				# id      domain  type    uri     author  language        title   text    date    external_uris
				# video-id        channel-id      video-title     video-view-count        lang    type    channel-title   text    id
				outarff = []
				if 'title' in headers:
					indextitle = headers.index('title')
				else:
					indextitle = headers.index('video-title')
				titre = doc[indextitle]
				titre = titre.replace('\r', ' ')
				titre = titre.replace('\n', ' ')
				titre = re.sub('  *', ' ', titre)
				titre = titre.replace('\'', '\\\'')
				outarff.append('\''+titre+'\'')
				indextext = headers.index('text')
				texte = doc[indextext]
				texte = texte.replace('\r', ' ')
				texte = texte.replace('\n', ' ')
				texte = re.sub('  *', ' ', texte)
				texte = texte.replace('\'', '\\\'')
				outarff.append('\''+texte+'\'')
				if 'train' in part:
					indextype = headers.index('type')
					doctype = doc[indextype]
					outarff.append(doctype)
				else:
					outarff.append('?')
				if 'id' in headers:
					indexid = headers.index('id')
				else:
					indexid = headers.index('video-id')
				outids.write(str(instid)+' '+str(doc[indexid])+'\n')
				instid += 1
				arff.write(','.join(outarff)+'\n')
