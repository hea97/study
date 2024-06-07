## 기본자료형와 래퍼클래스

### 기본자료형 (Primitive Data Types)

프로그래밍 언어에서 기본적인 데이터 타입.
간단한값을 저장한다. 

자바의 기본 자료형

**정수형**
byte, short, int, long

**실수형**
float, double

**문자형**
char

**논리형**
booleam

---

### 래퍼 클래스 (Wrapper Classes)

기본 자료형을 객체로 감싼 형태, 기본자료형의 값을 객체로 다룰 수 있도록 한다.

자바의 래퍼클래스

**정수형**
Byte, Short, Integer, Long

**실수형**
Float, Double

**문자형**
Character

**논리형**
Boolean

---

![image](https://github.com/hea97/Java_study/assets/168088580/450542a2-8c2d-443e-8427-7f19da5caf74)


**박싱(Boxing)**
기본 자료형의 값을 해당하는 래퍼 클래스 객체로 변환하는 과정.

**언방싱(Unboxing)**
래퍼 클래스 객체를 해당하는 기본 자료형 값으로 변환하는 과정.

ex. int(기본 자료형) → Integer(래퍼 클래스)
int라는 기본 자료형 변수에 정수 값을 저장한다라고 가정하였을때,
이 값을 Integer 래퍼 클래스의 객체로 변환하는 것이 **박싱**이다.
그리고 이를 다시 기본 자료형 변수에 정수 값을 가져오는 것이 **언박싱**이다.

```java
int num = 10;
// 기본 자료형 변수
Integer numObject = num;
// 박싱
Int unmboxedNum = numObject;
// 언박싱
```

---

### Why? 사용하는 이유.

1. 래퍼클래스는 기본 데이터 타입을 Object로 변환할 수 있다!
메소드에 전달된 인수를 수정하려는 경우엔 오브젝트가 필요하다
2. java.util 패키지의 클래스가 객체만 처리하므로 래퍼클래스가 이 경우에 도움이 된다.
3. ArrayList등과 같은 Collection 프레임 워크의 데이터 구조는 기본타입이 아닌 객체만 저장하게 되고 래퍼클레스를 사용하여 자동 방식과 언방식이 일어난다.
4. Null 값을 편리하게 처리해준다.
기본 자료형에서는 null 값이 허용되지 않지만 래퍼 클래스를 사용하게 되면 null 값을 허용할 수 있다.
null 유도하는 경우는 많지 않지만
→ checked crror에서 unchecked error로 에러 타입을 전환시킬 수 있다.
(프로그램이 중지되는 에러에서 중지되지 않는 에러로 전환시킴.)

> 기본 자료형 null 사용
> 

```java
int a = 5;
int b = 0;
// 기본 자료형 변수는 null을 가질 수 없음
// int c = null;
// 컴파일 오류
```

> 래퍼 클래스 null 사용
> 

```java
Integer a = 5;   
// 래퍼 클래스
Integer b = null; 
// null 값 허용

// null 체크
if (b != null) {
    System.out.println("b is not null");
} else {
    System.out.println("b is null");
}

```

**기본 자료형**은 메모리 효율성, 성능 최적화 등의 이유로 기본 자료형은 null을 허용하지 않는다.
반면에, **래퍼 클래스**에서는 null을 사용하면 값이 없음을 명확히 표현 할 수 있고. DB와의 사용작용, 컬렉션 사용, ‘Optional’ 클래스 활용 등의 상황에 융용하기 때문에 허용한다.
