#include <fstream>
#include <iostream>

#include "divideRandomly.h"
#include "shuffle.h"

// #include <cmath>
// #include <vector>
// #include <math.h>

// default
const float NORMAL[3]   = { 0.0, 0.0, 0.0 };
const int   COLOR[3]    = { 255, 255, 255 };

DivideRandomly::DivideRandomly( const kvs::PolygonObject* ply, const size_t repeat_level )
{
    DoRandomDivision( ply, repeat_level );
}

void DivideRandomly::DoRandomDivision( const kvs::PolygonObject* ply, const size_t repeat_level ) {
    const size_t num_of_input_points = ply->numberOfVertices();
    const int num_of_points_in_each_ensemble = (int)num_of_input_points / (int)repeat_level;
    std::cout << "Num. of input points : " << num_of_input_points << std::endl;
    std::cout << "Repeat level         : " << repeat_level << std::endl;
    std::cout << "Num. of points in each ensemble : " << num_of_points_in_each_ensemble << std::endl;

    // Shuffle
    kvs::PointObject* object = new kvs::PointObject( *ply );
    Shuffle shuffle_engine( object );
    object->setSize( 1 );
    object->updateMinMaxCoords();

    // Reset
    bool hasNormal = false;
    bool hasColor  = false;
    if ( num_of_input_points == object->numberOfNormals() ) hasNormal   = true; 
    if ( num_of_input_points == object->numberOfColors() )  hasColor    = true;
    kvs::ValueArray<kvs::Real32> coords     = object->coords();
    kvs::ValueArray<kvs::Real32> normals    = object->normals();
    kvs::ValueArray<kvs::UInt8>  colors     = object->colors();

    // Write to spbr file
    for ( size_t j = 0; j < repeat_level; j++ ) {
        // Set output file name
        std::string out_spbr_file_name = "OUTPUT_DATA/LR10/funehoko/ensemble";
        std::ostringstream oss;
        oss << j+1;
        out_spbr_file_name += oss.str();
        out_spbr_file_name += ".spbr";
        std::ofstream fout( out_spbr_file_name.c_str() );
            
        // Set spbr parameter
        fout << "#/SPBR_ASCII_Data"       << std::endl;
        fout << "#/RepeatLevel 1"         << std::endl;
        fout << "#/BGColorRGBByte 0 0 0"  << std::endl;
        fout << "#/ImageResolution 1000"  << std::endl;
        // fout << "#/BoundingBox 0.15 0.15 0 0.85 0.85 0" << std::endl;
        fout << "#/Shading 0"             << std::endl;
        fout << "#/EndHeader"             << std::endl;

        for ( size_t i = 0; i < num_of_points_in_each_ensemble; i++ ) {
            // if ( i == 0) std::cout << "ensamble" << j+1 << " : " << 3*j*num_of_points_in_each_ensemble + 3*i << std::endl;
            // if ( i == 0) std::cout << "ensamble" << j+1 << " : " << 3*j*num_of_points_in_each_ensemble + 3*i+1 << std::endl;
            // if ( i == 0) std::cout << "ensamble" << j+1 << " : " << 3*j*num_of_points_in_each_ensemble + 3*i+2 << std::endl;


            // coords
            float x = coords[ 3*j*num_of_points_in_each_ensemble + 3*i   ];
            float y = coords[ 3*j*num_of_points_in_each_ensemble + 3*i+1 ];
            float z = coords[ 3*j*num_of_points_in_each_ensemble + 3*i+2 ];

            // normal(default)
            float nx = NORMAL[0];
            float ny = NORMAL[1];
            float nz = NORMAL[2];
            if ( hasNormal ) {
                nx = normals[ 3*j*num_of_points_in_each_ensemble + 3*i   ];
                ny = normals[ 3*j*num_of_points_in_each_ensemble + 3*i+1 ];
                nz = normals[ 3*j*num_of_points_in_each_ensemble + 3*i+2 ];
            }

            // color(default)
            int r = COLOR[0];
            int g = COLOR[1];
            int b = COLOR[2];
            if ( hasColor ) {
                r = colors[ 3*j*num_of_points_in_each_ensemble + 3*i   ];
                g = colors[ 3*j*num_of_points_in_each_ensemble + 3*i+1 ];
                b = colors[ 3*j*num_of_points_in_each_ensemble + 3*i+2 ];
            }

            fout    << x   << " " << y  << " " << z  << " "
                    << nx  << " " << ny << " " << nz << " "
                    << r   << " " << g  << " " << b  << " " 
                    << std::endl;

            
        } // end for

        fout.close();

        // Show progress
        std::cout << "Ensemble" << j+1 << " done." << std::endl;
    } // end for

    std::cout << "\nFile export of all ensembles is complete." << std::endl;

} // End DoRandomDivision()