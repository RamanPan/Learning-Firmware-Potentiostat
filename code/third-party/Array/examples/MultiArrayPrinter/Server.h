// ----------------------------------------------------------------------------
// Server.h
//
//
// Authors:
// Peter Polidoro polidorop@janelia.hhmi.org
// ----------------------------------------------------------------------------
#ifndef SERVER_H
#define SERVER_H
#include "Arduino.h"
#include "Streaming.h"
#include "Array.h"
#include "Constants.h"


template <typename T,
          unsigned int X_SIZE,
          unsigned int Y_SIZE,
          unsigned int Z_SIZE>
class Server
{
public:
  Server(HardwareSerial & serial=Serial);
  void setSerial(HardwareSerial & serial);
  void print();
  template<typename E>
  void printRandomObject(const E & obj);
private:
  HardwareSerial * serial_ptr_;
  Array<T, X_SIZE+constants::RESERVED_X_COUNT> x_;
  Array<T, Y_SIZE+constants::RESERVED_Y_COUNT> y_;
  Array<T, Z_SIZE+constants::RESERVED_Z_COUNT> z_;
  template <unsigned int ARRAY_SIZE>
  void printArray(Array<T,ARRAY_SIZE> array);
};
#include "ServerDefinitions.h"

#endif
