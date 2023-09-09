#include <stdio.h>
#define MAXI 100000

int grundy[MAXI+5];
int moves[6] = {1,4,27,256,3125,46656};

void init(){
	int i,j,b;
	
	for(i = 0; i <= MAXI; i++){
		grundy[i] = 0;
		b = 1;
		while(b){
			b = 0;
			for(j = 0; j < 6 && moves[j] <= i; j++){
				if(grundy[i-moves[j]] == grundy[i]){
					++grundy[i];
					b = 1;
				}
			}
		}
		
	}
}

int main(){
	init();
	int t,n,xor,a;
	scanf("%d",&t);
	
	while(t--){
		
		scanf("%d",&n);
		xor = 0;
		while(n--){
			scanf("%d",&a);
			xor^=grundy[a];
		}
		if(xor) printf("Little Chef\n");
		else printf("Head Chef\n");
		
	}
	
	return 0;
}
