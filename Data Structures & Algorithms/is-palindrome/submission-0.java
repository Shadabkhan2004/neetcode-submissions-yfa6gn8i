class Solution {
    public boolean isPalindrome(String s) {
        String fixedString = "";
        for(char c : s.toCharArray()){
            if(Character.isDigit(c) || Character.isLetter(c)){
                fixedString+=c;
            }
        }

        fixedString = fixedString.toLowerCase();
        int i =0;
        int j = fixedString.length()-1;
        while(i<j){
            if(fixedString.charAt(i) != fixedString.charAt(j)){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
}
