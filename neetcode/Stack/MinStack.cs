// __Big O Time__
// O(1). This is because there is no iterations, it's just a grab the top of everything. This is the best time complexity as constant time is the best.

// __Space Complexity__
// O(n). This is because there we create 2 linked lists of possible size input n.

public class MinStack {
    private LinkedList<int> head;
    private LinkedList<int> min;

    public MinStack() {
        head = new();
        min = new();
    }
    
    public void Push(int val) {
        head.AddFirst(val);
        
        if (min.Count == 0 || min.First.Value >= val){
            min.AddFirst(val);
        }
    }
    
    public void Pop() {
        int x = head.First.Value;
        head.RemoveFirst();

        if (min.First.Value == x){
            min.RemoveFirst();
        }
    }
    
    public int Top() {
        return head.First.Value;
    }
    
    public int GetMin() {
        return min.First.Value;
    }
}
