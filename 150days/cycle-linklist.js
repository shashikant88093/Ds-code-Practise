
// Given head, the head of a linked list, determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list.Otherwise, return false.


function ListNode(val) {
    this.val = val; 
    this.next = null;
}

const hasCycle = function (head) {
    let slow = head;
    let fast = head;

    while (fast && fast.next) {
        slow = slow.next;        // Move slow pointer by 1 step.
        fast = fast.next.next;   // Move fast pointer by 2 steps.

        if (slow === fast) {
            return true; // Cycle detected.
        }
    }

    return false; // No cycle found.
};


const head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = head.next; // Creates a cycle.

console.log(hasCycle(head));