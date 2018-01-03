#include <iostream>
int main(int argc, char const *argv[]) {
  std::cout << "{" << '\n';
  char diccionario[]="! #$%&'()*+,-./:;<=>?@[]\^_`{}|0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  char diccionario2[]="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  char diccionario3[]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  char diccionario4[]="pqrstuvLMNOPQRSTUVWXYZabcdefghijklmnowxyz123456789ABCDEFGHIJK";
  int valor=0;
  int incrementp =1;
  for (int i =0 ; i < 94; i++) {
    std::cout << "'"<<diccionario[i]<<"' : '"<<diccionario2[valor]<<diccionario3[valor]<<diccionario4[valor]<<"',";
    valor+=incrementp;
    if (valor>62) {
      incrementp--;
    }
  }
  std::cout << "}" << '\n';
  return 0;
}
