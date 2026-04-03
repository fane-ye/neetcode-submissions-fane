public class Solution {
    public int CalPoints(string[] operations) {
        string[] ops = ["+", "C", "D"];
        Stack<int> stack = new Stack<int>();

        for (int i = 0; i < operations.Length; i++) {
            string val = operations[i];
            if (ops.Contains(val)) {
                //pop stack twice

                //if plus
                int a;
                int b;
                if (val == "+") {
                    a = stack.Pop();
                    b = stack.Pop();
                    stack.Push(b);
                    stack.Push(a);
                    Console.WriteLine("adding sum " + (a+b));
                    stack.Push(a + b);
                }
                //if double
                else if (val == "D") {
                    a = stack.Pop();
                    stack.Push(a);
                    stack.Push(a * 2);
                    Console.WriteLine("adding product " + (a*2));
                } else { //remove
                    stack.Pop();
                }

            }
            else {
                //push onto stack
                stack.Push(int.Parse(val));
            }
        }       
        int sum = 0;
        while (stack.Count > 0) {
            sum += stack.Pop();
        } 
    return sum;
    }
}