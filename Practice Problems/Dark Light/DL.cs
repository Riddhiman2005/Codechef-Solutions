using System;
using System.Linq;

public class Test
{
	public static void Main()
	{
		int T = int.Parse( Console.ReadLine() );
		
		while ( (T --) > 0 )
		{
		    var parts = Console.ReadLine().Split();
		    
		    Console.WriteLine( Torch.GetStatus( parts[0],parts[1] ) );
		}
	}

    public static class Torch
    {
        public class Level
        {
            public Level(int number, bool status) { Number = number; Status = status; }
            
            public int  Number { get; private set; }
            public bool Status { get; private set; }
        }

        public static readonly Level[] Levels = new Level[]
        {
            new Level( 1,true),
            new Level( 2,true),
            new Level( 3,true),
            new Level( 4,false),
        };

        public static string GetStatus(string N, string K) 
        {
            return GetStatus( Levels, int.Parse( N ) , int.Parse( K ) == 1 );
        }
        
        private static string GetStatus(Level[] levels , int numberOfChanges , bool initialStatus )
        {
            int currentIndex = Array.FindIndex( levels , x => x.Status == initialStatus );

            if ( initialStatus )
			{
                if ((currentIndex + numberOfChanges) % levels.Length != 0)
                    return "Ambiguous";
            }

            return levels[(currentIndex + numberOfChanges) % levels.Length ].Status ? "On" : "Off";
        }
    }
}
