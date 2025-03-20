package org.example.stockmarket;

public class Investor implements Observer {
    private String name;

    public Investor(String name) {
        this.name = name;
    }

    @Override
    public void update(String stockName, double price) {
        System.out.println("Nhà đầu tư " + name + " nhận thông báo: Giá cổ phiếu " + stockName + " thay đổi thành " + price);
    }
}