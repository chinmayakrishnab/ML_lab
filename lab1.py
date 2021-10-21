{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the first number 1000\n",
      "enter the second number 20\n",
      "1.add 2.subtract 3.multiply 4.divide 4\n",
      "50.0\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the first number \")\n",
    "b=input(\"enter the second number \")\n",
    "st=input(\"1.add 2.subtract 3.multiply 4.divide \")\n",
    "if(int(st)==1):\n",
    "    print(int(a)+int(b))\n",
    "elif(int(st)==2):\n",
    "    print(int(a)-int(b))\n",
    "elif(int(st)==3):\n",
    "    print(int(a)*int(b))\n",
    "else:\n",
    "    print(int(a)/int(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string qwerty\n",
      "1.len 2.concat 3.substring or not 4.reverse4\n",
      "ytrewq\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string \")\n",
    "st=input(\"1.len 2.concat 3.substring or not 4.reverse \")\n",
    "if(int(st)==1):\n",
    "    i=0\n",
    "    count=0\n",
    "    while(i!=len(a)):\n",
    "        i=i+1\n",
    "        count=count+1\n",
    "    print(count)\n",
    "elif(int(st)==2):\n",
    "    b=input(\"enter the 2nd string to concatinate \")\n",
    "    c=a+b\n",
    "    print(c)\n",
    "elif(int(st)==3):\n",
    "    b=input(\"enter the substring \")\n",
    "    i=0\n",
    "    j=0\n",
    "    k=0\n",
    "    while(i!=len(a)):\n",
    "        if(a[i]==b[j]):\n",
    "            j=j+1\n",
    "            if(j==len(b)):\n",
    "                print(b + \" is a substring of \"+ a)\n",
    "                k=1\n",
    "                break\n",
    "            else:\n",
    "                i=i+1\n",
    "                continue\n",
    "        else:\n",
    "            i=i+1\n",
    "            j=0\n",
    "    if(k!=1):\n",
    "        print(b + \" is not a substring of \"+ a)\n",
    "else:\n",
    "    i=len(a)-1\n",
    "    st=\"\"\n",
    "    while(i>=0):\n",
    "        st+=a[i]\n",
    "        i=i-1\n",
    "    print(st)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst=[\"hello\",50,\"hi\",1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[50]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst[1:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "50\n",
      "hi\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "for i in lst:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst[2]=\"hey\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hey'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst.append(\"okay\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hello', 50, 'hey', 1, 'okay']"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'okay'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hello', 50, 'hey', 1]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "d={\"name\":\"qwerty\",\"age\":21,\"address\":\"bangalore\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'qwerty', 'age': 21, 'address': 'bangalore'}"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name  :  qwerty \n",
      "\n",
      "age  :  21 \n",
      "\n",
      "address  :  bangalore \n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in d:\n",
    "    print(i,\" : \",d[i],\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "d1={\"ph.No\":98672524,\"gender\":\"M\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
