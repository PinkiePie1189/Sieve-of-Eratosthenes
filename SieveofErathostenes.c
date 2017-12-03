//Sieve of Erathostenes C implementation
//Reads N from stdin
//Calculates sum of prime  numbers up to N and prints them to stdout
#include<stdio.h>
#include<limits.h>
#define MAXN 2000000
void sieve(int N);
FILE*fin,*fout;
int marked[MAXN+1];
long long sum=0;
int main()
{
    fin=fopen("ciur.in","r");
    fout=fopen("ciur.out","w");
    int N;
    fscanf(stdin,"%d",&N);
    sieve(N);
    fprintf(stdout,"%lld",sum);
    return 0;
}
void sieve(int N)
{
    marked[0]=1;
    marked[1]=1;
    int i;
    for(i=2;i<=N;i++)
    {
        if(!marked[i])
        {
            sum+=i;
            long long j;
            for(j=1LL*i*i;j<=N;j+=i)
            {
                marked[j]=1;
            }
        }
    }
}
