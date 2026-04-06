class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }

        int[] char_counts = new int[123];

        for(int i=0;i<s.length();i++){
            int count = s.charAt(i);
            char_counts[count] = char_counts[count] + 1;
        }

        for(int i=0;i<t.length();i++){
            int count = t.charAt(i);
            char_counts[count] = char_counts[count] - 1;
        }

        for(int i=0;i<char_counts.length;i++){
            if(char_counts[i]>0){
                return false;
            }
        }

        return true;
    }
}
