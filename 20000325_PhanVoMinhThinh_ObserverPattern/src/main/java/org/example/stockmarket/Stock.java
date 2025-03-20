package org.example.stockmarket;

import java.util.ArrayList;
import java.util.List;

public class Stock {
    private String name;
    private double price;
    private List<Observer> investors = new ArrayList<>();

    public Stock(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public void addInvestor(Observer investor) {
        investors.add(investor);
    }

    public void removeInvestor(Observer investor) {
        investors.remove(investor);
    }

    public void setPrice(double price) {
        this.price = price;
        notifyInvestors();
    }

    private void notifyInvestors() {
        for (Observer investor : investors) {
            investor.update(name, price);
        }
    }
}