package com.example.demo.presentation.model;

import com.example.demo.infrastructure.entity.User;

public class UserResponse {
    public Long id;
    public String username;
    public Long age;

    public UserResponse(User user) {
        this.id = user.getId();
        this.username = user.getUsername();
        this.age = user.getAge();
    }
}