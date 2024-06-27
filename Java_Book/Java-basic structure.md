### 소스파일
![image](https://github.com/hea97/Java_study/assets/168088580/e45adf6f-3c2f-4daa-9a19-9b6e998c22aa)

# 클래스

객체 지향언어에서 클래스는 프로그램을 개발하는 단위로 적어도 하나의 클래스가 있어야 한다.
Java 소스 파일 이름은 클래스 이름과 연관되기 때문에 이클립스로 Hello 클래스를 생성
→ Hello.java라는 소스 파일이 생성
클래스 이름은 대문자 시작,
클래스 내부에는 여러 개의 메서드가 포함 된다.

# **메서드(Method)**

수행할 작업을 나열한 코드의 모임.
Java 애플리케이션은 main() 메서드부터 실행을 시작
main() 메서드를 포함한 클래스가 만드시 있어야한다.

# **실행문(Statement)**

작업을 지시하는 변수 선언, 값 저장, 메서드 호출 등의 코드를 의미.
System.out.println() 화면에 정수나 문자, 문자열을 출력하는 실행문.

# **주석문**

프로그램에 덧붙이는 설명문
→ 컴파일러가 무시한다.
1. 행 주석 : // 부터 행끝까지를 주석처리
2. 범위 주석 : /*와 */ 사이를 주석처리
3. 문서 주석 : /**와 **/ 사이를 주석처리 javadoc.exe 명령어로 API 문서 생성하는데 사용된다.

> ex.

```java
public class Hello {
	public static void main(String[] args) {
		System.out.println("안녕, 자바!");
	}
}
```

## **클래스**

```java
public class Hello{
// public class -> 클래스를 정의하기 위한 키워드
// Hello -> 클래스의 이름
// {} -> 클래스의 시작
```

## **메서드**

```java
public static void main(String[] args){ // -> 메세드 시작
//public static void
// ->메서드를 실행한 후 반환할 값이 없음을 의미
// main -> 메서드 이름
// (String[] args) -> 메서드의 매개변수 타입과 매개변수
	//TODO Auto-generated method stud
	System.out.println("안녕, 자바!");
	// 실행문 세미콜론으로 끝남
} // -> 메세드 끝
} // -> 클래스 끝
```
