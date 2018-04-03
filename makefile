grafica.png: graph.py laminas.txt
	python graph.py
laminas.txt: album.cpp
	c++ album.cpp
	./a.out>laminas.txt
