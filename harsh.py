#include<fstream>
#include<iostream>
#include<conio.h>
using namespace std;
class student
{
private:
string name;
int rollno;
public:
void add_info()
{
fstream fs;
fs.open("D:\\Welcome\\Student Info.txt",ios::app);
if(!fs)
cout<<"File creation failed....";
else
{
cout<<"\n Enter name: ";
cin>>name;
cout<<"\n Enter roll no: ";
cin>>rollno;
fs<<name<<" ";
fs<<rollno<<"\n";
fs.close();
}
}
void display_info()
{
fstream fs;
fs.open("D:\\Welcome\\Student Info.txt",ios::in);
if(!fs)
cout<<"No such file...";
else
{
while(!fs.eof())
{
fs>>name;
fs>>rollno;
cout<<name<<" ";
cout<<rollno;
cout<<"\n";
}
fs.close();
}
}
};
int main()
{
int ch;
student s;
fstream fs;
do
{
cout<<"\n ***Student Information*** ";
cout<<"\n ***Menu*** ";
cout<<"\n 1.Add Information";
cout<<"\n 2.Dislay Information";
cout<<"\n 3.Exit";
cout<<"\n Enter Choice: ";
cin>>ch;
switch (ch)
{
case 1:
s.add_info();
break;
case 2:
s.display_info();
break;
case 3:
exit(0);
}
} while (ch != 3);
return 0;
}
