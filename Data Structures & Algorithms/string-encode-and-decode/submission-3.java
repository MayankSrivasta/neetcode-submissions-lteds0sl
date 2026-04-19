class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs)
            sb.append(str.length()).append("#").append(str);
        return sb.toString();
    }

  	public static List<String> decode(String str) {
		List<String> list = new ArrayList();
		int i = 0;
		int n = str.length();
		while (i < n) {
			int j = i;
			while (str.charAt(j) != '#')
				j++;

			int strLen = Integer.valueOf(str.substring(i, j));
			i = j + 1 + strLen;
			list.add(str.substring(j + 1, i));
		}
		return list;
	}

}
