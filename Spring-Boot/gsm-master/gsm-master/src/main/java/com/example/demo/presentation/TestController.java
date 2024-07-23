package com.example.demo.presentation;

import com.example.demo.presentation.model.UserRequest;
import org.springframework.web.bind.annotation.*;

@RestController
public class TestController {

    @GetMapping("/{id}")
    public String test(@PathVariable Long id) {
        return "Your id is " + id.toString();
    }

    @PostMapping
    public String post(@RequestBody UserRequest userRequest) {
        return "Your age is " + userRequest.getAge();
    }
}
