void Tree()
{
     //tree body
     glPushMatrix();
     GLfloat matAmbientTreeBody[] = {0.5,0.5,0.2,1.0};
     glMaterialfv(GL_FRONT,GL_AMBIENT,matAmbientTreeBody);
     glColor3f(1,.6,0);
     glTranslatef(0.0,0.0,0.0);
     glScalef(1.0,2.0,1.0);
     glRotatef(-90.0,1,0,0);
     glutSolidCone(1.0,5.0,40,40);
     glPopMatrix();
     //leaf
     glPushMatrix();
     GLfloat matAmbientLeaf[] = {0.0,1.0,0.0,1.0};
     glMaterialfv(GL_FRONT,GL_AMBIENT,matAmbientLeaf);
     glColor3f(0,1,0);
     glTranslatef(0.0,5.0,0.0);
     glScalef(3.0,2.0,3.0);
     glRotatef(-90.0,1,0,0);
     glutSolidCone(1.0,5.0,40,40);
     glPopMatrix();
     //leaf 2
     glPushMatrix();
     GLfloat matAmbientLeaf2[] = {0.4,1.0,0.0,1.0};
     glMaterialfv(GL_FRONT,GL_AMBIENT,matAmbientLeaf2);
     glTranslatef(0.0,8.0,0.0);
     glScalef(3.0,2.0,3.0);
     glRotatef(-90.0,1,0,0);
     glutSolidCone(1.0,5.0,40,40);
     glPopMatrix();
     //leaf 3
     glPushMatrix();
     GLfloat matAmbientLeaf3[] = {0.0,1.0,0.0,1.0};
     glMaterialfv(GL_FRONT,GL_AMBIENT,matAmbientLeaf3);
     glTranslatef(0.0,10.0,0.0);
     glScalef(3.0,2.0,3.0);
     glRotatef(-90.0,1,0,0);
     glutSolidCone(1.0,5.0,40,40);
     glPopMatrix();
}    
