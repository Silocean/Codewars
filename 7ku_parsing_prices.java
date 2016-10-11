/*
Description:

Implement String#to_cents, which should parse prices expressed as $1.23 and return number of cents, or in case of bad format return nil.
 */
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class CentParser {

  public static Integer toCents(String price) {
    if (price == null) {
        return null;
    }
    Pattern p = Pattern.compile("^\\$\\d+\\.\\d{2}$");
    if (!p.matcher(price).matches()) {
        return null;
    }
    return Integer.parseInt(price.replaceAll("[$.]", ""));
  }
  
}