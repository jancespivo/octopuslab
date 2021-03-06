// bit order, 0bdABCDEFG
//     A
//    ---
// F | G | B
//    ---
// E | D | C
//    ---
//        dot: d

// Special chars
uint8_t special[] = {
  0b00001000, // 00 _
  0b00000001, // 01 -
  0b01000000, // 02 - (upper)
  0b01100011, // 03 degree
  0b00011101, // 04 degree down
  0b01000000, // 05 | pipe A
  0b00100000, // 06 | pipe B
  0b00010000, // 07 | pipe C
  0b00001000, // 08 | pipe D
  0b00000100, // 09 | pipe E
  0b00000010, // 10 | pipe F
  0b00001001, // 11 = (middle and down) G/D
  0b01000001, // 12 = (up and middle) A/G
  0b01001000, // 13 = (up and down) A/D
  0b01001001, // 14 = (up, middle, down) A/G/D
  0b01001110, // 15 [
  0b01111000, // 16 ]
  0b00100100, // 17 /
  0b00010010, // 18 backslash
  0b00000111, // 19 {
  0b00110001  // 20 }
};

// Digit
uint8_t digits[] = {
  0b01111110, // 0
  0b00110000, // 1
  0b01101101, // 2
  0b01111001, // 3
  0b00110011, // 4
  0b01011011, // 5
  0b01011111, // 6
  0b01110000, // 7
  0b01111111, // 8
  0b01111011  // 9
};

// Alpha
uint8_t alpha[] = {
  0b01110111, // A
  0b00011111, // b
  0b00001101, // c
  0b00111101, // d
  0b01001111, // E
  0b01000111, // F
  0b01011110, // G
  0b00010111, // h
  0b00000100, // i
  0b00111100, // J
  0b00110111, // K
  0b00001110, // L
  0b00010101, // m
  0b00010101, // n
  0b00011101, // O
  0b01100111, // P
  0b01110011, // Q
  0b00000101, // r
  0b01011011, // S
  0b00001111, // t
  0b00111110, // U
  0b00011100, // v
  0b00101010, // W
  0b00110111, // X
  0b00111011, // Y
  0b01101101  // Z
};

// Alpha
uint8_t ALPHA[] = {
  0b01110111, // A
  0b01111111, // B
  0b01001110, // C
  0b00111101, // d
  0b01001111, // E
  0b01000111, // F
  0b01011110, // G
  0b00110111, // H
  0b00000110, // I
  0b00111100, // J
  0b00110111, // K
  0b00001110, // L
  0b01110110, // M
  0b01110110, // N
  0b01111110, // O
  0b01100111, // P
  0b01110011, // Q
  0b00000101, // r
  0b01011011, // S
  0b00001111, // t
  0b00111110, // U
  0b00111110, // V
  0b00101010, // W
  0b00110111, // X
  0b00111011, // Y
  0b01101101  // Z
};
