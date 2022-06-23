for file in /Users/ya/Documents/GitHub/ITSEC21/data/CrossMatch_Sample_DB/original_jpeg/*
do
	echo "Processing ${file##*/}"
	/Users/ya/Desktop/FingerPrint/bin/mindtct -b /Users/ya/Documents/GitHub/ITSEC21/data/CrossMatch_Sample_DB/original_jpeg/${file##*/} /Users/ya/Documents/GitHub/ITSEC21/data/CrossMatch_Sample_DB/minutiaeExtraction/$(basename ${file##*/} | cut -d. -f1)
done
