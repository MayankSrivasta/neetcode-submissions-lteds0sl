class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for(String str : strs)
        {
            sb.append(str.length()).append("#").append(str);
        }
    return sb.toString();

    }
//	ENCODE 4#neet 4#code 4#love3#you
//	DECODE [neet, code, love, you]
    public List<String> decode(String str) {

        List<String> list = new ArrayList();
        int i = 0;
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
