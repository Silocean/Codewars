/*
Description:

What could be easier than comparing integer numbers? However, the given piece of code doesn't recognize some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.
 */
public class HowDoICompare {
    public static String whatIs(Integer x) {
        for (Object[] p : specialNumbers) {
            if ((int)p[0] == x)
                return (String)p[1];
        }
        return "nothing";
    }
    
    static final Object[][] specialNumbers = {
        {42, "everything"},
        {42 * 42, "everything squared"},
    }
}