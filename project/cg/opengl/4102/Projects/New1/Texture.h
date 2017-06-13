#include<iostream>
using namespace std;
GLuint LoadTexture1( const char * filename, int width, int height )
{
  GLuint texture;
  unsigned char * data;
  FILE * file;
  file = fopen( filename, "rb" );
  if ( file == NULL ) return 0;
  data = (unsigned char *)malloc( width * height * 3 );
  fread( data, width * height * 3, 1, file );
  fclose( file ); 
  
//for(int i = 0; i < width * height ; ++i) swap(data[i*3],data[i*3+2]);
  glGenTextures(1, &texture );
  glBindTexture(GL_TEXTURE_2D, texture);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    //when the texture area is large, repeat texel nearest center
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    //when the texture area is small, repeat texel nearest center
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
  free( data );
  return texture;
}

void FreeTexture( GLuint texture ){ glDeleteTextures( 1, &texture ); }
