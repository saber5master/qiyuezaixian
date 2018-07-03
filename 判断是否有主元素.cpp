//# -*- coding: utf-8 -*-

//Created on Wed Aug 16 19:55:35 2017

//@author: ice-fire

#include <iostream>  
using namespace std;  
void exchange(int &a,int &b)  
{  
    int tmp=a;  
    a=b;  
    b=tmp;  
}  
int Partition(int *A,int start,int end)  
{  
    int tmp=A[end];  
    int i=start;  
    for (int k=start;k<end;k++)  
    {  
        if(A[k]<=tmp)  
        {  
            exchange(A[k],A[i]);  
            i++;  
        }  
    }  
    exchange(A[i],A[end]);  
    return i;  
  
}  
void findMain(int *A,int length)  
{  
    int mid=(length+1)/2;  
    int q=Partition(A,0,length-1);  
    int s,e;//新的开始和结束点  
    if (mid<q)  
    {  
        s=0;  
        e=q-1;  
    }  
    else  
    {  
        s=q+1;  
        e=length-1;  
    }  
    while(mid!=q)  
    {  
        if (mid<q)  
        {  
            q=Partition(A,s,e);  
        }  
        else   
        {  
            q=Partition(A,s,e);  
        }  
          
        if(mid<q)  
        {  
            e=q-1;  
        }  
        else s=q+1;  
          
    }  
}  
int main()  
{  
    int A[]={1,5,6,5,5,5,3,5};  
    int length=sizeof(A)/sizeof(int);  
    findMain(A,length);  
    int MainMember;  
    int maxleng=0;  
    int tmp=1;  
    for (int k=0;k<length;k++)  
    {  
        tmp=1;  
        while(A[k]==A[k+1]&&k<length-2)  
        {  
            k++;  
            tmp++;  
        }  
        if (tmp>maxleng)  
        {  
            maxleng=tmp;  
            MainMember=A[k];  
        }  
    }  
    if (maxleng>=(length+1)/2)  
    {  
        cout<<MainMember<<endl;  
    }  
    else cout<<-1<<endl;  
    return 0;  
}  
