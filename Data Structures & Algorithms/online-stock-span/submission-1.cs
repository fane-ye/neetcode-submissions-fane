// using System.Collections.Generic;
public class StockInfo {
    public int Day {get; set;}
    public int Price {get; set;}

    public StockInfo(int dayVal, int priceVal) {
        Day = dayVal;
        Price = priceVal;
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

        while (prices.Peek().Price <= price) {
            Console.WriteLine("popping: " + prices.Peek().Price);
            prices.Pop();
        }

        int span = this.day - prices.Peek().Day;

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