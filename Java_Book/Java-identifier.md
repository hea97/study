**식별자(identifier)**
프로그램에서 사용하는 변수, 메서드, 클래스, 상수 등도 이름으로 구별

식별자 작성시 따라야할 규칙

- 문자, 언더바(_), $로 시작
한글도 가능, 영문자는 대소문자를 구별해야한다.
- +, -등 연산자를 포함하면 안된다.
- [자바 키워드](https://www.notion.so/1db2554f7a3349638215aea017c7dbfe?pvs=21) 를 사용하면 안된다.
- 길이에 제한이 없다.

ex. %5, a+b, 1b 잘못된 식별자
    ColoredCircle, radius, $a, _int 올바른 식별자
→ 대소문자 구별로 x, X는 서로 다름

### **식별자를 정할 때 가독성을 높이는 방법**

1. 변수의 메서드는 모두 소문자로 표기한다.
→ 복합 단어일 때는 두 번째 단어부터 단어의  첫자만 대문자로 표기

```java
int thisYear;
String currentPosition;
boolean isEmpty;
public int getYEar() {}
```

1. 클래스와 인터페이스는 첫 자만 대문자로 표기하고 나머지는 소문자로 표기.
→ 복합 단어일 때는 각 단어의 첫 자만 대문자로 표기.

```java
public class HelloDemo{}
public interface MyRunnable {}

```

1. 상수는 전체를 대문자로 표기.
→ 복합 단어일 때는 단어를 언더바(_)로 연결.

```java
final int NUMBER_ONE = 1;
final double PI = 3.141592
```
