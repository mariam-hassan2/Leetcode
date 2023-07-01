
class Solution{ 
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode last = dummy;
        if(list1 == null) return list2;
        if(list2 == null) return list1;
            while(list1 != null && list2 != null){
                if(list1.val < list2.val){
                  last.next = list1;
                  list1 = list1.next;
                }
                else{
                  last.next = list2;
                  list2 = list2.next;
                }
                last = last.next;
            }
            if(list1 !=null){
                last.next = list1;
            }
            else{
                last.next = list2;
            }
        return dummy.next;    
    }
}
