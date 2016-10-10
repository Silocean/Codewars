/*
Description:

Define a method named count_one_char that accepts a string and a char as inputs and returns the number of times the char occurs in the string as an int. You may call only the methods charAt() and length().
 */

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