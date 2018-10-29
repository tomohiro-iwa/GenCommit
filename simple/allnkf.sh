for i in repositorys/*
do
	cd $i
	nkf -w mygitlogdata.txt > mygitlogdata2.txt
	pwd
	cd ../../
	pwd
done
