#!/bin/bash

python3 buildarff.py
wekacmd="java -Xmx8g -cp /Applications/weka-3-8-2-oracle-jvm.app/Contents/Java/weka.jar"
for src in en fr yt; do
	echo "Processing $src"
	$wekacmd weka.filters.unsupervised.attribute.StringToWordVector -L -C -M 2 -W 100000 -T -P 'STWV' -b -i ../arff/train-test1/storyzy_${src}_train.tsv.arff -o ../arff/train-test1/storyzy_${src}_train.tsv.preproc.arff -r ../arff/test2/storyzy_${src}_test2.tsv.arff -s ../arff/test2/storyzy_${src}_test2.tsv.preproc.arff -tokenizer "weka.core.tokenizers.NGramTokenizer -min 1 -max 5"
	#algos="rules.ZeroR bayes.NaiveBayes bayes.NaiveBayesMultinomial functions.SMO"
	$wekacmd weka.classifiers.functions.SMO -C 4 -c 1 -no-cv -t ../arff/train-test1/storyzy_${src}_train.tsv.preproc.arff -d fake.mdl
	$wekacmd weka.classifiers.functions.SMO -c 1 -l fake.mdl -T ../arff/test2/storyzy_${src}_test2.tsv.preproc.arff -p 0 > preds.out
	cat preds.out | grep '^ *[0-9]* *[0-9]:? *[0-9]:[^ ]*' | sed -E 's/^ *([0-9]*) *[0-9]*:\? *[0-9]*:([^ ]*) *.*/\1 \2/' > preds.ids
	join -1 1 -2 1 ../arff/test2/storyzy_${src}_test2.tsv.ids preds.ids | cut -d ' '  -f 2,3 | sed "s/$/ $src/" > soumissionsrc-$src
done
echo 'id	type	source' > soumissionfull
cat soumissionsrc* | tr ' ' '\t' >> soumissionfull
rm preds.*
