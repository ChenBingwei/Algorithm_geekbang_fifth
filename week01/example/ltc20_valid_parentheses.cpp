//
// Created by Opt_c on 2022/4/18.
//
#include <bits/stdc++.h>
#include <cassert>

using namespace std;


class Solution {
public:
    bool isValid(string s) {
        for (char ch: s) {
            if (ch == '(' || ch == '[' || ch == '{') a.push(ch);
            else {
                if (a.empty()) return false;
                if (ch == ')' && '(' != a.top()) return false;
                if (ch == ']' && '[' != a.top()) return false;
                if (ch == '}' && '{' != a.top()) return false;
                a.pop();
            }
        }
        return a.empty();
    }

private:
    stack<char> a;
};


int main() {
    assert(Solution().isValid("()") == true);
    assert(Solution().isValid("{[]}") == true);
    assert(Solution().isValid("([)]") == false);
    return 0;
}