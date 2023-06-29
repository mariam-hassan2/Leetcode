/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || k == 0){return head;}
        if(head.next == null){return head;}
        int counter = 0;
        ListNode pointer = head;
        ListNode prev = null;  
        int len = length(head);
        int x = len-k%len-1;

        if(len == k){return head;}
        if(k % len == 0){return head;}
        
        prev = null;
        pointer = head; 
        while(counter < x+1 ){
            prev = pointer;
            pointer = pointer.next;
            counter++;
        }

        prev.next = null;

        ListNode newHead = pointer;
        while(pointer != null && pointer.next != null){
            pointer = pointer.next;
        }
        if(pointer != null){
            pointer.next = head;
            head = pointer;
        }
        

        return newHead;
    }
    
    public int length(ListNode list){
        int counter = 0;
        while(list != null){
            list = list.next;
            counter++;
        }
        return counter;
    }
}

