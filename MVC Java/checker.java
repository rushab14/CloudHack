public class checker
{
	public int spaceCheck(String str)
	{
		int ctr = 0;
		char[] ch = str.toCharArray();
		for(char c: ch)
			if(Character.isWhitespace(c))
				ctr++;
		return ctr;
	}
	
	public boolean singleSpaceCheck(String str)
	{
		int ctr = 0;
		char[] ch = str.toCharArray();
		for(char c: ch)
			if(Character.isWhitespace(c))
				return true;
		return false;
	}
	
	public boolean isNotNum(String str)
	{
		int ctr = 0;
		char[] ch = str.toCharArray();
		for(char c: ch)
			if(Character.isDigit(c))
				continue;
			else
				return true;
		return false;
	}
}
