/*
Description:

Color Ghost

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
c# Ghost ghost = new Gost(); ghost.GetColor(); // => "white" or "yellow" or "purple" or "red"
 */
import java.util.Random;
public class Ghost {
  // your code goes here
  public String getColor() {
		Random random = new Random();
		int i = random.nextInt(4);
		switch(i) {
		case 0:
			return "white";
		case 1:
			return "yellow";
		case 2:
			return "purple";
		case 3:
			return "red";
		default:
			return null;	
		}
	}
}