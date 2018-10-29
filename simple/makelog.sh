for i in repositorys/*
do
	cd $i
	git log -p --pretty=format:!!!!!!!%s > mygitlogdata.txt
	pwd
	cd ../../
	pwd
done
