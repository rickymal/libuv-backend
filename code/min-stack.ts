class MinStack {
    data: Array<number>
    minValue: number

    constructor() {
        this.minValue = Infinity
    }

    push(value: number) {
        /**
         * Não vai funcionar pq poderiamos ter valores repetidos
         */
        if (value < this.minValue) {
            this.minValue = value
        }
        this.data.push(value)
    }

    pop() {
        
        return this.data.pop()
    }

    getMin() {
        return this.minValue
    }
}
