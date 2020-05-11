#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n = 1048576;
	int a[n];
	for (int i = 0; i < n; ++i)
	{
		a[i]=i;
	}

	//random_shuffle(a, a + n);
	FILE * fp = fopen("dataset_search.txt","w");
	for (int i = 0; i < n; ++i)
	{
		// cout<<a[i]<<" ";
		fprintf(fp, "%d\n", a[i]);
	}


	fclose(fp);
}