#include <stack>
using namespace std;

class MinStack {
public:

    stack<int> mainStack;
    stack<int> minStack;

    MinStack() {
        
    }
    
    void push(int val) {
        // Always push the value onto the main stack
        mainStack.push(val);

        // If the minStack is empty or val is less than or equal to the current minimum, push it
        if (minStack.empty() || val <= minStack.top()){
            minStack.push(val);
        }
    }
    
    void pop() {
        // If the top elements of mainStack and minStack are the same, pop from the minStack
        if (mainStack.top() == minStack.top()){
            minStack.pop();
        }
        mainStack.pop();
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */