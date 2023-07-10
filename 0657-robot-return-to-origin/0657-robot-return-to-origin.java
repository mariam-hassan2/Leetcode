class Solution {
    public boolean judgeCircle(String moves) {
        // u d r l
        int[] list = {0, 0, 0, 0};
        for(int i = 0 ; i < moves.length();i++){
            if(moves.charAt(i)=='U'){list[0]++;}
            else if(moves.charAt(i)=='D'){list[1]++;}
            else if(moves.charAt(i) == 'R'){list[2]++;}
            else if(moves.charAt(i) == 'L'){list[3]++;}
        }
        if(list[0]==list[1] && list[2]==list[3]){
            return true;
        }
            return false;
        }    
}