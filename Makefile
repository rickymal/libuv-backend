CXX=clang++
CXXFLAGS=-Wall -g -std=c++17  # Você pode especificar a versão do C++ aqui

all: main

main: main.o
	$(CXX) -o main main.o

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp

clean:
	rm -f *.o main
