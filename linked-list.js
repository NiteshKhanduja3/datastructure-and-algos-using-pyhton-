// It is List  Which consists of node ( Data value and pointer)
//the first node is called the head and the tail 
//at the end the tail value is null
// In javascript we have to make a linked list there is no built ins
//Why we need Linked list? inserting in between link list is easy than array
//BigO of link list is  append and prepend = O(1) ,,, lookup ,delete and Insert is O(n)


// const obj1 ={a:true}; // giving the value
// const obj2 = obj1; // giving the pointer
// obj1.a ="Nitesh" // changing the value
// obj2.a ="Nitesh2"
// delete obj1 // deleting the previous node
// console.log(obj2)

// making link list10-->5--->6

// let myLinkedList ={
//     head:{
//         value:10,
//         next:{                     // head contains the value and next is the pointer
//             value:5,
//             next:{
//                 value:16,
//                 next:null
//             }
//         }
//     }
// }


class LinkedList{
    constructor(value){
    this.head ={
        value:value,
        next:null

    }
    this.tail = this.head;
    this.length = 1
}
// adding to the end of the list
append(value){
const newNode={
    value: value,
    next: null
}
this.tail.next = newNode
this.tail =newNode
this.length++;
return this
}
//appending at beginning
prepend(value){
    const newNode ={
      value:value,
      next: null
    }
    newNode.next = this.head;
    this.head =newNode
    this.length++
    return this

}
printList(){
    const array =[]
    let curretNode = this.head
    while (curretNode !==null){
        array.push(curretNode.value)
        curretNode = curretNode.next
    }
    console.log( array)
    return array
}
// Inserting in the linklist
insert(index,value){
//check parameters
if(index >= this.length){
    return this.append(value)
}
const newNode ={
    value:value,
    next:null
}
const leader =this.tracerseToIndex(index-1)
const holdingPointer = leader.next
leader.next =newNode
newNode.next =holdingPointer
this.length++;
return this.printList
}
tracerseToIndex(index){
    let counter = 0
    let curretNode = this.head
    while (counter !==index){
        curretNode =curretNode.next
        counter++
    }
    return curretNode
}
remove(index){
    //check params
    const leader = this.tracerseToIndex(index-1);
    const unwantedNode = leader.next;
    leader.next = unwantedNode.next;
    this.length--;
    return this.printList();
}

}

const myLinkedList = new LinkedList(10)

myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(20,88)
myLinkedList.remove(2)
myLinkedList.printList()
// myLinkedList.printList()
// console.log(myLinkedList)

