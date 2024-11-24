package main

import (
	"context"
	"sync"
)

type Task struct {
	Error  error
	Value  uint
	Cancel context.CancelFunc
}

type WorkerPool struct {
	Result  chan Task
	Context context.Context
}

func receiver(wg *sync.WaitGroup, worker *WorkerPool) {
	wg.Add(1)
	defer wg.Done()
	for result := range worker.Result {
		if result.Error != nil {
			result.Cancel()
		}
	}
}

func sender(wp *WorkerPool, val uint, cancelFunc context.CancelFunc) {
	wp.Result <- Task{
		Error:  nil,
		Value:  val,
		Cancel: cancelFunc,
	}
}

func main() {
	var wg sync.WaitGroup
	var worker *WorkerPool
	var ctx context.Context
	var cancel context.CancelFunc
	var wp *WorkerPool

	ctx, cancel = context.WithCancel(context.Background())

	wp = &WorkerPool{
		Result:  make(chan Task),
		Context: ctx,
	}

	for i := 0; i < 100; i++ {
		go receiver(&wg, worker)
	}

	for i := 0; i < 100; i++ {
		go sender(wp, uint(i), cancel)
	}
}
