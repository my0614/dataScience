#include <avr/io.h>
#include <util/delay.h>
#define EX_LED (*(volatile unsigned char *)0x8008)
int main(void)
{
  int i=0;
  int toggle = 0;
  port_init();
  MCUCR = 0x80;
  PORTD = 0xff; // PORTD 초기값 설정
  DDRD = 0xff; // PORTD 모두 출력으로 설정
  PORTB = 0xff;
  DDRB = 0x00; // PORTB 입력으로 설정
  while (1)
  {
    //왼쪽에서 오른쪽
    if((PINB & 0x01) == 0)
    {
        toggle = 1;
    }
    //오른쪽에서 왼쪽
    if((PINB & 0x02) == 0)
    {
        toggle = 2;
    }
    // 깜빡거림버튼
    if((PINB & 0x04) == 0)
    {
        EX_LED= 0xff;
        _delay_ms(500);
        EX_LED= 0x00;
        _delay_ms(500);
    }
    else
    {
        EX_LED = 0xff;
        _delay_ms(500);

    }
    switch(toggle)
    {
      case 1: 
      EX_LED = 0xff;
      _delay_ms(500);
      for(int i=0;i<8;i++)
      {
        EX_LED = (EX_LED <<i);
        _delay_ms(500);
      }
      break;

      case 2:
      EX_LED = 0xff;
      _delay_ms(500);
      for(int i=8;i>=0;i--)
      {
        EX_LED = (EX_LED <<i);
        _delay_ms(500);
      }
      _delay_ms(500);
      break;
    }
  }
}