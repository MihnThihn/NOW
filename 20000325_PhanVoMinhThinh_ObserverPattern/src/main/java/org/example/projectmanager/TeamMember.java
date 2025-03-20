package org.example.projectmanager;

public class TeamMember implements Observer {
    private String name;

    public TeamMember(String name) {
        this.name = name;
    }

    @Override
    public void update(String taskName, String status) {
        System.out.println(name + " nhận thông báo: Công việc '" + taskName + "' đã thay đổi trạng thái thành '" + status + "'");
    }
}