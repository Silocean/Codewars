public class Count {
	
	// count characters in string
	public int count_one_char(String s, char c){
  //do something
    int count = 0;
    for(int i=0; i<s.length(); i++) {
      if (s.charAt(i) == c){
        count ++;
      }
    }
    return count;
  }
  }