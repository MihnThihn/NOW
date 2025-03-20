package org.example.stockmarket;

public interface Observer {
    void update(String stockName, double price);
}