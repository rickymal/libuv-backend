package main

type Handler interface {
	Run() error
}

func main() {
	worker.Add()
}
