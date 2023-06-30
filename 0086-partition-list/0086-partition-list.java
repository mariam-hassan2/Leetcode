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
    public ListNode partition(ListNode head, int x) { 
        ListNode left = new ListNode(0);
        ListNode right = new ListNode(0);
        ListNode llast = left;
        ListNode rlast = right;

        while(head != null){
            if(head.val < x){
                llast.next = head;
                llast = llast.next;
            }
            else{
                rlast.next= head;
                rlast = rlast.next;
            }
            head = head.next;
        }
        llast.next = right.next;
        rlast.next = null;
        return left.next;
    }
}
