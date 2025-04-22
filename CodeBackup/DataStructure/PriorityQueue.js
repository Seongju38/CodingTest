class PriorityQueue {
  constructor(comparator = (a, b) => a - b) {
    this._elements = [];
    this._comparator = comparator;
  }

  enq(element) {
    let size = this._elements.push(element);
    let current = size - 1;

    while (current > 0) {
      let parent = Math.floor((current - 1) / 2);

      if (this._compare(current, parent) <= 0) break;

      this._swap(parent, current);
      current = parent;
    }
    return size;
  }

  size() {
    return this._elements.length;
  }

  deq() {
    const first = this.peek();
    const last = this._elements.pop();
    const size = this.size();

    if (size === 0) return first;

    this._elements[0] = last;
    let current = 0;

    while (current < size) {
      let largest = current;
      let left = 2 * current + 1;
      let right = 2 * current + 2;

      if (left < size && this._compare(left, largest) >= 0) {
        largest = left;
      }

      if (right < size && this._compare(right, largest) >= 0) {
        largest = right;
      }

      if (largest === current) break;

      this._swap(largest, current);
      current = largest;
    }
    return first;
  }

  peek() {
    return this._elements[0];
  }

  _compare(a, b) {
    return this._comparator(this._elements[a], this._elements[b]);
  }

  _swap(a, b) {
    let tmp = this._elements[a];
    this._elements[a] = this._elements[b];
    this._elements[b] = tmp;
  }
}

// 사용 예시
let pq = new PriorityQueue(function (a, b) {
  return a.cash - b.cash;
});

pq.enq({ cash: 250, name: "ABC" });
pq.enq({ cash: 300, name: "DEF" });
pq.enq({ cash: 150, name: "GHI" });

console.log(pq.size());
console.log(pq.deq());
console.log(pq.peek());
console.log(pq.size());
