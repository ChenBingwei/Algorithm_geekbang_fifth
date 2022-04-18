//
// Created by Opt_c on 2022/4/18.
//
#include <bits/stdc++.h>

using namespace std;

class MinStack {
public:
    MinStack() {

    }

    void push(int val) {
        a.push(val);
        if (preMin.empty()) preMin.push(val);
        else preMin.push(min(preMin.top(), val));
    }

    void pop() {
        a.pop();
        preMin.pop();

    }

    int top() {
        return a.top();
    }

    int getMin() {
        return preMin.top();
    }

private:
    stack<int> a;
    stack<int> preMin;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */