package org.example.stockmarket;

public class StockMarketApp {
    public static void main(String[] args) {
        Stock apple = new Stock("Apple", 150.0);
        Stock google = new Stock("Google", 2800.0);

        Observer investor1 = new Investor("Nguyễn Văn A");
        Observer investor2 = new Investor("Trần Thị B");

        apple.addInvestor(investor1);
        apple.addInvestor(investor2);
        google.addInvestor(investor1);

        System.out.println("Giá cổ phiếu thay đổi...");
        apple.setPrice(155.5);
        google.setPrice(2850.0);
    }
}