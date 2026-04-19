class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs)
            sb.append(str.length()).append("#").append(str);
        return sb.toString();
    }

    public List<String> decode(String str) {
        int i = 0;
        List<String> list = new ArrayList();
        while(i < str.length())
        {
            int j = i;

            while(str.charAt(j) != '#')
                j++;
            int length = Integer.valueOf(str.substring(i, j));
            i = j + 1 + length;
            list.add(str.substring(j + 1, i));
        }
        return list;
    }
}
