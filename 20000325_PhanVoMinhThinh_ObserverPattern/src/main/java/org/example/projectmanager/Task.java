package org.example.projectmanager;

import java.util.ArrayList;
import java.util.List;

public class Task {
    private String name;
    private String status;
    private List<Observer> teamMembers = new ArrayList<>();

    public Task(String name, String status) {
        this.name = name;
        this.status = status;
    }

    public void addTeamMember(Observer member) {
        teamMembers.add(member);
    }

    public void removeTeamMember(Observer member) {
        teamMembers.remove(member);
    }

    public void setStatus(String status) {
        this.status = status;
        notifyTeamMembers();
    }

    private void notifyTeamMembers() {
        for (Observer member : teamMembers) {
            member.update(name, status);
        }
    }
}