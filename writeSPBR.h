#ifndef _writeSPBR_H__
#define _writeSPBR_H__

#include <kvs/PolygonObject>
#include <vector>
#include <fstream>
#include <cstdlib>

enum WritingDataType {
    Ascii = 0,
    Binary = 1
};

// default
const float NORMAL[3]   = { 0.0, 0.0, 0.0 };
const int   COLOR[3]    = { 255, 255, 255 };

void writeSPBR( kvs::PolygonObject *_ply, 
                char* _filename,  
                float _correct_parameter,
                WritingDataType _type = Ascii) {
    size_t  num         = _ply->numberOfVertices(); 
    bool    hasNormal   = false;
    bool    hasColor    = false;
    if( num == _ply->numberOfNormals() ) hasNormal   = true; 
    if( num == _ply->numberOfColors() )  hasColor    = true;
    kvs::ValueArray<kvs::Real32>         coords      = _ply->coords();  
    kvs::ValueArray<kvs::Real32>         normals     = _ply->normals();
    kvs::ValueArray<kvs::UInt8>          colors      = _ply->colors();

    std::ofstream fout( _filename );
    if ( _type == Ascii ) {
        fout << "#/SPBR_ASCII_Data"       << std::endl;
        fout << "#/RepeatLevel 100"       << std::endl;
        fout << "#/BGColorRGBByte 0 0 0"  << std::endl;
        fout << "#/ImageResolution 1000"  << std::endl;
        fout << "#/Shading 0"             << std::endl;
        fout << "#/EndHeader"             << std::endl;
    }

    // Write to ouput file
    int R_over_255_count=0;
    int G_over_255_count=0;
    int B_over_255_count=0;
    for ( int i = 0; i < num; i++ ) {
        // coords                                               
        float x = coords[3*i];
        float y = coords[3*i+1];
        float z = coords[3*i+2];

        // normal(default)
        float nx = NORMAL[0];
        float ny = NORMAL[1];
        float nz = NORMAL[2];
        if ( hasNormal ) {
            nx = normals[ 3*i ];
            ny = normals[ 3*i+1 ];
            nz = normals[ 3*i+2];
        }

        // color(default)
        int r = COLOR[0];
        int g = COLOR[1];
        int b = COLOR[2];
        if ( hasColor ) {
            // ----------------------------------
            // ----- Correct original color -----
            // ----------------------------------
            r = (int)colors[3*i]    * _correct_parameter;
            if (r > 255) {
                r = 255;
                R_over_255_count++;
            }

            g = (int)colors[3*i+1]  * _correct_parameter;
            if (g > 255) {
                g = 255;
                G_over_255_count++;
            }

            b = (int)colors[3*i+2]  * _correct_parameter;
            if (b > 255) {
                b = 255; 
                B_over_255_count++;
            }

        } else {
            std::cout << "\nhas not color!\n" << std::endl;
            exit(1);
        }

        // Binary
        if( _type == Binary ) {
            fout.write( (char*)&x, sizeof(float) );
            fout.write( (char*)&y, sizeof(float) );
            fout.write( (char*)&z, sizeof(float) );
            fout.write( (char*)&nx, sizeof(float) );
            fout.write( (char*)&ny, sizeof(float) );
            fout.write( (char*)&nz, sizeof(float) );

            unsigned char cl = (unsigned char)r;
            fout.write( (char*)&cl, sizeof(unsigned char) );
            cl = (unsigned char)g;
            fout.write( (char*)&cl, sizeof(unsigned char) );
            cl = (unsigned char)b;
            fout.write( (char*)&cl, sizeof(unsigned char) );

            // float tmp = _ni[i]; 
            // fout.write( (char*)&tmp, sizeof(float) );
            
        // Ascii
        } else {     
            fout    << x   << " " << y  << " " << z  << " "
                    << nx  << " " << ny << " " << nz << " "
                    << r   << " " << g  << " " << b  << " " 
                    << std::endl;
        }
    } // end for

    std::cout << "\ncorrect_parameter\n> " << (float)_correct_parameter << std::endl;

    std::cout << "\nR_over_255_count\n> " << R_over_255_count << std::endl;
    std::cout << "> " << (float)R_over_255_count/(float)num*100.0 << "(%)" << std::endl;

    std::cout << "\nG_over_255_count\n> " << G_over_255_count << std::endl;
    std::cout << "> " << (float)G_over_255_count/(float)num*100.0 << "(%)" << std::endl;

    std::cout << "\nB_over_255_count\n> " << B_over_255_count << std::endl;
    std::cout << "> " << (float)B_over_255_count/(float)num*100.0 << "(%)" << std::endl;

    fout.close();
}


#endif
