package main

import (
	"fmt"
	"time"
)

type LRUCache struct {
	cacheData   map[string]interface{}
	cacheOrder  map[string]int64
	capacity    int
}

func NewLRUCache(capacity int) *LRUCache {
	return &LRUCache{
		cacheData:  make(map[string]interface{}),
		cacheOrder: make(map[string]int64),
		capacity:   capacity,
	}
}

func (c *LRUCache) Set(key string, value interface{}) {
	if _, found := c.cacheData[key]; found {
		c.cacheData[key] = value
		c.cacheOrder[key] = time.Now().UnixNano()
		return
	}

	if len(c.cacheData) >= c.capacity {
		oldKey := c.getOlderKey()
		delete(c.cacheData, oldKey)
		delete(c.cacheOrder, oldKey)
	}

	c.cacheData[key] = value
	c.cacheOrder[key] = time.Now().UnixNano()
}

func (c *LRUCache) Get(key string) interface{} {
	if value, found := c.cacheData[key]; found {
		c.cacheOrder[key] = time.Now().UnixNano()
		return value
	}
	return -1
}

func (c *LRUCache) getOlderKey() string {
	var oldestKey string
	var oldestTime int64 = time.Now().UnixNano()

	for key, lastAccess := range c.cacheOrder {
		if lastAccess < oldestTime {
			oldestTime = lastAccess
			oldestKey = key
		}
	}

	return oldestKey
}

func main() {
	cache := NewLRUCache(2)
	cache.Set("a", 1)
	cache.Set("b", 2)
	fmt.Println(cache.Get("a")) // Deve imprimir 1
	cache.Set("c", 3)
	fmt.Println(cache.Get("b")) // Deve imprimir -1, pois "b" foi removido
}
