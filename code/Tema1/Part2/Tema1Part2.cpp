#include <iostream>
using namespace std;
#define PI 3.14159265358979323846

struct special {
	int numar;
	bool e_special;
};

float PerimetruCerc(int raza)
{
	float perimetru=0;
	perimetru= 2 * raza * PI;
	return perimetru;
}
float AriaCerc(int raza)
{
	float aria = 0;
	aria = raza * raza * PI;
	return aria;
}


int cmmdc(int a, int b)
{
	while (a != b)
	{
		if (a > b)
			a = a - b;
		else
			b = b - a;
	}
	return a;
}

int Suma(int n,int vector[])
{
	int s = 0;
	for (int i = 0; i < n; i++)
		s += vector[i];
	return s;
}

int Error2(int a)
{
	do
	{
		a--;
	} 	while (a > 0);

	return a;
}

int main()
{
	/*int a, b, n, vector[100];
	a = 12; b = 30;
	int raza=3;
	cout << PerimetruCerc(raza) << " " << AriaCerc(raza)<<endl;
	cout << cmmdc(a, b) << endl;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin>>vector[i];
	cout << Suma(n,vector);*/
	int a = 4;
	cout << Error2(a);
	return 0;
}