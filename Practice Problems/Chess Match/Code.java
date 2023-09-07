

import java.util.*;
import java.lang.*;
import java.io.*;


class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
    Scanner s= new Scanner(System.in);
    int t= s.nextInt();
    
    while(t-->0){
        int n=s.nextInt();
        int a=s.nextInt();
        int b=s.nextInt();
        
        System.out.println((2*(180+n))-(a+b));
    }
	}
}
