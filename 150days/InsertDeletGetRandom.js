// Input
// ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
// [[], [1], [2], [2], [], [1], [2], []]
// Output
// [null, true, false, true, 2, true, false, 2]

class randomized{
    constructor(){
      this.itemToIndex = new Map()
      this.itemArray = new Array()

    }

    insert(item){
        if(this.itemToIndex.has(item)){
            return false
        }

        let index = this.itemArray.length;
        this.itemArray.push(item)
        this.itemToIndex.set(item,index)
        return true
    }

    remove(item){
        if(!this.itemToIndex.has(item)){
            return false
        }
        let index = this.itemToIndex.get(item)
        let lastItem = this.itemArray[this.itemArray.length -1]

        this.itemToIndex.set(lastItem,index)
        this.itemArray[index] = lastItem
        this.itemArray.pop();
        this.itemToIndex.delete(item)
        return true

    }

    getRandom(){
        let index = Math.floor(Math.random() * this.itemArray.length)
        return this.itemArray[index]
    }
}






// var RandomizedSet = function() {
//     this.numMap = new Map();  // Maps value to its index in the list
//     this.numList = [];        // List of values
//   };
  
//   /** 
//    * @param {number} val
//    * @return {boolean}
//    */
//   RandomizedSet.prototype.insert = function(val) {
//     if (this.numMap.has(val)) {
//       return false;
//     }
//     this.numMap.set(val, this.numList.length);
//     this.numList.push(val);
//     return true;
//   };
  
//   /** 
//    * @param {number} val
//    * @return {boolean}
//    */
//   RandomizedSet.prototype.remove = function(val) {
//     if (!this.numMap.has(val)) {
//       return false;
//     }
//     const idx = this.numMap.get(val);
//     const lastElement = this.numList[this.numList.length - 1];
  
//     // Move the last element to the place of the element to delete
//     this.numList[idx] = lastElement;
//     this.numMap.set(lastElement, idx);
  
//     // Remove the last element from the list and the map
//     this.numList.pop();
//     this.numMap.delete(val);
  
//     return true;
//   };
  
//   /**
//    * @return {number}
//    */
//   RandomizedSet.prototype.getRandom = function() {
//     const randomIndex = Math.floor(Math.random() * this.numList.length);
//     return this.numList[randomIndex];
//   };
  
//   /** 
//    * Your RandomizedSet object will be instantiated and called as such:
//    * var obj = new RandomizedSet()
//    * var param_1 = obj.insert(val)
//    * var param_2 = obj.remove(val)
//    * var param_3 = obj.getRandom()
//    */
  