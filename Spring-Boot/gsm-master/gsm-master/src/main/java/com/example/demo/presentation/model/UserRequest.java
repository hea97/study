package com.example.demo.presentation.model;

import com.example.demo.infrastructure.entity.User;

public class UserRequest {
    private Long id;
    private String username;
    private Long age;

    // Constructor, getters, and setters

    public Long getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public Long getAge() {
        return age;
    }

    public User toEntity() {
        User user = new User();
        user.setId(this.id);
        user.setUsername(this.username);
        user.setAge(this.age);
        return user;
    }
}
