for file in /Users/ya/Documents/GitHub/ITSEC21/data/FingerPrints_1Channel/*
do
	echo "Processing ${file##*/}"
	/Users/ya/Desktop/FingerPrint/bin/mindtct /Users/ya/Documents/GitHub/ITSEC21/data/FingerPrints_1Channel/${file##*/} /Users/ya/Documents/GitHub/ITSEC21/data/minutiaeExtraction/$(basename ${file##*/} | cut -d. -f1)
done
