package com.example.demo.infrastructure.entity;

public class User {
    private Long id;
    private String username;
    private Long age;

    // Getter methods
    public Long getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public Long getAge() {
        return age;
    }

    // Setter methods (Optional)
    public void setId(Long id) {
        this.id = id;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setAge(Long age) {
        this.age = age;
    }
}
