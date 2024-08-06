class LRUCache<T, U> {
    cacheData: Map<T, U>
    capacity: number
    cacheOrder: Map<T, number>
    constructor(capacity: number) {
        this.capacity = capacity
        this.cacheData = new Map()
        this.cacheOrder = new Map()
    }

    set(key: T, value: U): void {
        if (this.cacheData.has(key)) {
            this.cacheData.set(key, value);
            this.cacheOrder.set(key, Date.now())
            return
        }

        // n tá claro qual sinal usar
        if (this.capacity <= this.cacheData.size) {
            const oldKey: T = this.getOlderKey()
            this.cacheData.delete(oldKey)
            this.cacheOrder.delete(oldKey)
        }

        this.cacheData.set(key, value)
        this.cacheOrder.set(key, Date.now())
    }

    getOlderKey(): T {
        // o reduce usa < e preciso aprender pq
        const data: T = [...this.cacheOrder.entries()].reduce((oldest, current) => oldest[1] < current[1] ? oldest : current)[0]
        return data
    }

    get(key: T): U | -1 {
        if (this.cacheData.has(key)) {
            const data: U = this.cacheData.get(key)!
            this.cacheOrder.set(key, Date.now())
            return data
        }

        return -1
    }
}