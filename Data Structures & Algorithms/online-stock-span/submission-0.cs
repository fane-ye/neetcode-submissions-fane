// using System.Collections.Generic;
public class StockInfo {
    public int day;
    public int price;

    public StockInfo(int dayVal, int priceVal) {
        day = dayVal;
        price = priceVal;
    }
}

public class StockSpanner {

    Stack<StockInfo> prices;
    int day;
    public StockSpanner() {
        //mantain a monotonically decreasing stack
        prices = new Stack<StockInfo>();
        prices.Push(new StockInfo(0, int.MaxValue));
        day = 0;
        
    }
    
    public int Next(int price) {
        this.day++;

        while (prices.Peek().price <= price) {
            Console.WriteLine("popping: " + prices.Peek().price);
            prices.Pop();
        }

        int span = this.day - prices.Peek().day;

        StockInfo stock = new StockInfo(day, price);
        prices.Push(stock);
        
        return span;
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */