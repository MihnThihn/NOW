package org.example.projectmanager;

public class ProjectManagerApp {
    public static void main(String[] args) {
        Task task1 = new Task("Thiết kế UI", "Chưa bắt đầu");
        Task task2 = new Task("Phát triển Backend", "Chưa bắt đầu");

        Observer member1 = new TeamMember("Lê Văn C");
        Observer member2 = new TeamMember("Hoàng Thị D");

        task1.addTeamMember(member1);
        task1.addTeamMember(member2);
        task2.addTeamMember(member1);

        System.out.println("Cập nhật trạng thái công việc...");
        task1.setStatus("Đang thực hiện");
        task2.setStatus("Hoàn thành");
    }
}
